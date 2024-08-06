{
    ##--Use ElectronCharge
    ##---bHad_pt
    "bHad_pt_bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet":{
        "deno":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingGoodJetCharge","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "nume":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],

    },

    ##---bHad eta
    "bHad_eta_bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet":{
        "deno":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingGoodJetCharge","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "nume":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"]
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
    },




}
