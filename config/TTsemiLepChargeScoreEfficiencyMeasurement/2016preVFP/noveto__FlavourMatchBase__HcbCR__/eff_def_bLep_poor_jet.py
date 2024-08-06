{
    ##--Use ElectronCharge
    ##---bLep_pt
    "bLep_pt_bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet":{
        "deno":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingGoodJetCharge","AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],

    },

    ##---bLep eta
    "bLep_eta_bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet":{
        "deno":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingGoodJetCharge","AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"]
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
    },




}
