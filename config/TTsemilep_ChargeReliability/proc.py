from collections import OrderedDict
dict_proc=OrderedDict([
    ("DY",{
        "procs":["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"],
        "color":8,
        #"color":40,
        "name":"DY",
    }),
    ("QCD",{
        "procs":["QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"],
        "color":9,
        #"color":41,
        "name":"QCD",
    }),
    ("WJets",{
        "procs":["WJets_Sherpa"],
        "name":"W+jets",
       "color":7,
        #"color":42,
    }),
    ("TTLL",{
        "procs":["TTLL_powheg"],
        "name":"TTLL",
        "color":6,
        #"color":45,
    }),
    ("TTLJ_Unmatched",{
        "procs":["TTLJ_powheg_bHadJet_Unmatched","TTLJ_powheg_bLepJet_Unmatched"],
        "name":"TTLJ No b-flv matching",
        "color":3,
        #"color":46,
    }),

    ("SingleTop",{
        "procs":["SingleTop_sch_Lep","SingleTop_tch_antitop_incl","SingleTop_tch_top_incl","SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad",""],
        "color":5,
        #"color":30,
        "name":"SingleTop"
    }),
    ("TTLJ_bMatched",{
        "procs":["TTLJ_powheg_bHadJet_true_bmatch","TTLJ_powheg_bLepJet_true_bmatch"],
        "color":2,
        #"color":32,
        "name":"TTLJ matching to b"
    }),
    ("TTLJ_bbarMatched",{
        "procs":["TTLJ_powheg_bHadJet_true_bbarmatch","TTLJ_powheg_bLepJet_true_bbarmatch"],
        "name":"TTLJ matching to #bar{b}",
        "color":4,
        #"color":38,
    }),


    ("Data",{
        "proc":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
    
]
)
