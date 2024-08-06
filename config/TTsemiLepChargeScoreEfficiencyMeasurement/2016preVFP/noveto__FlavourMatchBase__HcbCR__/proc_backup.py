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
        "procs":[ _proc+_suffix for _proc in ["QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"]+\
        ["QCD_Pt-1000_MuEnriched",
         "QCD_Pt-800To1000_MuEnriched",
         "QCD_Pt-600To800_MuEnriched",
         "QCD_Pt-470To600_MuEnriched",
         "QCD_Pt-300To470_MuEnriched",
         "QCD_Pt-170To300_MuEnriched",
         "QCD_Pt-120To170_MuEnriched",
         "QCD_Pt-80To120_MuEnriched",
         "QCD_Pt-50To80_MuEnriched",
         "QCD_Pt-30To50_MuEnriched",
         "QCD_Pt-20To30_MuEnriched",
         "QCD_Pt-15To20_MuEnriched",
         "QCD_Pt-300toInf_EMEnriched",
         "QCD_Pt-170to300_EMEnriched",
         "QCD_Pt-120to170_EMEnriched",
         "QCD_Pt-80to120_EMEnriched",
         "QCD_Pt-50to80_EMEnriched",
         "QCD_Pt-30to50_EMEnriched",
         "QCD_Pt-20to30_EMEnriched",
         "QCD_Pt-15to20_EMEnriched",
     ] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
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
        "procs":[ _proc+_suffix for _proc in ["TTLJ"] for _suffix in ["_NonFromb","_bHadCandFromb","_bLepCandFromb","_All_bjetFromb"]],
        "name":"TT",
        "color":9,
    }),


    ("Data",{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
]


