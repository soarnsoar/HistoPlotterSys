[

    
    ("Bkg_Others",{
        "procs":["WW_pythia","WZ_pythia","ZZ_pythia"]+["WJets_MG"],
        "color":5,
        "name":"OtherBkg",
    }),
    ("Bkg_QCD",{
        "procs":["QCD_bEnriched_HT100to200","QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000",'QCD_bEnriched_HT2000toInf'],
        "color":5,
        "name":"QCD",
    }),
    ("SingleTop_sch",{
        "procs":["SingleTop_sch_Lep"],
        "color":5,
        "name":"SingleTop_sch_Lep",
    }),

    ("SingleTop_tch_top",{
        "procs":["SingleTop_tch_top_Incl"],
        "color":5,
        "name":"SingleTop_tch_top",
    }),
    ("SingleTop_tch_antitop",{
        "procs":["SingleTop_tch_antitop_Incl"],
        "color":5,
        "name":"SingleTop_tch_antitop",
    }),
    ("SingleTop_tW",{
        "procs":["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"],
        "color":5,
        "name":"SingleTop_tW",
    }),            

    ("TTLL",{
        "procs":["TTLL_powheg"],
        "color":5,
        "name":"TTLL",
    }),
    ("TTLJ",{
        "procs":["TTLJ_powheg"],
        "color":5,
        "name":"TTLJ",
    }),                
    
    ("DYothers",{
        "procs":[p+"_others" for p in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"]],
        "color":8,
        "name":"DY others",
    }),

    ##  __logx_-InfTo-4.5
    ##  __logx_-4.5To-3.5
    ##  __logx_-3.5To0

    ("DYbminus_logx_Under_m4.5",{
        "procs":[p+"_b__logx_-InfTo-4.5" for p in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"]],
        "color":61,
        "name":"DY b^{-}, log(xb)<-4.5",
        "IsSig":True,
    }),
    ("DYbminus_logx_m4.5_To_m3.5",{
        "procs":[p+"_b__logx_-4.5To-3.5" for p in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"]],
        "color":65,
        "name":"DY b^{-}, -4.5<log(xb)<-3.5",
        "IsSig":True,
    }),
    ("DYbminus_logx_Over_m3.5",{
        "procs":[p+"_b__logx_-3.5To0" for p in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"]],
        "color":70,
        "name":"DY b^{-}, log(xb)>-3.5",
        "IsSig":True,
    }),    

    

    ("DYbplus_logx_Under_m4.5",{
        "procs":[p+"_bbar__logx_-InfTo-4.5" for p in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"]],
        "color":91,
        "name":"DY b^{+}, log(xb)<-4.5",
        "IsSig":True,
    }),

    ("DYbplus_logx_m4.5_To_m3.5",{
        "procs":[p+"_bbar__logx_-4.5To-3.5" for p in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"]],
        "color":95,
        "name":"DY b^{+}, -4.5<log(xb)<-3.5",
        "IsSig":True,
    }),

    ("DYbplus_logx_Over_m3.5",{
        "procs":[p+"_bbar__logx_-3.5To0" for p in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"]],
        "color":99,
        "name":"DY b^{+}, log(xb)>-3.5",
        "IsSig":True,
    }),            

    ("Data",{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
]


