{

    "WJets":{
        "procs":["WJets_Sherpa"],
        "name":"W+jets",
        "color":7,
    },
    "TT":{
        "procs":["TTLJ_powheg","TTLL_powheg"],
        "name":"TT",
        "color":5,
    },
    "SingleTop":{
        "procs":["SingleTop_sch_Lep","SingleTop_tch_antitop_Incl","SingleTop_tch_top_Incl","SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"],
        #"color":3,
        "color":6,
        "name":"SingleTop"
    },

    "DY":{
        "procs":["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"],
        "color":8,
        "name":"DY",
    },
    "QCD":{
        "procs":["QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000","QCD_Pt-1000_MuEnriched",
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
],
        "color":9,
        "name":"QCD",
    },

    
    "Data":{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }
}


