import ROOT
mainproc="SingleTop_tW_antitop_NoFullyHad"
fpath="SKFlatOutput/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING/2017/runSys__ApplyBtagSF__/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING_"+mainproc+".root"
tfile=ROOT.TFile(fpath)

procs=[
    mainproc+"_FromOthers__HadronOthers",
    mainproc+"_Frombminus__HadronB",
    mainproc+"_Frombplus__HadronB",
    mainproc+"_Frombminus__HadronOthers",
    mainproc+"_Frombplus__HadronOthers",
    mainproc+"_FromOthers__HadronB",

]
cut="LeptonMinus_bJetHadronicSide__PASS__PT30To50__Eta1p6To2"

sum_nom=0
sum_00=0
sum_10=0
for proc in procs:
    try:
        this_hnom=tfile.Get(cut+"/Tcand_mass/"+proc)
        this_Nnom=this_hnom.GetEntries()
        sum_nom+=this_Nnom
    except:
        continue
for proc in procs:
    try:
        this_h00=tfile.Get("SYS/"+cut+"/Tcand_mass/muonscale2017/0/0/"+proc)
        this_N00=this_h00.GetEntries()
        sum_00+=this_N00
    except:
        continue
for proc in procs:
    try:
        this_h10=tfile.Get("SYS/"+cut+"/Tcand_mass/muonscale2017/1/0/"+proc)
        this_N10=this_h10.GetEntries()
        sum_10+=this_N10
    except:
        continue

print("sum_nom=",sum_nom)
print("sum_00=",sum_00)
print("sum_10=",sum_10)
