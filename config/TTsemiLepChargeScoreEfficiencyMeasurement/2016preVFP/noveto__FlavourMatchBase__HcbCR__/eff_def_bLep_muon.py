{
    ##--Use MuonCharge
    ##---bLep_pt
    "bLep_pt_bLepUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon","AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],

    },


    ##---bLep eta
    "bLep_eta_bLepUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bLep_FailSoftMuon","AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
    },




    ##--Use OppositeMuonCharge
    ##---bLep_pt

    "bLep_pt_bLepUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite","AllLep_TTLJ__bLep_FailSoftMuon"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
    },

    ##---bLep eta

    "bLep_eta_bLepUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite","AllLep_TTLJ__bLep_FailSoftMuon"]
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
    },



}
