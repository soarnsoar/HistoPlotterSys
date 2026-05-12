#!/usr/bin/env python3
from JHDatacard import JHDatacard
import sys
import os
from ExportShellCondorSetup_tamsa import Export
import argparse
from OpenDictFile import OpenDictFile




def RunYear(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,OneBinFailRegion,IsTestJob=False):
    print(Year,suffix)
    #Year="2018"
    Year=str(Year)
    YearCombine=Year.replace("preVFP","").replace("postVFP","")
    name="dc_"+cut+"_"+Year
    

    dsuffix=""

    if StatOnly:
        #datacarddir="datacards_StatOnly/"+Ana+"/"+suffix
        dsuffix+="_StatOnly"
    if PreCalcScalePDF:
        dsuffix+="_PreCalcScalePDF"
    if DoSimple:
        dsuffix+="_DoSimple"
    if pseudo:
        dsuffix+="_Pesudo"
    if OneBinFailRegion:
        dsuffix+="_OneBinFailRegion"
    datacarddir="datacards"+dsuffix+"/bTagChargeAsymFactor_BINNING/"+Ana+"/"+suffix+"/"+xname
    print("datacarddir=",datacarddir)
    mydc=JHDatacard(Year,name,datacarddir,pseudo)
    mydc.NuisanceSkip=['btag_ChargeAsymFactor']
    if StatOnly:
        mydc.StatOnly=1
    if PreCalcScalePDF:
        mydc.EnvelopRMSScalePDF=1
    if DoSimple:
        mydc.SimplifiedSys=1
        

    #    def RunWithSKFlatOutput(self,Year,AnalyzerName,cut,x,procpath,suffix):
    #/data6/Users/jhchoi/plotter/HistoPlotterSys/test/test_procconfig/TTsemiEff_test

    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    procpath=GIT_HistoPlotterSys+"/config/ForDC/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING/proc.py"
    if IsTestJob:
        procpath=GIT_HistoPlotterSys+"/config/ForDC/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING/proc_test.py"
    nuinamepath=GIT_HistoPlotterSys+"/names/nuisance/v2410/map_nuisance_name.py"
    mydc.LoadNuisanceNameMap(nuinamepath)
    mydc.AddNormSysPath("config/NormSys/lnN_nuisance_XSEC.py")
    mydc.AddNormSysPath("config/NormSys/lnN_lumi"+YearCombine+".py")
    
    mydc.Rebinning=Rebinning

    #mydc.RunWithSKFlatOutput(Year,Ana,"FinalCut","MeasuredCharge_Total",procpath,suffix)
    mydc.RunWithSKFlatOutput(Year,Ana,cut,xname,procpath,suffix)
    mydc.Export()

def RunWithCondor(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,pseudo,OneBinFailRegion):
    Year=str(Year)
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax=0):
    statonly_suffix=""
    scalepdf_precalc_suffix=""
    pseudo_suffix=""
    OneBinFailRegion_suffix=""
    if StatOnly:
        statonly_suffix="__statonly"
    if PreCalcScalePDF:
        scalepdf_precalc_suffix="__precalcPDFScale"
    if DoSimple:
        scalepdf_precalc_suffix+="__doSimple"
    if pseudo:
        pseudo_suffix="__pseudo"
    if OneBinFailRegion:
        OneBinFailRegion_suffix="__OneBinFailRegion"
    WORKDIR="WORKDIR/bTagChargeAsym_BINNING/datacard"+statonly_suffix+scalepdf_precalc_suffix+pseudo_suffix+OneBinFailRegion_suffix+"/"+Ana+"/"+Year+"/"+suffix+"/"+cut+"/"+xname
    
        
    jobname="datacard__"+Ana+"__"+Year
    submit=1
    ncpu=1
    memory=False
    nretry=1
    nmax=480

    curdir=os.getcwd()

    statonly_option=""
    if StatOnly:
        statonly_option=" --statonly"
    scalepdf_precalc_option=""
    if PreCalcScalePDF:
        scalepdf_precalc_option=" --precalcPDFScale"
    dosimple_option=""
    if DoSimple:
        dosimple_option=" --dosimple "
    pseudo_option=""
    if pseudo:
        pseudo_option=" --pseudo "
    OneBinFailRegion_option=""
    if OneBinFailRegion:
        OneBinFailRegion_option=" --OneBinFailRegion "
        
    commandlist=[]
    commandlist.append("cd "+curdir)
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    this_scriptname=sys.argv[0].split("/")[-1]
    commandlist.append("python3 -u "+GIT_HistoPlotterSys+"/script/"+this_scriptname+" --condorsub --xname "+xname+" --year "+Year+" --cut "+cut+statonly_option+scalepdf_precalc_option+dosimple_option+pseudo_option+OneBinFailRegion_option)


    command="&&".join(commandlist)

    Export(WORKDIR,command,jobname,submit,ncpu,memory,nretry,nmax)


def GetRebinningHadronicSide():
    this_rebinning=[]
    #this_N=70
    this_N=55 ##update 250725
    #xmin=100.
    xmin=130. ## update 250725
    xmax=240.

    dx=(xmax-xmin)/this_N

    for i in range(this_N+1):
        this_x=xmin+float(i)*dx
        this_rebinning.append(this_x)
    return this_rebinning

def GetRebinningLeptonicSide():
    this_rebinning=[]
    this_N=45
    xmin=150.
    xmax=240.

    dx=(xmax-xmin)/this_N

    for i in range(this_N+1):
        this_x=xmin+float(i)*dx
        this_rebinning.append(this_x)
    return this_rebinning

def GetRebinning(year,cut,x,suffix):
    #config/ForDC/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING/RebinInfo/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING__2016postVFP__runSys__ApplyBtagSF__use_beff__.py
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")

    path=GIT_HistoPlotterSys+"/config/ForDC/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING/RebinInfo/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING__"+year+"__"+suffix+".py"
    this_info=OpenDictFile(path)
    return this_info[cut][x]
if __name__ == '__main__':
    ##----Setup-----##
    Years=["2016preVFP","2016postVFP","2017","2018"]
        
    Ana="TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING"
    #suffix="runSys__TopMassWindow__"
    suffix="runSys__ApplyBtagSF__use_beff__JETPUID_L__chi2kincut__"
    
        
    cutlist=[]
    LeptonChs=["LeptonMinus_","LeptonPlus_"] ##2
    TDecayChs=["bJetHadronicSide","bJetLeptonicSide"] ##2
    ProbePassFails=["__PASS","__FAIL"]
    PTBINS=["PT30To50","PT50To70","PT70To100","PT100To140","PT140ToInf"]
    ETABINS=["Eta0To0p8","Eta0p8To1p6","Eta1p6To2","Eta2To2p5"] #

    
    for LeptonCh in LeptonChs:
        for TDecayCh in TDecayChs:
            for PASSFAIL in ProbePassFails:
                for PTBIN in PTBINS:
                    for ETABIN in ETABINS:
                        cutname=LeptonCh+TDecayCh+PASSFAIL+"__"+PTBIN+"__"+ETABIN
                        cutlist.append(cutname)


    ##---
    parser = argparse.ArgumentParser(description='RunDatacard_bTagChargeAsymFactor.py')
    parser.add_argument('--condor', dest='runCondor', action="store_true", default=False)
    parser.add_argument('--condorsub', dest='runCondorSub', action="store_true", default=False)
    parser.add_argument('--statonly', dest='StatOnly', action="store_true", default=False)
    parser.add_argument('--pseudo', dest='pseudo', action="store_true", default=False)
    parser.add_argument('--precalcPDFScale', dest='PreCalcScalePDF', action="store_true", default=False)
    parser.add_argument('--dosimple', dest='DoSimple', action="store_true", default=False)

    parser.add_argument('--year', dest="this_Year",  default=False)
    parser.add_argument('--cut', dest="this_cut",  default=False)
    parser.add_argument('--xname', dest="xname",  default="Tcand_mass")


    parser.add_argument('--testjob', dest='testjob', action="store_true", default=False)
    
    parser.add_argument('--OneBinFailRegion', dest='OneBinFailRegion', action="store_true", default=False)

    args = parser.parse_args()
    xname=args.xname
    #xname="Tcand_mass"

    ##----Run-------##

    runCondor=args.runCondor
    runCondorSub=args.runCondorSub
    StatOnly=args.StatOnly
    PreCalcScalePDF=args.PreCalcScalePDF
    DoSimple=args.DoSimple
    pseudo=args.pseudo
    if DoSimple:
        PreCalcScalePDF=1
    ##--THad ->[100,350]
    ##--tLep ->[150,250]

    
    Rebinning=[]

    
    
    ##---Print Run Mode
    if runCondor:
        print("[submit condorjob]")
    elif runCondorSub:
        print("[run condor subjob]")
    else:
        print("[run in standalone]")

    if runCondor:
        for Year in Years:
            for cut in cutlist:
                print(cut)
                #Rebinning=GetRebinning(Year,cut,xname,suffix)
                #if "__FAIL" in cut :
                #    Rebinning=[Rebinning[0],Rebinning[-1]]
                RunWithCondor(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,pseudo,args.OneBinFailRegion)       
    else:

        if runCondorSub:
            this_Year=args.this_Year
            this_cut=args.this_cut
            #if "LeptonicSide" in this_cut and "Tcand_mass" in xname:
            #    Rebinning=GetRebinningLeptonicSide()
            #if "HadronicSide" in this_cut and "Tcand_mass" in xname:
            #    Rebinning=GetRebinningHadronicSide()
            Rebinning=GetRebinning(this_Year,this_cut,xname,suffix)
            if args.OneBinFailRegion:
                if "__FAIL" in this_cut :
                    Rebinning=[Rebinning[0],Rebinning[-1]]
                    print("Use SingleBinning For Fail Region!")
            RunYear(Ana,this_Year,suffix,this_cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,args.OneBinFailRegion,args.testjob)
        else:
            for Year in Years:
                for cut in cutlist:
                    print(cut)
                    #if "LeptonicSide" in cut and "Tcand_mass" in xname:
                    #    Rebinning=GetRebinningLeptonicSide()
                    #if "HadronicSide" in cut and "Tcand_mass" in xname:
                    #    Rebinning=GetRebinningHadronicSide()
                    Rebinning=GetRebinning(Year,cut,xname,suffix)
                    if args.OneBinFailRegion:
                        if "__FAIL" in cut :
                            Rebinning=[Rebinning[0],Rebinning[-1]]
                            print("Use SingleBinning For Fail Region!")

                    RunYear(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,args.OneBinFailRegion,args.testjob)
        



