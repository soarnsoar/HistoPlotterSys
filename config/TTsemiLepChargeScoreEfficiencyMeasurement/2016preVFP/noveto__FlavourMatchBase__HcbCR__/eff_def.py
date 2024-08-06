{
    ##--Use MuonCharge
    ##---bLep_pt
    "bLep_pt_PassSoftMuonCutUsingMuonCharge":{
        "deno":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],

    },

    "bLep_pt_PassSoftMuonCutUsingOppositeMuonCharge":{
        "deno":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
    },

    "bLep_eta_PassSoftMuonCutUsingMuonCharge":{
        "deno":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon"],
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
    },

    "bLep_eta_PassSoftMuonCutUsingOppositeMuonCharge":{
        "deno":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon"]
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
    },


}
