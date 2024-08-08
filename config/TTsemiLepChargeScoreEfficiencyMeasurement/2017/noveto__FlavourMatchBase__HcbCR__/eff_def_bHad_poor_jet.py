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
        "ymax":1.0,
        "xbins":[30,50,70,100,140,200,300],
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
        "ymax":1.0,
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5],
    },




}
