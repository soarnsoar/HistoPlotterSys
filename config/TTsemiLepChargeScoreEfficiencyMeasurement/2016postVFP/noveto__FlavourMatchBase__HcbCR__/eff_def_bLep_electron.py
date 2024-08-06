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
    },



}
