#!/usr/bin/env python3
##---
#NoEtabinning for SoftLeptonTagged 
from JHDatacard import JHDatacard
import sys
import os
from ExportShellCondorSetup_tamsa import Export
import argparse
from OpenDictFile import OpenDictFile




def RunYear(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,IsTestJob=False):
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
    
    datacarddir="datacards"+dsuffix+"/PreselectionToBDTRegionAnalyzer/"+Ana+"/"+suffix+"/"+xname
    print("datacarddir=",datacarddir)
    mydc=JHDatacard(Year,name,datacarddir,pseudo)    
    if StatOnly:
        mydc.StatOnly=1
    if PreCalcScalePDF:
        mydc.EnvelopRMSScalePDF=1
    if DoSimple:
        mydc.SimplifiedSys=1
        



    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    procpath=GIT_HistoPlotterSys+"/config/ForDC/PreselectionToBDTRegionAnalyzer/proc_bbbar_addxsuffix_dc.py"

    nuinamepath=GIT_HistoPlotterSys+"/names/nuisance/v2410/map_nuisance_name.py"
    mydc.LoadNuisanceNameMap(nuinamepath)
    mydc.AddNormSysPath("config/NormSys/lnN_nuisance_XSEC.py")
    mydc.AddNormSysPath("config/NormSys/lnN_lumi"+YearCombine+".py")
    mydc.Rebinning=Rebinning
    

    mydc.RunWithSKFlatOutput(Year,Ana,cut,xname,procpath,suffix)
    mydc.Export()

def RunWithCondor(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,pseudo):
    Year=str(Year)
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax=0):
    statonly_suffix=""
    scalepdf_precalc_suffix=""
    pseudo_suffix=""
    
    if StatOnly:
        statonly_suffix="__statonly"
    if PreCalcScalePDF:
        scalepdf_precalc_suffix="__precalcPDFScale"
    if DoSimple:
        scalepdf_precalc_suffix+="__doSimple"
    if pseudo:
        pseudo_suffix="__pseudo"
    
    WORKDIR="WORKDIR/PreselectionToBDTRegionAnalyzer/datacard"+statonly_suffix+scalepdf_precalc_suffix+pseudo_suffix+"/"+Ana+"/"+Year+"/"+suffix+"/"+cut+"/"+xname
    
        
    jobname="datacard__"+Ana+"__"+Year
    submit=1
    ncpu=1
    memory=False
    nretry=1
    #nmax=480
    nmax=False

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
    
        
    commandlist=[]
    commandlist.append("cd "+curdir)
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    this_scriptname=sys.argv[0].split("/")[-1]
    commandlist.append("python3 -u "+GIT_HistoPlotterSys+"/script/"+this_scriptname+" --condorsub --xname "+xname+" --year "+Year+" --cut "+cut+statonly_option+scalepdf_precalc_option+dosimple_option+pseudo_option)


    command="&&".join(commandlist)

    Export(WORKDIR,command,jobname,submit,ncpu,memory,nretry,nmax)


if __name__ == '__main__':
    ##----Setup-----##
    Years=["2016preVFP","2016postVFP","2017","2018"]
        
    Ana="PreselectionToBDTRegionAnalyzer"
    
    suffix="runSys__jetpuid_loose__lepveto__use_beffasym__bdt2512.5__bdtcut__apply_chargeid_eff_corr__apply_chargeid_acc_corr__addxsuffix__"
    
        
    cutlist=[
        "AllEvents__broad",
        "AllEvents__high_peak",
        "AllEvents__low_peak",
        "AllEvents__mid_peak",
    ]



    ##---
    parser = argparse.ArgumentParser(description='RunDatacard_PreselectionToBDTRegionAnalyzer.py')
    parser.add_argument('--condor', dest='runCondor', action="store_true", default=False)
    parser.add_argument('--condorsub', dest='runCondorSub', action="store_true", default=False)
    parser.add_argument('--statonly', dest='StatOnly', action="store_true", default=False)
    parser.add_argument('--pseudo', dest='pseudo', action="store_true", default=False)
    parser.add_argument('--precalcPDFScale', dest='PreCalcScalePDF', action="store_true", default=False)
    parser.add_argument('--dosimple', dest='DoSimple', action="store_true", default=False)

    parser.add_argument('--year', dest="this_Year",  default=False)
    parser.add_argument('--cut', dest="this_cut",  default=False)
    parser.add_argument('--xname', dest="xname",  default="measured_charge")


    parser.add_argument('--testjob', dest='testjob', action="store_true", default=False)
    


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
                RunWithCondor(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,pseudo)
    else:

        if runCondorSub:
            this_Year=args.this_Year
            this_cut=args.this_cut
            RunYear(Ana,this_Year,suffix,this_cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,args.testjob)
        else:
            for Year in Years:
                for cut in cutlist:
                    RunYear(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,args.testjob)
        



