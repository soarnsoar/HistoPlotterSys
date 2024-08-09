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
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]

        
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
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]

    },




}
