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
    
    datacarddir="datacards"+dsuffix+"/TTsemiLepChargeScoreAccuracyMeasurement_splitcharge/"+Ana+"/"+suffix+"/"+xname
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
    procpath=GIT_HistoPlotterSys+"/config/ForDC/TTsemiLepChargeScoreAccuracyMeasurement_splitcharge/proc.py"
    if IsTestJob:
        procpath=GIT_HistoPlotterSys+"/config/ForDC/TTsemiLepChargeScoreAccuracyMeasurement_splitcharge/proc_test.py"
    nuinamepath=GIT_HistoPlotterSys+"/names/nuisance/v2410/map_nuisance_name.py"
    mydc.LoadNuisanceNameMap(nuinamepath)
    mydc.AddNormSysPath("config/NormSys/lnN_nuisance_XSEC.py")
    mydc.AddNormSysPath("config/NormSys/lnN_lumi"+YearCombine+".py")
    mydc.AddNormSysPath("config/NormSys/Only_bChargeID/lnN_bChargeID.py")
    
    mydc.Rebinning=Rebinning

    #mydc.RunWithSKFlatOutput(Year,Ana,"FinalCut","MeasuredCharge_Total",procpath,suffix)
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
    
    WORKDIR="WORKDIR/TTsemiLepChargeScoreAccuracyMeasurement_splitcharge/datacard"+statonly_suffix+scalepdf_precalc_suffix+pseudo_suffix+"/"+Ana+"/"+Year+"/"+suffix+"/"+cut+"/"+xname
    
        
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
    #config/ForDC/RunDatacard_TTsemiLepChargeScoreAccuracyMeasurement/RebinInfo/RunDatacard_TTsemiLepChargeScoreAccuracyMeasurement__2016postVFP__runSys__ApplyBtagSF__use_beff__.py
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    #config/ForDC/TTsemiLepChargeScoreAccuracyMeasurement/RebinInfo/TTsemiLepChargeScoreAccuracyMeasurement__2018__runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__
    path=GIT_HistoPlotterSys+"/config/ForDC/TTsemiLepChargeScoreAccuracyMeasurement_splitcharge/RebinInfo/TTsemiLepChargeScoreAccuracyMeasurement__"+year+"__"+suffix+".py"
    this_info=OpenDictFile(path)
    return this_info[cut][x]
if __name__ == '__main__':
    ##----Setup-----##
    Years=["2016preVFP","2016postVFP","2017","2018"]
    #Years=["2016preVFP","2017"]
    
    Ana="TTsemiLepChargeScoreAccuracyMeasurement"    
    suffix="runSys__use_beff_dasym__JETPUID_L__newlepveto__chi2kincut__bdt2608.2__splitcharge__jHOnly__jOthersOnly__"
    
        
    cutlist={
        "2016preVFP":[],
        "2016postVFP":[],
	"2017":[],
        "2018":[],

    }
    LeptonChs=["LeptonMinus_","LeptonPlus_"] ##2
    TDecayChs=["bJetHadronicSide","bJetLeptonicSide"] ##2
    
    bChargeTypes=[
        #"1muHOnly",
        #"1muLOnly",
        #"1eHOnly",
        #"1eLOnly",
        "NoSL_jH",
        "NoSL_jOthers",
    ]
    MOVERPTBINS = {

    "2016preVFP": {
        
        "1muHOnly": {
            "PT30To50":   [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 0.2, 1],
        },

        "1muLOnly": {
            "PT30To50":   [0, 0.15, 0.2, 1],
            "PT50To70":   [0, 0.15, 1],
            "PT70To100":  [0, 0.1, 0.15, 1],
            "PT100To140": [0, 0.1, 0.15, 1],
            "PT140ToInf": [0, 0.1, 1],
        },

        "1eHOnly": {
            "PT30To50":   [0, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },

        "1eLOnly": {
            "PT30To50":   [0, 0.15, 0.2, 1],
            "PT50To70":   [0, 0.15, 1],
            "PT70To100":  [0, 0.1, 0.15, 1],
            "PT100To140": [0, 0.1, 0.15, 1],
            "PT140ToInf": [0, 0.1, 1],
        },

        "NoSL_jH": {
            
        },

    },


    "2016postVFP": {

        "1muHOnly": {
            "PT30To50":   [0, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },

        "1muLOnly": {
            "PT30To50":   [0, 0.15, 1],
            "PT50To70":   [0, 0.15, 1],
            "PT70To100":  [0, 0.1, 0.15, 1],
            "PT100To140": [0, 0.1, 0.15, 1],
            "PT140ToInf": [0, 0.1, 1],
        },

        "1eHOnly": {
            "PT30To50":   [0, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },

        "1eLOnly": {
            "PT30To50":   [0, 0.15, 0.2, 1],
            "PT50To70":   [0, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },
        "NoSL_jH": {
          
        },

    },


    "2017": {

        "1muHOnly": {
            "PT30To50":   [0, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 0.2, 1],
        },

        "1muLOnly": {
            "PT30To50":   [0, 0.15, 0.2, 1],
            "PT50To70":   [0, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },

        "1eHOnly": {
            "PT30To50":   [0, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 0.2, 1],
        },

        "1eLOnly": {
            "PT30To50":   [0, 0.15, 0.2, 1],
            "PT50To70":   [0, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },
        "NoSL_jH": {

        },

    },


    "2018": {

        "1muHOnly": {
            "PT30To50":   [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 0.2, 1],
        },

        "1muLOnly": {
            "PT30To50":   [0, 0.15, 0.2, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },

        "1eHOnly": {
            "PT30To50":   [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 0.25, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 0.2, 1],
        },

        "1eLOnly": {
            "PT30To50":   [0, 0.15, 0.2, 1],
            "PT50To70":   [0, 0.1, 0.15, 0.2, 1],
            "PT70To100":  [0, 0.1, 0.15, 0.2, 1],
            "PT100To140": [0, 0.1, 0.15, 0.2, 1],
            "PT140ToInf": [0, 0.1, 0.15, 1],
        },
        "NoSL_jH": {

        },
        
    },
    }

    PTBINS=["PT30To50","PT50To70","PT70To100","PT100To140","PT140ToInf"]

    MeasuredCharges=[
        "MeasuredMinus",
        "MeasuredPlus"
    ]
    for YEAR in MOVERPTBINS:
            MOVERPTBINS[YEAR]["NoSL_jOthers"]=MOVERPTBINS[YEAR]["NoSL_jH"]
    
    for LeptonCh in LeptonChs:
        for TDecayCh in TDecayChs:
            for bChargeType in bChargeTypes:
                for PTBIN in PTBINS:
                    for Year in Years:
                        for MeasuredCharge in MeasuredCharges:
                            #THIS_MOVERPTBINS=MOVERPTBINS[Year][bChargeType][PTBIN]
                            #for i_MOVERPTBIN in range(len(THIS_MOVERPTBINS)-1):
                            #    #LeptonMinus_bJetHadronicSide_1muLOnly_MeasuredPlus__PT70To100__mOverPt_0p1_0p15
                            #    THIS_MOVERPTBIN="mOverPt_"+str(THIS_MOVERPTBINS[i_MOVERPTBIN])+"_"+str(THIS_MOVERPTBINS[i_MOVERPTBIN+1])
                            #    THIS_MOVERPTBIN=THIS_MOVERPTBIN.replace(".","p")
                            #    cutname=LeptonCh+TDecayCh+"_"+bChargeType+"_"+MeasuredCharge+"__"+PTBIN+"__"+THIS_MOVERPTBIN
                            #    cutlist[Year].append(cutname)
                            ##---Use unifrom one
                            for THIS_MOVERPTBIN in ['mOverPt_0_0p15',"mOverPt_0p15_1"]:
                                #LeptonMinus_bJetHadronicSide_1muLOnly_MeasuredPlus__PT70To100__mOverPt_0p1_0p15
                                #THIS_MOVERPTBIN="mOverPt_"+str(THIS_MOVERPTBINS[i_MOVERPTBIN])+"_"+str(THIS_MOVERPTBINS[i_MOVERPTBIN+1])
                                #THIS_MOVERPTBIN=THIS_MOVERPTBIN.replace(".","p")
                                #LeptonMinus_bJetHadronicSide_1muHOnly_MeasuredMinus__PT50To70__mOverPt_0p15_1
                                cutname=LeptonCh+TDecayCh+"_"+bChargeType+"_"+MeasuredCharge+"__"+PTBIN+"__"+THIS_MOVERPTBIN
                                cutlist[Year].append(cutname)                            


    ##---
    parser = argparse.ArgumentParser(description='RunDatacard_TTsemiLepChargeScoreAccuracyMeasurement_splitcharge.py')
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
            for cut in cutlist[Year]:
                print(cut)
                #Rebinning=GetRebinning(Year,cut,xname,suffix)
                #if "__FAIL" in cut :
                #    Rebinning=[Rebinning[0],Rebinning[-1]]
                RunWithCondor(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,pseudo)
    else:

        if runCondorSub:
            this_Year=args.this_Year
            this_cut=args.this_cut
            #if "LeptonicSide" in this_cut and "Tcand_mass" in xname:
            #    Rebinning=GetRebinningLeptonicSide()
            #if "HadronicSide" in this_cut and "Tcand_mass" in xname:
            #    Rebinning=GetRebinningHadronicSide()
            if "Tcand_mass" in xname: Rebinning=GetRebinning(this_Year,this_cut,xname,suffix)
            
            RunYear(Ana,this_Year,suffix,this_cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,args.testjob)
        else:
            for Year in Years:
                for cut in cutlist[Year]:
                    print(cut)
                    #if "LeptonicSide" in cut and "Tcand_mass" in xname:
                    #    Rebinning=GetRebinningLeptonicSide()
                    #if "HadronicSide" in cut and "Tcand_mass" in xname:
                    #    Rebinning=GetRebinningHadronicSide()
                    if "Tcand_mass" in xname: Rebinning=GetRebinning(Year,cut,xname,suffix)
                    

                    RunYear(Ana,Year,suffix,cut,xname,StatOnly,PreCalcScalePDF,DoSimple,Rebinning,pseudo,args.testjob)
        



