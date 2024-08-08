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
        "ymax":0.2,
        "xbins":[30,50,70,100,140,200,300]
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
        "ymax":0.2,
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5]
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
        "ymax":0.05,
        "xbins":[30,50,70,100,140,200,300]
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
        "ymax":0.05,
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5]
    },



}
