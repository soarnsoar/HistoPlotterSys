{
    ##--Use MuonCharge
    ##---bHad_pt
    "bHad_pt_bHadUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bHad_FailSoftMuon","AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],

    },


    ##---bHad eta
    "bHad_eta_bHadUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite","AllLep_TTLJ__bHad_FailSoftMuon","AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
    },




    ##--Use OppositeMuonCharge
    ##---bHad_pt

    "bHad_pt_bHadUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite","AllLep_TTLJ__bHad_FailSoftMuon"],
        },
        "nume":{
            "x":"bHad_pt",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
    },

    ##---bHad eta

    "bHad_eta_bHadUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite","AllLep_TTLJ__bHad_FailSoftMuon"]
        },
        "nume":{
            "x":"bHad_eta",
            "cut":["AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bHadCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bLepCandFrom bquark"],
    },



}
