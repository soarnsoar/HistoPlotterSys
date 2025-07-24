#!/usr/bin/env python3
from JHDatacard__bplusminus_5percent import JHDatacard
import sys
import os
from ExportShellCondorSetup_tamsa import Export
import argparse
from collections import OrderedDict
from OpenDictFile import OpenDictFile



def RunYear(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,ScaleToPlusPass,ScaleToMinusPass):
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
        
    dsuffix+="_bPlusMinus5percent"
    datacarddir="datacards"+dsuffix+"/bTagChargeAsymFactor/"+Ana+"/"+suffix+"/"+xname
    print("datacarddir=",datacarddir)
    mydc=JHDatacard(Year,name,datacarddir,1)
    mydc.bplusPassScale=ScaleToPlusPass
    mydc.bminusPassScale=ScaleToMinusPass
    if StatOnly:
        mydc.StatOnly=1
    if PreCalcScalePDF:
        mydc.EnvelopRMSScalePDF=1
    if DoSimple:
        mydc.SimplifiedSys=1
        

    #    def RunWithSKFlatOutput(self,Year,AnalyzerName,cut,x,procpath,suffix):
    #/data6/Users/jhchoi/plotter/HistoPlotterSys/test/test_procconfig/TTsemiEff_test

    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    procpath=GIT_HistoPlotterSys+"/config/ForDC/TTsemiLepBtagChargeAsymEfficiencyMeasurement/proc.py"
    nuinamepath=GIT_HistoPlotterSys+"/names/nuisance/v2410/map_nuisance_name.py"
    mydc.LoadNuisanceNameMap(nuinamepath)
    mydc.AddNormSysPath("config/NormSys/lnN_nuisance_XSEC.py")
    mydc.AddNormSysPath("config/NormSys/lnN_lumi"+YearCombine+".py")
    
    mydc.Rebinning=Rebinning

    #mydc.RunWithSKFlatOutput(Year,Ana,"FinalCut","MeasuredCharge_Total",procpath,suffix)
    mydc.RunWithSKFlatOutput(Year,Ana,cut,xname,procpath,suffix)
    mydc.Export()

def RunWithCondor(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,ScaleToPlusPass,ScaleToMinusPass):
    Year=str(Year)
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax=0):
    statonly_suffix=""
    scalepdf_precalc_suffix=""
    pseudo_suffix="__bPlusMinus5percent"
    if StatOnly:
        statonly_suffix="__statonly"
    if PreCalcScalePDF:
        scalepdf_precalc_suffix="__precalcPDFScale"
    if DoSimple:
        scalepdf_precalc_suffix+="__doSimple"

    WORKDIR="WORKDIR/bTagChargeAsym/datacard"+statonly_suffix+scalepdf_precalc_suffix+pseudo_suffix+"/"+Ana+"/"+Year+"/"+suffix+"/"+cut+"/"+xname
    
        
    jobname="datacard__"+Ana+"__"+Year
    submit=1
    ncpu=1
    memory=False
    nretry=1
    nmax=960

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
    
    #pseudo_option=" --ScaleToPlusPass "+str(ScaleToPlusPass)+" "
    pseudo_option=""
        
    commandlist=[]
    commandlist.append("cd "+curdir)
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    this_scriptname=sys.argv[0].split("/")[-1]
    commandlist.append("python3 -u "+GIT_HistoPlotterSys+"/script/"+this_scriptname+" --condorsub --xname "+xname+" --year "+Year+" --cut "+cut+statonly_option+scalepdf_precalc_option+dosimple_option+pseudo_option)


    command="&&".join(commandlist)

    Export(WORKDIR,command,jobname,submit,ncpu,memory,nretry,nmax)


def GetRebinningHadronicSide():
    this_rebinning=[]
    this_N=70
    xmin=100.
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


def GetScaleToPlusPass(year):
    maindir=os.getenv("GIT_HistoPlotterSys")
    infopath=maindir+"/config/ForDC/TTsemiLepBtagChargeAsymEfficiencyMeasurement/YieldInfo/RunDatacard_bTagChargeAsymFactor__NoTopMassWindow_bplusminus_5percent/"+str(year)+".py"
    #OpenDictFile
    this_info=OpenDictFile(infopath)
    bplus_pass=this_info['N_bplus_PASS']
    bplus_fail=this_info['N_bplus_FAIL']
    p=bplus_pass
    f=bplus_fail
    r=f/p

    #r'=r/1.05 - 5/105
    rr=r/1.05-5./105.
    #p'=f/r' = f/(r/1.05 -5/105)
    pp=f/rr

    this_scale=pp/p
    print(year,"] Scale bplus to",this_scale)
    return this_scale

def GetScaleToMinusPass(year):
    maindir=os.getenv("GIT_HistoPlotterSys")
    infopath=maindir+"/config/ForDC/TTsemiLepBtagChargeAsymEfficiencyMeasurement/YieldInfo/RunDatacard_bTagChargeAsymFactor__NoTopMassWindow_bplusminus_5percent/"+str(year)+".py"
    #OpenDictFile
    this_info=OpenDictFile(infopath)
    bminus_pass=this_info['N_bminus_PASS']
    bminus_fail=this_info['N_bminus_FAIL']
    p=bminus_pass
    f=bminus_fail
    r=f/p

    #r'=r/0.95 + 5/95
    rr=r/0.95 + 5./95.
    #p'=f/r' = f/(r/0.95 +5/95)
    pp=f/rr

    this_scale=pp/p
    print(year,"] Scale bminus to",this_scale)
    return this_scale

if __name__ == '__main__':
    ##----Setup-----##
    Years=["2016preVFP","2016postVFP","2017","2018"]
        
    Ana="TTsemiLepBtagChargeAsymEfficiencyMeasurement"
    #suffix="runSys__TopMassWindow__"
    suffix="runSys__ApplyBtagSF__"
    
        
    cutlist=[]
    LeptonChs=["LeptonMinus_","LeptonPlus_"] ##2
    TDecayChs=["bJetHadronicSide","bJetLeptonicSide"] ##2
    ProbePassFails=["__PASS","__FAIL"]



    
    for LeptonCh in LeptonChs:
        for TDecayCh in TDecayChs:
            for PASSFAIL in ProbePassFails:
                cutname=LeptonCh+TDecayCh+PASSFAIL
                cutlist.append(cutname)


    ##---
    parser = argparse.ArgumentParser(description='RunDatacard_bTagChargeAsymFactor.py')
    parser.add_argument('--condor', dest='runCondor', action="store_true", default=False)
    parser.add_argument('--condorsub', dest='runCondorSub', action="store_true", default=False)
    parser.add_argument('--statonly', dest='StatOnly', action="store_true", default=False)
    #parser.add_argument('--ScaleToPlusPass', dest='ScaleToPlusPass', default=1.)
    parser.add_argument('--precalcPDFScale', dest='PreCalcScalePDF', action="store_true", default=False)
    parser.add_argument('--dosimple', dest='DoSimple', action="store_true", default=False)

    parser.add_argument('--year', dest="this_Year",  default=False)
    parser.add_argument('--cut', dest="this_cut",  default=False)
    parser.add_argument('--xname', dest="xname",  default="Tcand_mass")



    args = parser.parse_args()
    xname=args.xname
    #xname="Tcand_mass"

    ##----Run-------##

    runCondor=args.runCondor
    runCondorSub=args.runCondorSub
    StatOnly=args.StatOnly
    PreCalcScalePDF=args.PreCalcScalePDF
    DoSimple=args.DoSimple

    #ScaleToPlusPass=float(args.ScaleToPlusPass)
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
            ScaleToPlusPass=GetScaleToPlusPass(Year)
            ScaleToMinusPass=GetScaleToMinusPass(Year)
            for cut in cutlist:
                print(cut)
                RunWithCondor(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,ScaleToPlusPass,ScaleToMinusPass)       
    else:

        if runCondorSub:
            this_Year=args.this_Year
            this_cut=args.this_cut
            if "LeptonicSide" in this_cut and "Tcand_mass" in xname:
                Rebinning=GetRebinningLeptonicSide()
            if "HadronicSide" in this_cut and "Tcand_mass" in xname:
                Rebinning=GetRebinningHadronicSide()
            ScaleToPlusPass=GetScaleToPlusPass(this_Year)
            ScaleToMinusPass=GetScaleToMinusPass(this_Year)
            RunYear(Ana,this_Year,suffix,this_cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,ScaleToPlusPass,ScaleToMinusPass)
        else:
            for Year in Years:
                ScaleToPlusPass=GetScaleToPlusPass(Year)
                ScaleToMinusPass=GetScaleToMinusPass(Year)
                for cut in cutlist:
                    print(cut)
                    if "LeptonicSide" in cut and "Tcand_mass" in xname:
                        Rebinning=GetRebinningLeptonicSide()
                    if "HadronicSide" in cut and "Tcand_mass" in xname:
                        Rebinning=GetRebinningHadronicSide()
                    RunYear(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,ScaleToPlusPass,ScaleToMinusPass)
        



