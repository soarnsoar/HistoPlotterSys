import ROOT
from JHProcHist import JHProcHist
from JHReader import Reader
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile
from copy import deepcopy
import time
import psutil
def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    print(memory_info.rss/1024./1024.,"MB")


maindir=os.getenv("GIT_HistoPlotterSys")

class JHEffPurityReader:
    def __init__(self,effname,path_confdef,Year,AnalyzerName,suffix,procconfpath,rebin=[]):
        self.procconfpath=procconfpath
        self.path_confdef=path_confdef
        ##cuts/xs= [deno,nume]
        self.suffix=suffix
        Year=str(Year)
        name="__".join([Year,AnalyzerName])
        self.Year=Year
        self.AnaName=AnalyzerName
        self.rebin=rebin
        self.effname=effname

        self.dict_eff={}
        self.dict_effobj={}
        self.ReadEffPurityDef()
        

        
        self.ReadData()

    def ReadEffPurityDef(self):
        ##eff_def.py
        #_confpath="/".join([maindir,"config",self.AnaName,self.Year,"eff_def.py"])
        _conf=OpenDictFile(self.path_confdef)
        self.dict_eff=_conf[self.effname]
    def ReadData(self):
        
        self.myreader=Reader(self.AnaName,self.Year,self.suffix,self.procconfpath)
        ###----read components one by one----###
        for dn in ["nume","deno"]:
            
            self.LoadHPColl(dn) ##denominator and numerator hists of process in procconf 
            self.MakeCombinedObject(dn)
            
            ##--now denominator and numerator are ready. Make HP of effciency
        self.MakeEfficiencyObjects()
        self.myreader.CloseFile()
        ##---remove objects of each subprocess
        #for info in sorted(self.dict_effobj):
        #    for proc in sorted(self.dict_effobj[info]):
        #        if proc in ["Data","sig","bkg","Data-bkg"]: continue
        #        #del self.dict_effobj[info][proc]
        #for info in sorted(self.dict_effobj):
        #    for proc in sorted(self.dict_effobj[info]):
        #        print proc
    def LoadHPColl(self,dn):
        ###----Using given denominator and numerator def, get necessary histoproc objects

        cuts=self.dict_eff[dn]["cut"]
        x=self.dict_eff[dn]["x"]
        for i,cut in enumerate(cuts):
            print(cut,x)
            this_hp_coll=self.myreader.MakeHistContainer(cut,x,self.rebin)            
            ##---Make MC stat nuisances shapes---##
            for proc in self.myreader.ProcConf:
                if proc.lower()=="data":
                    #print "it's data, skip statnuis"
                    continue
                this_hp_coll[proc].MakeStatNuiShapes(str(self.Year))
            ##------
            if i==0:
                self.dict_effobj[dn]=this_hp_coll                    
            else:
                for proc in self.myreader.ProcConf:            
                    self.dict_effobj[dn][proc]=self.dict_effobj[dn][proc].Combine(this_hp_coll[proc],cut,x,proc)
            #del this_hp_coll
    def GetEmptyHist(self,dn):
        for _p in sorted(self.dict_effobj[dn]):
            _h=self.dict_effobj[dn][_p].GetHist().Clone()
            _h.Reset()
            return _h
    def MakeCombinedObject(self,dn):
        HasData=False
        HistColl=self.dict_effobj[dn]
        if "Data" in HistColl: HasData=True
        
        
        cut="__".join(self.dict_eff[dn]["cut"])
        x=self.dict_eff[dn]["x"]
        
        hp_data=JHProcHist(cut,x,"Data"+dn)
        if HasData:
            hp_data.Clone(HistColl["Data"])
        else:
            hp_data.SetHist(self.GetEmptyHist(dn))
        hp_sig=JHProcHist(cut,x,"sig")
        hp_bkg=JHProcHist(cut,x,"bkg")
        ##as data has leptonscale variations, propagate them to mc sys.
        ##e.g)mc_up_new = mc_up_old/data_up*data_nom
        ##then data_nom/mc_up_new = data_nom/mc_up_old*data_up/data_nom = data_up/mc_up //good

        dosysnorm=False
        if HasData:
            if HistColl["Data"].GetHist().Integral()!=0:dosysnorm=True
        
        ## divide mc by data_var/data
        

        hp_data_nosys=JHProcHist(cut,x,"data_nosys")
        if HasData:
            hp_data_nosys.SetHist(HistColl["Data"].GetHist().Clone()) ## add only nominal
        else:
            hp_data_nosys.SetHist(self.GetEmptyHist(dn))
        hp_norm_data_sys=hp_data.Divide(hp_data_nosys)
        ##---Need to make each binerror to zero for self.hp_norm_data_sys(it disturbs mcstat variation)
        hp_norm_data_sys.MakeBinErrorZero()
        
        ##now divide all mc with self.hp_norm_data_sys
        i_sig=0
        i_bkg=0
        siglist=self.dict_eff["sig"]
        bkglist=self.dict_eff["bkg"]
        if len(siglist)==0:
            hp_sig=JHProcHist(cut,x,"sig")
            hp_sig.SetHist(self.GetEmptyHist(dn))
        if len(bkglist)==0:
            hp_bkg=JHProcHist(cut,x,"bkg")
            hp_bkg.SetHist(self.GetEmptyHist(dn))
        for i,proc in enumerate(self.myreader.ProcConf):
            _h=HistColl[proc].GetHist().Clone()
            if proc=="Data" :
                continue
            ##--systematic norm with data var
            if dosysnorm : HistColl[proc]=HistColl[proc].Divide(hp_norm_data_sys)
            
            if proc in siglist:
                #
                print("sig->",proc)
                if i_sig==0:
                    hp_sig.Clone(HistColl[proc])
                else:
                    hp_sig=hp_sig.Combine(HistColl[proc],cut,x,"sig")
                i_sig+=1

            if proc in bkglist:
                if i_bkg==0:
                    hp_bkg.Clone(HistColl[proc])
                else:
                    hp_bkg=hp_bkg.Combine(HistColl[proc],cut,x,"bkg")
                i_bkg+=1

        ##---Because we generate mc-stat shapes, remove stat err of each histogram 
        hp_sig.MakeBinErrorZero()
        hp_bkg.MakeBinErrorZero()
        self.dict_effobj[dn]["sig"]=hp_sig
        self.dict_effobj[dn]["bkg"]=hp_bkg
        

        ##---Now, sig and bkg shapes are ready
        ##---subtract bkg from Data
        hp_data_sub_bkg=JHProcHist(cut,x,"Data_sub_bkg"+dn)
        hp_data_sub_bkg.Clone(hp_data)
        hp_data_sub_bkg=hp_data_sub_bkg.Subtract(hp_bkg,cut,x,"Data-bkg"+dn)
        self.dict_effobj[dn]["Data-bkg"]=hp_data_sub_bkg


    def MakeEfficiencyObjects(self):
        ##HP of efficiency
        self.dict_effobj["eff"]={}
        self.dict_effobj["eff"]["Data-bkg"]=self.dict_effobj["nume"]["Data-bkg"].Divide(self.dict_effobj["deno"]["Data-bkg"])
        ##--data-bkg, include data stat to total errbar
        self.dict_effobj["eff"]["Data-bkg"].MakeStatNuiShapes()

        self.dict_effobj["eff"]["sig"]=self.dict_effobj["nume"]["sig"].Divide(self.dict_effobj["deno"]["sig"])

        self.dict_effobj["SF"]=self.dict_effobj["eff"]["Data-bkg"].Divide(self.dict_effobj["eff"]["sig"])
        

    def __del__(self):
        for info in sorted(self.dict_effobj):
            if info=="SF":
                del self.dict_effobj["SF"]
                continue
            for proc in sorted(self.dict_effobj[info]):
                #print "proc=",proc
                #if proc in ["Data","sig","bkg","Data-bkg"]: continue
                del self.dict_effobj[info][proc]

    def GetEffHP(self):
        return self.dict_effobj





if __name__ == "__main__":
    Year=2017
    AnayzerName="TTsemiLepChargeScoreEfficiencyMeasurement"
    #class DefineEffPurity:
    #def __init__(self,Year,AnalyzerName,suffix,rebin=[]):
    print("Read")
    testjob=JHEffPurityReader("Muon_bLep_pt__Usepoor_jetCharge",Year,AnayzerName,"/")
    get_memory_usage()
    print("Get Obj Dict")
    myhp=testjob.GetEffHP()
    get_memory_usage()
    print("del Reader")
    del testjob
    get_memory_usage()
    print("print HP dict")
    for key1 in myhp:
        print("key1=",key1)
        for key2 in myhp[key1]:
            print("key2=",key2)
    print("Read add one")
    testjob=JHEffPurityReader("Muon_bHad_pt__Usepoor_jetCharge",Year,AnayzerName,"/")
    get_memory_usage()
    print("Get Obj Dict2")
    myhp2=testjob.GetEffHP()
    get_memory_usage()
    print("del 2nd Reader")
    del testjob
    get_memory_usage()


    print("rm 1st HP dict")
    del myhp
    get_memory_usage()

    print("rm 2nd HP dict")
    del myhp2
    get_memory_usage()
