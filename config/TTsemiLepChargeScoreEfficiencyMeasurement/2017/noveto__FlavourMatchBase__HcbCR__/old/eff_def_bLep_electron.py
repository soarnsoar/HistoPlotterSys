{
    ##--Use MuonCharge
    ##---bLep_pt
    "bLep_pt_bLepUsingSoftElectronChargeNotOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron","AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.2,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]


    },


    ##---bLep eta
    "bLep_eta_bLepUsingSoftElectronChargeNotOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron","AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.2,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]



    },




    ##--Use OppositeElectronCharge
    ##---bLep_pt

    "bLep_pt_bLepUsingSoftElectronChargeUseOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite","AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.05,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]


    },

    ##---bLep eta

    "bLep_eta_bLepUsingSoftElectronChargeUseOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite","AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron"]
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.05,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]


    },



}
