{
    ##--Use MuonCharge
    ##---bHad_pt
    "bHad_pt_bHadUsingSoftElectronChargeNotOpposite":{
        "deno":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron","AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"],
        },
        "nume":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
        "ymax":0.2,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]


    },


    ##---bHad eta
    "bHad_eta_bHadUsingSoftElectronChargeNotOpposite":{
        "deno":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron","AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"],
        },
        "nume":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
        "ymax":0.2,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
        
    },




    ##--Use OppositeElectronCharge
    ##---bHad_pt

    "bHad_pt_bHadUsingSoftElectronChargeUseOpposite":{
        "deno":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron"],
        },
        "nume":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
        "ymax":0.05,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]


    },

    ##---bHad eta

    "bHad_eta_bHadUsingSoftElectronChargeUseOpposite":{
        "deno":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite","AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron"]
        },
        "nume":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
        "ymax":0.05,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
        
    },



}
