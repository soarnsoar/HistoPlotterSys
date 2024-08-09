{
    ##--Use ElectronCharge
    ##---bHad_pt
    "bHad_pt_bHadUsingGoodJetCharge":{
        "deno":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingGoodJetCharge","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "nume":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingGoodJetCharge"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
        "ymax":1.,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]


    },

    ##---bHad eta
    "bHad_eta_bHadUsingGoodJetCharge":{
        "deno":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingGoodJetCharge","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"],
        },
        "nume":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingGoodJetCharge"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
        "ymax":1.,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
    },




}
