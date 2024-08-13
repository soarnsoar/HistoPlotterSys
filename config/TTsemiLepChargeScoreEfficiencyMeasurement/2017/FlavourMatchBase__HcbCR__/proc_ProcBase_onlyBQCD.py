[

    ("VV",{
        "procs": [ _proc+_suffix for _proc in ["WW_pythia","WZ_pythia","ZZ_pythia"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
        "color":4,
        "name":"VV",
    }),
    ("Vjets",{
        "procs":[ _proc+_suffix for _proc in ["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO","WJets_Sherpa"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
        "color":8,
        "name":"Vjets",
    }),
    ("QCD",{
        "procs":[ _proc+_suffix for _proc in ["QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
        "color":2,
        "name":"QCD",
    }),

    ("SingleTop",{
        "procs": [ _proc+_suffix for _proc in ["SingleTop_sch_Lep","SingleTop_tch_antitop_Incl","SingleTop_tch_top_Incl","SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],

        "color":6,
        "name":"SingleTop"
    }),
    ("TTLL",{
        "procs":[ _proc+_suffix for _proc in ["TTLL_powheg"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
        "name":"TTLL",
        "color":5,
    }),

    ("TTLJ",{
        "procs":[ _proc+_suffix for _proc in ["TTLJ_powheg"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
        "name":"TTLJ",
        "color":9,
    }),


    ("Data",{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
]


