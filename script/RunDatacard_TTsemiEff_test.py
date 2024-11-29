#!/usr/bin/env python
from JHDatacard import JHDatacard
import sys
import os
from ExportShellCondorSetup_tamsa import Export
def RunYear(Ana,Year,suffix,cut,xname):
    print Year,suffix
    #Year="2018"
    Year=str(Year)
    YearCombine=Year.replace("preVFP","").replace("postVFP","")
    name="dc_"+cut+"_"+Year
    mydc=JHDatacard(Year,name,"datacards/"+Ana+"/"+suffix,1)
    #    def RunWithSKFlatOutput(self,Year,AnalyzerName,cut,x,procpath,suffix):
    #/data6/Users/jhchoi/plotter/HistoPlotterSys/test/test_procconfig/TTsemiEff_test

    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    procpath=GIT_HistoPlotterSys+"/test/test_procconfig/TTsemiEff_test/proc.py"
    nuinamepath=GIT_HistoPlotterSys+"/names/nuisance/v2410/map_nuisance_name.py"
    mydc.LoadNuisanceNameMap(nuinamepath)
    mydc.AddNormSysPath("config/NormSys/lnN_nuisance_XSEC.py")
    mydc.AddNormSysPath("config/NormSys/lnN_lumi"+YearCombine+".py")
    
    #mydc.RunWithSKFlatOutput(Year,Ana,"FinalCut","MeasuredCharge_Total",procpath,suffix)
    mydc.RunWithSKFlatOutput(Year,Ana,cut,xname,procpath,suffix)
    mydc.Export()

def RunWithCondor(Ana,Year,suffix,cut,xname):
    Year=str(Year)
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax=0):
    WORKDIR="WORKDIR/datacard/"+Ana+"/"+Year+"/"+suffix+"/"+cut+"/"+xname
    jobname="datacard__"+Ana+"__"+Year
    submit=1
    ncpu=1
    memory=False
    nretry=3
    nmax=999

    curdir=os.getcwd()
    commandlist=[]
    commandlist.append("cd "+curdir)
    commandlist.append("RunDatacard_TTsemiEff_test.py 2 "+Year+" "+cut)
    command="&&".join(commandlist)

    Export(WORKDIR,command,jobname,submit,ncpu,memory,nretry,nmax)

if __name__ == '__main__':
    ##----Setup-----##
    Years=["2017"]
        
    Ana="TTsemiLepChargeScoreEfficiencyMeasurement_TightMatch"
    suffix="runSys__use_beff__ForMeasure__"
    xname="Tcand_mass"
        
    cutlist=[]
    LeptonChs=["LeptonMinus_","LeptonPlus_"] ##2
    TDecayChs=["bJetHadronicSide","bJetLeptonicSide"] ##2
    ChargeObjs=["TestMuon_HasSLTMuonHigh","TestMuon_HasSLTMuonLow","TestElectron_HasSLTElectronHigh","TestElectron_HasSLTElectronLow","TestJet_GoodBJet","TestJet_BadBJet"]##6
    PtBins=["__30To50","__PT50To70","__PT70To100","__PT100To140","__PT140ToInf"]##Need To Fix later -> 30to50 ##5
    
    for LeptonCh in LeptonChs:
        for TDecayCh in TDecayChs:
            for ChargeObj in ChargeObjs:
                for PtBin in PtBins:
                    cutname=LeptonCh+TDecayCh+ChargeObj+PtBin
                    cutlist.append(cutname)
    ##----Run-------##

    runCondor=False
    runCondorSub=False

    if len(sys.argv) >1 :
        if int(sys.argv[1])==2:
            runCondorSub=True
        if int(sys.argv[1])==1:
            runCondor=True


    ##---Print Run Mode
    if runCondor:
        print "[submit condorjob]"
    elif runCondorSub:
        print "[run condor subjob]"
    else:
        print "[run in standalone]"

    if runCondor:
        for Year in Years:
            for cut in cutlist:
                print cut
                RunWithCondor(Ana,Year,suffix,cut,xname)       
    else:

        if runCondorSub:
            this_Year=sys.argv[2]
            this_cut=sys.argv[3]
            
            RunYear(Ana,this_Year,suffix,this_cut,xname)
        else:
            for Year in Years:
                for cut in cutlist:
                    print cut
                    RunYear(Ana,Year,suffix,cut,xname)
        



