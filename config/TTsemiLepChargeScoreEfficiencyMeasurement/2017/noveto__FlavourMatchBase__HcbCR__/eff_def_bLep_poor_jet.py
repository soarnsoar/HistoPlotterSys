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
        "ymax":1.0,
        "xbins":[30,50,70,100,140,200,300],
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
        "ymax":1.0,
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5]


    },




}
