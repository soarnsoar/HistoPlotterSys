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
        "ymax":0.2,
        "xbins":[30,50,70,100,140,200,300],
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
        "ymax":0.2,
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5],

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
        "ymax":0.05,
        "xbins":[30,50,70,100,140,200,300],
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
        "ymax":0.05,
        "xbins":[-2.5,-2,-1.6, -0.8, 0, 0.8, 1.6, 2, 2.5],

    },



}
