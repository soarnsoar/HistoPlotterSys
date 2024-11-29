import ROOT
import os
import json
from copy import deepcopy
from JHProcHist import JHProcHist
from OpenDictFile import OpenDictFile
from GetBinsX import GetBinsX 
from array import array
maindir=os.getenv("GIT_HistoPlotterSys")
##
import time
##
class Reader:
    def __init__(self,AnaName,YEAR,suffix,ProcConfPath,ListNormSysPath=[]):
        self.Verbose=0
        self.suffix=suffix
        self.AnaName=AnaName
        self.YEAR=str(YEAR)
        self.ProcConfPath=ProcConfPath
        self.ListNormSysPath=ListNormSysPath
        self.SetPath()
        self.ReadInput()
        self.ReadConf()
    def SetVerbose(self,_v):
        self.Verbose=_v
    def SetPath(self):
        #if self.runsys:
        #    self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/runSys__/combine.root"
        #else:
        #    self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/combine.root"
        self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix+"/combine.root"
        #print self.inputpath
    def ReadInput(self):
        self.tfile=ROOT.TFile.Open(self.inputpath)
        print self.inputpath
    def ReadConf(self):
        self.ReadProcConf()
        self.ReadNuiConf()
        self.ReadNormSysConfs()
    def ReadProcConf(self):
        _path=self.GetProcConfPath()
        print "--input:",_path
        self.ProcConf=OpenDictFile(_path)

    def GetProcConfPath_OLD(self):
        if os.path.isfile(maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix+"/proc.py"):
            return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix+"/proc.py"
        #print "[Use nominal proc.py file]"
        return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/proc.py"

    def GetProcConfPath(self):
        return self.ProcConfPath


    def ReadNuiConf(self):
        _path=self.GetNuiConfPath()
        #print "--nui:",_path
        self.NuiConf=OpenDictFile(_path)

        #_path=self.GetEffToolConfPath()
        #print "--effnui:",_path
        #self.EffToolConf=OpenDictFile(_path)
    def ReadNormSysConfs(self):
        self.dict_NormSys={}
        for NormSysPath in self.ListNormSysPath:
            this_dict=OpenDictFile(NormSysPath)
            self.dict_NormSys.update(this_dict)
        #print "[self.dict_NormSys]"
        #print self.dict_NormSys
    def GetNuiConfPath(self):
        return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix+"/nuisances.py"
    #def GetEffToolConfPath(self):
    #    return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/nuisances_efftool.py"
    def CheckIsData(self,p):
        return 1 if "IsData" in self.ProcConf[p] and self.ProcConf[p]["IsData"] else 0
    
    def GetEmptyHist(self,cut,x):
        _cut_x=cut+"/"+x
        #print _cut_x
        for _prockey in self.tfile.Get(_cut_x).GetListOfKeys():
            _classname=_prockey.GetClassName()
            #print "_prockey.GetName()=",_prockey.GetName()
            #print "_classname=",_classname
            if not "TH" in _classname: continue
            _proc=_prockey.GetName()
            _path=_cut_x+"/"+_proc
            _h_empty=deepcopy(self.tfile.Get(_path))
            _h_empty.Reset()
            return _h_empty

        raise ValueError("No Histogram in "+_cut_x)
    def MakeHistContainer(self,cut,x,rebin=[]):
        #print "<MakeHistContainer>"
        rebin=array('d',rebin)
        this_container={}
        #print "[MakeHistContainer] in JHReader.py, rebin=",rebin
        ##---Before Start, Make Empty Hist---##
        self._h_empty=self.GetEmptyHist(cut,x)
        if len(rebin)!=0 : 
            self._h_empty=self._h_empty.Rebin(len(rebin)-1,self._h_empty.GetName(),rebin)
        for p in self.ProcConf:
            subplist=self.ProcConf[p]["procs"]
            IsData=self.CheckIsData(p)
            this_container[p]=JHProcHist(cut,x,p)
            for isubp,subp in enumerate(sorted(subplist)):
                this_h=JHProcHist(cut,x,subp) ##JHProcHist for this proc
                p_weight=False ### For example, Add this subp with p_weight==1 if combined proc is A-B
                if not isinstance(subplist,list):##if subp info is  not a simple list.(For example it would have "weight"key)
                    if "weight" in subplist[subp] : p_weight=subplist[subp]["weight"]
                ##-----NominalShape-----#
                this_nominal=self.ReadNominalShape(cut,x,subp)
                
                if len(rebin)!=0 : this_nominal=this_nominal.Rebin(len(rebin)-1,this_nominal.GetName(),rebin)
                if p_weight: this_nominal.Scale(p_weight)

                this_h.SetHist(deepcopy(this_nominal))##set only nominal. No sys
                

                ##----NuisanceShape-----#
                for nui in self.NuiConf:
                    if IsData :
                        if nui!="electronscale" and nui!="muonscale" : continue
                    for idx1 in self.NuiConf[nui]:
                        for idx2 in self.NuiConf[nui][idx1]:
                            this_sys=self.ReadNuisanceShape(cut,x,subp,nui,idx1,idx2)
                            if len(rebin)!=0 : this_sys=this_sys.Rebin(len(rebin)-1,this_sys.GetName(),rebin)
                            if p_weight: this_sys.Scale(p_weight)
                            this_h.SetHist(deepcopy(this_sys),nui,idx1,idx2)
                    #this_h.MakeStatNuiShapes()
                    #this_h.SetEffTool(self.EffToolConf)
                ##---Norm Variation Shapes---##
                for normsys in self.dict_NormSys:
                    if IsData:continue
                    ApplyThisNormSys=False
                    this_sample_keys=self.dict_NormSys[normsys]["sample_keys"]
                    for this_sample_key in this_sample_keys:                        
                        if this_sample_key in subp:
                            ApplyThisNormSys=True
                            break
                    if not ApplyThisNormSys : continue
                    
                    this_exceptions=self.dict_NormSys[normsys]["exception"]
                    if subp in this_exceptions:continue ## if this subp is in exception
                    this_nuisancename=self.dict_NormSys[normsys]["nuisanceName"]
                    this_scaleUp=self.dict_NormSys[normsys]["up"]
                    this_scaleDown=self.dict_NormSys[normsys]["down"]
                    #    def AddNormSys(self,sys,scaleUp,scaleDown):
                    this_h.AddNormSys(this_nuisancename,this_scaleUp,this_scaleDown)
                    #print "subp=",subp,"->Add Norm Sys->",this_nuisancename

                ##--Store JHProcHist of this subprocess--##
                this_container[subp]=this_h

                ##--Combined p = sum(subp)
                if isubp==0:
                    this_container[p].Clone(this_h)
                else:
                    this_container[p]=this_container[p].Combine(this_h,cut,x,p)
            ###--SetColor--##
            #_color=self.ProcConf[p]["color"]
            #print _color
            #this_container[p].SetLineColor(_color)
            #this_container[p].SetFillColor(_color)
        #if not IsData :
        #    this_h.MakeStatNuiShapes()



        return this_container
    def ReadNominalShape(self,cut,x,proc):
        _path=self.GetHistPath(cut,x,proc)
        _h=self.GetShapeFromFile(_path)
        if _h==False:
            if self.Verbose:
                print "<Fail to read Shape>"
                print _path
                #raise ValueError("No Histogram in the TFile->"+self.inputpath)
                print "return empty hist"
            return self._h_empty            
        return _h
    def ReadNuisanceShape(self,cut,x,proc,nui,idx1,idx2):
        _path=self.GetHistPath(cut,x,proc,nui,idx1,idx2)
        _h=self.GetShapeFromFile(_path)
        if _h==False:
            _hnom= deepcopy(self.ReadNominalShape(cut,x,proc))
            _hnom.SetName("__".join([cut,x,proc,nui,idx1,idx2]))
            return _hnom
        return _h

    def GetHistPath(self,cut,x,proc,sys=False,idx1=0,idx2=0):
        if not sys:## nominal
            _path=cut+"/"+x+"/"+proc
        else:
            _path="SYS/"+cut+"/"+x+"/"+sys+"/"+idx1+"/"+idx2+"/"+proc

        return _path
    def GetShapeFromFile(self,_path):
        _h = self.tfile.Get(_path)
        if not "TH" in str(type(_h)):
            if self.Verbose:
                print "NoShape->",_path
            return False
        return _h

    def CloseFile(self):
        self.tfile.Close()

def ReadCutAndX(AnaName,YEAR,suffix=""):
    YEAR=str(YEAR)
    _path=GetCutAndXConfPath(AnaName,YEAR,suffix)
    CutAndX=OpenDictFile(_path)
    return CutAndX
def GetCutAndXConfPath(AnaName,YEAR,suffix=""):
    return maindir+"/config/"+AnaName+"/"+YEAR+"/"+suffix+"/cut_and_x.py"

if __name__ == '__main__':
    import time
    start_time = time.time()

    ##---Following shows an example how to run
    AnaName="DiLeptonAnalyzer"
    Year=2017
    cut_and_x=ReadCutAndX(AnaName,Year)

    HistColl={}
    N=len(cut_and_x)
    idx_cut=0
    for cut in cut_and_x:
        idx_cut+=1
        print idx_cut,"/",N
        for x in cut_and_x[cut]:
            if not cut in HistColl : HistColl[cut]={}
            myreader=Reader(AnaName,Year)
            HistColl[cut][x]=myreader.MakeHistContainer(cut,x)
            myreader.CloseFile()
            
            for p in myreader.ProcConf:
                #print "-----"
                integral=HistColl[cut][x][p].GetHist().Integral()
                #print p

                _sum=0
                for subp in myreader.ProcConf[p]["procs"]:
                    #for p in  sorted(HistColl[cut][x]):
                    _sum+= HistColl[cut][x][subp].GetHist().Integral()
                #print "sum=",_sum
                if abs(1.-integral/_sum)>0.000001:
                    print p,"!!!!! "
                    print "integral=",integral
                    print "_sum=",_sum
            del myreader
    end_time= time.time()
    execution_time = end_time - start_time
    print "[runtime]", execution_time, "sec"
