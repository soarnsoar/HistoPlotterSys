[


    ("bkgs",{
        "procs":["WW_pythia","WZ_pythia","ZZ_pythia"]+["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO","WJets_Sherpa"]+["SingleTop_sch_Lep","SingleTop_tch_antitop_Incl","SingleTop_tch_top_Incl","SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"]+["TTLL_powheg"],
        "color":4,
        "name":"bkgs",
    }),

    ("Not From bquark",{
        "procs":["TTLJ_powheg_Unmatched"],
        "name":"TTLJ_NonFromb",
        "color":7,
    }),

    ("bLepCandFrom bquark",{
        "procs":["TTLJ_powheg_bLepMatchedOnly"],
        "name":"TTLJ_bLepCandFromb",
        "color":9,
    }),

    ("bHadCandFrom bquark",{
        "procs":["TTLJ_powheg_bHadMatchedOnly"],
        "name":"TTLJ_bHadCandFromb",
        "color":3,
    }),

    ("All bCand From bquark",{
        "procs":["TTLJ_powheg_AllMatched"],
        "name":"TTLJ_All_bjetFromb",
        "color":2,
    }),


    ("Data",{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
]


