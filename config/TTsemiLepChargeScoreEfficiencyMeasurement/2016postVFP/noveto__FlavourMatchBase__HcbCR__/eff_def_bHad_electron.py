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
        "xbins":[30,50,70,100,140,200,300],
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
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5],
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
        "xbins":[30,50,70,100,140,200,300],
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
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5],
    },



}
