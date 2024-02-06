from collections import OrderedDict
dict_proc=OrderedDict({
    "DY":{
        "procs":["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO"],
        "color":8,
        "name":"DY",
    },
    "QCD":{
        "procs":["QCD_bEnriched_HT1000To1500","QCD_bEnriched_HT1500To2000","QCD_bEnriched_HT200To300","QCD_bEnriched_HT300To500","QCD_bEnriched_HT500To700","QCD_bEnriched_HT700To1000"],
        "color":6,
        "name":"QCD",
    },
    "SingleTop":{
        "procs":["SingleTop_sch_Lep","SingleTop_tch_antitop_incl","SingleTop_tch_top_incl","SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad",""],
        "color":3,
        "name":"SingleTop"
    },
    "TTLJ_bMatched":{
        "procs":["TTLJ_powheg_bHadJet_true_bmatch","TTLJ_powheg_bLepJet_true_bmatch"],
        "color":2,
        "name":"TTLJ matching to b"
    },
    "TTLJ_bbarMatched":{
        "procs":["TTLJ_powheg_bHadJet_true_bbarmatch","TTLJ_powheg_bLepJet_true_bbarmatch"],
        "name":"TTLJ matching to #bar{b}",
        "color":4,
    },
    "TTLJ_Unmatched":{
        "procs":["TTLJ_powheg_bHadJet_Unmatched","TTLJ_powheg_bLepJet_Unmatched"],
        "name":"TTLJ No b-flv matching",
        "color":5,
    },
    "TTLL":{
        "procs":["TTLL_powheg"],
        "name":"TTLL",
        "color":7,
    },
    "WJets":{
        "procs":["WJets_Sherpa"],
        "name":"W+jets",
       "color":9,
    },
    "Data":{
        "proc":["Data"],
        "name":"Data",
        "IsData":True,
    }

}
)
