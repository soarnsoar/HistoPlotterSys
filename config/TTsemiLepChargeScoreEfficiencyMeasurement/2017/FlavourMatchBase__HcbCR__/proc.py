[

    ("bkgs",{
        "procs": [ _proc+_suffix for _proc in ["WW_pythia","WZ_pythia","ZZ_pythia"]+["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO","WJets_Sherpa"]+["SingleTop_sch_Lep","SingleTop_tch_antitop_Incl","SingleTop_tch_top_Incl","SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"]+ ["TTLL_powheg"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
        "color":4,
        "name":"bkgs",
    }),

    ("Not From bquark",{
        "procs":[ _proc+_suffix for _proc in ["TTLJ_powheg"] for _suffix in ["_NonFromb"]],
        "name":"TTLJ_NonFromb",
        "color":7,
    }),

    ("bLepCandFrom bquark",{
        "procs":[ _proc+_suffix for _proc in ["TTLJ_powheg"] for _suffix in ["_bLepCandFromb"]],
        "name":"TTLJ_bLepCandFromb",
        "color":9,
    }),


    ("bHadCandFrom bquark",{
        "procs":[ _proc+_suffix for _proc in ["TTLJ_powheg"] for _suffix in ["_bHadCandFromb"]],
        "name":"TTLJ_bHadCandFromb",
        "color":3,
    }),


    ("All bCand From bquark",{
        "procs":[ _proc+_suffix for _proc in ["TTLJ_powheg"] for _suffix in ["_All_bjetFromb"]],
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


