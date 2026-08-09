import re
import os
from datetime import datetime


import sys

def GetLogPath(year,lepton,bdecay,ptbin,etabin,jtype):
    #WORKDIR/TTsemiLepChargeScoreEfficiencyMeasurement_splitcharge_noetabin_HighJetOnly/datacard/TTsemiLepChargeScoreEfficiencyMeasurement/2018/runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__noetabin__HighJetOnly__/LeptonPlus_bJetHadronicSide_NoSL_jOthers__PT140ToInf__Eta2To2p5/Tcand_mass/run.log
    ret="WORKDIR/TTsemiLepChargeScoreEfficiencyMeasurement_splitcharge_noetabin_HighJetOnly/datacard/TTsemiLepChargeScoreEfficiencyMeasurement/"+year+"/runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__noetabin__HighJetOnly__/"

    dirname=lepton+"_"+bdecay+"_NoSL_"+jtype+"__"+ptbin+"__"+etabin
    ret+=dirname
    ret+="/Tcand_mass/run.log"
    return ret


def GetCardPath(year,lepton,bdecay,ptbin,etabin,jtype):
    #datacards/TTsemiLepChargeScoreEfficiencyMeasurement_splitcharge_noetabin_HighJetOnly/TTsemiLepChargeScoreEfficiencyMeasurement/runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__noetabin__HighJetOnly__/Tcand_mass/dc_LeptonMinus_bJetHadronicSide_NoSL_jH__PT50To70__Eta2To2p5_2018.txt
    ret="datacards/TTsemiLepChargeScoreEfficiencyMeasurement_splitcharge_noetabin_HighJetOnly/TTsemiLepChargeScoreEfficiencyMeasurement/runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__noetabin__HighJetOnly__/Tcand_mass/dc_"+lepton+"_"+bdecay+"_NoSL_"+jtype+"__"+ptbin+"__"+etabin+"_"+year+".txt"
    return ret


def GetShapePath(year,lepton,bdecay,ptbin,etabin,jtype):
    ret="datacards/TTsemiLepChargeScoreEfficiencyMeasurement_splitcharge_noetabin_HighJetOnly/TTsemiLepChargeScoreEfficiencyMeasurement/runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__noetabin__HighJetOnly__/Tcand_mass/shapes/dc_"+lepton+"_"+bdecay+"_NoSL_"+jtype+"__"+ptbin+"__"+etabin+"_"+year+".root"
    return ret

def GetModifiedTime(_path):
    stat = os.stat(_path)
    t = datetime.fromtimestamp(stat.st_mtime)
    ret=t.strftime("%Y-%m-%d %H:%M:%S")

    return ret

def is_within_5sec(t1, t2):
    fmt = "%Y-%m-%d %H:%M:%S"
    d1 = datetime.strptime(t1, fmt)
    d2 = datetime.strptime(t2, fmt)

    return abs((d1 - d2).total_seconds()) <= 5



year=sys.argv[1]
lepton=sys.argv[2]
bdecay=sys.argv[3]
ptbin=sys.argv[4]
etabin=sys.argv[5]
jtype=sys.argv[6]
#logpath=sys.argv[1]

logpath=GetLogPath(year,lepton,bdecay,ptbin,etabin,jtype)
cardpath=GetCardPath(year,lepton,bdecay,ptbin,etabin,jtype)
shapepath=GetShapePath(year,lepton,bdecay,ptbin,etabin,jtype)

condor_time = None
with open(logpath) as f:
    for line in f:
        m = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) Job terminated\.', line)
        if m:
            condor_time = m.group(1)

card_time=GetModifiedTime(GetCardPath(year,lepton,bdecay,ptbin,etabin,jtype))
shape_time=GetModifiedTime(GetShapePath(year,lepton,bdecay,ptbin,etabin,jtype))

dt_card_shape=is_within_5sec(card_time,shape_time)
dt_condor_card=is_within_5sec(condor_time,card_time)
dt_shape_condor=is_within_5sec(shape_time,condor_time)

if not (dt_card_shape and dt_condor_card and dt_shape_condor):
    print ("-----")
    print(cardpath)
    print(logpath)

    print(condor_time)
    print(card_time)
    print(shape_time)




