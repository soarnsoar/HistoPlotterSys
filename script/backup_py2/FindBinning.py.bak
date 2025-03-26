#!/usr/bin/env python
import ROOT
from collections import OrderedDict
import os
from ParseSKFlatOutput import Parser
from math import sqrt
maindir=os.getenv("GIT_HistoPlotterSys")
##Use only "data"
class FindBinning:
    def __init__(self,AnalyzerName,Year,suffix):
        self.AnalyzerName=AnalyzerName
        self.Year=str(Year)
        self.suffix=suffix
        self.SetInputPath()
        self.ReadInput()
        self.proc="Data"

        ##----read cut and x---##
        self.myparser=Parser(self.AnalyzerName,Year,suffix)
        self.myparser.Parse()
        self.cut_and_x=self.myparser.cut_x
        #self.ParseInitPtBinning()

    def SetProc(self,proc):
        self.proc=proc
    def Setbname(self,bname):
        self.bname=bname

    def SetInputPath(self):
        self.inputpath=maindir+"/SKFlatOutput/"+self.AnalyzerName+"/"+self.Year+"/"+self.suffix+"/combine.root"
    def ReadInput(self):
        self.tfile=ROOT.TFile.Open(self.inputpath)
    def SetDeno(self,deno_cuts):
        self.deno_cuts=deno_cuts
    def SetNume(self,nume_cuts):
        self.nume_cuts=nume_cuts
    def SetPtRange(self,ptmin,ptmax):
        if not ptmin in self.init_ptbin:
            print "ptmin=",ptmin,"is not in init pt bins",self.init_ptbin
            1/0
        if not ptmax in self.init_ptbin:
            print "ptmax=",ptmax,"is not in init pt bins",self.init_ptbin
            1/0
        self.ptmin=ptmin
        self.ptmax=ptmax
        ##bLep_eta__pt130140
    def SetEtaRange(self,etamin,etamax):
        d=(etamax-etamin)/1000000000000.
        self.etamin=etamin+d
        self.etamax=etamax+d
    def GetNdata(self):
        
        self.SelectPtBins()
        y_deno=self.GetYieldDeno()
        y_nume=self.GetYieldNume()


        total_relerr=sqrt(1/(y_deno-y_nume) + 1/y_nume)
        #total_relerr=0
        print "y_deno=",y_deno
        print "y_nume=",y_nume
        return y_deno,y_nume,total_relerr
    def GetYieldDeno(self):
        ret=0
        for path in self.list_denohistpath:
            #print path
            h=self.tfile.Get(path)
            ret+=self.GetYield_EtaRange(h,self.etamin,self.etamax)
        return ret
    def GetYieldNume(self):
        ret=0
        for path in self.list_numehistpath:
            #print path
            h=self.tfile.Get(path)
            ret+=self.GetYield_EtaRange(h,self.etamin,self.etamax)
        return ret
    def GetYield_EtaRange(self,_h,etamin,etamax):
        i_etamin=_h.FindBin(etamin)
        i_etamax=_h.FindBin(etamax)
        print "Integral eta from",_h.GetBinLowEdge(i_etamin),"To",_h.GetBinLowEdge(i_etamax)
        return _h.Integral(i_etamin,i_etamax)
    def SelectPtBins(self):
        #self.ParseInitPtBinning()
        #bLep_eta__pt5060
        self.selected_ptbins=[]
        for x in self.init_ptbin:
            if x>=self.ptmin and x<=self.ptmax:
                self.selected_ptbins.append(x)
        self.selected_ptbins=sorted(list(set(self.selected_ptbins)))
        print "self.selected_ptbins=",self.selected_ptbins
        self.xnames=[]
        for i in range(len(self.selected_ptbins)-1):
            ##30,40,50,60....
            pt1=self.selected_ptbins[i]
            pt2=self.selected_ptbins[i+1]
            print "integral from ",pt1,"to",pt2
            xname=self.bname+"_eta__pt"+str(pt1)+"_"+str(pt2)
            self.xnames.append(xname)
    def SetHistPaths(self):
        self.list_denohistpath=[]
        self.list_numehistpath=[]
        for xname in self.xnames:
            for cut in self.deno_cuts:
                this_path=cut+"/"+xname+"/Data"
                self.list_denohistpath.append(this_path)
            for cut in self.nume_cuts:
                this_path=cut+"/"+xname+"/Data"
                self.list_numehistpath.append(this_path)
                
    def ParseInitPtBinning(self):
        xnames=[]
        for deno_cut in self.deno_cuts:
            xnames+=sorted(self.cut_and_x[deno_cut])
        ##xnames=["bLep_eta__pt60_70","bLep_eta__pt50_60",...]
        self.init_ptbin=[]
        for x in xnames:
            pts=x.split("eta__pt")[-1] ## 60_70 OR 50_60 OR 300400
            
            ptmin=int(pts.split("_")[0])
            ptmax=int(pts.split("_")[1])
            self.init_ptbin.append(ptmin)
            self.init_ptbin.append(ptmax)
        self.init_ptbin=sorted(list(set(self.init_ptbin)))
        print "---inti ptbin---"
        print self.init_ptbin

    def __del__(self):
        self.tfile.Close()
def ChargreScoreCutEfficiency():
    Ana="TTsemiLepChargeScoreEfficiencyMeasurement"
    year="2016postVFP"
    bnames=["bLep","bHad"]
    suffix="noveto__FlavourMatchBase__HcbCR__ForBinning__"


    ##----def of efficiency---##
    dict_def=OrderedDict()
    for bname in bnames:
        dict_def[bname]=OrderedDict()
        dict_def[bname]["bmuon_high"]={
            "deno":["AllLep_TTLJ__"+bname+"UsingSoftMuonChargeNotOpposite","AllLep_TTLJ__"+bname+"UsingSoftMuonChargeUseOpposite","AllLep_TTLJ__"+bname+"_FailSoftMuon"],
            "nume":["AllLep_TTLJ__"+bname+"UsingSoftMuonChargeNotOpposite"],
        }
        dict_def[bname]["bmuon_low"]={
            "deno":["AllLep_TTLJ__"+bname+"UsingSoftMuonChargeUseOpposite","AllLep_TTLJ__"+bname+"_FailSoftMuon"],
            "nume":["AllLep_TTLJ__"+bname+"UsingSoftMuonChargeUseOpposite"],
        }
    

    
    ptmin=30
    ptmax=70
    etamin=-2.6
    etamax=-2.0


    for bname in bnames:
        print "--",bname,"--"
        thisjob=FindBinning(Ana,year,suffix)
        thisjob.Setbname(bname)
        thisjob.SetDeno(dict_def[bname]["bmuon_high"]["deno"])
        thisjob.SetNume(dict_def[bname]["bmuon_high"]["nume"])
        #thisjob.SetDeno(["AllLep_TTLJ__bLep_FailSoftMuon","AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite","AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"])
        #thisjob.SetNume(["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"])
        thisjob.ParseInitPtBinning()
        print thisjob.init_ptbin
        thisjob.SetPtRange(ptmin,ptmax)
        thisjob.SetEtaRange(etamin,etamax)
        thisjob.SelectPtBins()
        thisjob.SetHistPaths()
        y_deno,y_nume,total_relerr=thisjob.GetNdata()
        print "total_relerr=",total_relerr
        
if __name__ == '__main__':

    ChargreScoreCutEfficiency()
