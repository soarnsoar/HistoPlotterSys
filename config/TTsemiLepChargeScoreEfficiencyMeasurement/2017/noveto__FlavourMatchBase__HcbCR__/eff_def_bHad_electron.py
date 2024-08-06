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
    },



}
