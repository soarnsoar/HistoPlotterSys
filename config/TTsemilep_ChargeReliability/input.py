import os
maindir=os.getenv("GIT_HistoPlotterSys")
#print maindir
maindir2=maindir+"/SKFlatOutput/TTsemilep_ChargeReliability/"
#print maindir2
dict_input={
    "MuonHadAcc":maindir2+"RunSyst__RunSoftMuon__RunHadronSide__RunChAcc__/combine.root",
    "MuonLepAcc":maindir2+"RunSyst__RunSoftMuon__RunLeptonSide__RunChAcc__/combine.root",
    "ElectronHadAcc":maindir2+"RunSyst__RunSoftElectron__RunHadronSide__RunChAcc__/combine.root",
    "ElectronLepAcc":maindir2+"RunSyst__RunSoftElectron__RunLeptonSide__RunChAcc__/combine.root",
    "JetHadAcc":maindir2+"RunSyst__RunJet__RunHadronSide__RunChAcc__/combine.root",
    "JetLepAcc":maindir2+"RunSyst__RunJet__RunLeptonSide__RunChAcc__/combine.root",

    "MuonHadReliab":maindir2+"RunSyst__RunSoftMuon__RunHadronSide__RunReliab__/combine.root",
    "MuonLepReliab":maindir2+"RunSyst__RunSoftMuon__RunLeptonSide__RunReliab__/combine.root",
    "ElectronHadReliab":maindir2+"RunSyst__RunSoftElectron__RunHadronSide__RunReliab__/combine.root",
    "ElectronLepReliab":maindir2+"RunSyst__RunSoftElectron__RunLeptonSide__RunReliab__/combine.root",
    "JetHadReliab":maindir2+"RunSyst__RunJet__RunHadronSide__RunReliab__/combine.root",
    "JetLepReliab":maindir2+"RunSyst__RunJet__RunLeptonSide__RunReliab__/combine.root",
}
