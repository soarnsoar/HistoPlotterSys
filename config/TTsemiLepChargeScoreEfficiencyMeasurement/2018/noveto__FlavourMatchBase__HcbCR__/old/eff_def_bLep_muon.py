{
    ##--Use MuonCharge
    ##--AllTTLJ
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
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]
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
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
    },



    ##--TTMuJ
    ##---bLep_pt
    "bLep_pt_bLepUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite","Muon_TTLJ__bLep_FailSoftMuon","Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.2,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]
    },


    ##---bLep eta
    "bLep_eta_bLepUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite","Muon_TTLJ__bLep_FailSoftMuon","Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.2,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
    },

    ##---TTEJ
    ##---bLep_pt
    "bLep_pt_bLepUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite","Electron_TTLJ__bLep_FailSoftMuon","Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.2,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]
    },


    ##---bLep eta
    "bLep_eta_bLepUsingSoftMuonChargeNotOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite","Electron_TTLJ__bLep_FailSoftMuon","Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.2,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
    },



    ##--Use OppositeMuonCharge

    ##--ALLTTLJ
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
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]
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
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]

    },



    ##--TTMuJ
    ##---bLep_pt

    "bLep_pt_bLepUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite","Muon_TTLJ__bLep_FailSoftMuon"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.05,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]
    },

    ##---bLep eta

    "bLep_eta_bLepUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite","Muon_TTLJ__bLep_FailSoftMuon"]
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.05,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]

    },

    ##--TTEJ
    ##---bLep_pt

    "bLep_pt_bLepUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bLep_pt",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite","Electron_TTLJ__bLep_FailSoftMuon"],
        },
        "nume":{
            "x":"bLep_pt",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.05,
        "xbins":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000]
    },

    ##---bLep eta

    "bLep_eta_bLepUsingSoftMuonChargeUseOpposite":{
        "deno":{
            "x":"bLep_eta",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite","Electron_TTLJ__bLep_FailSoftMuon"]
        },
        "nume":{
            "x":"bLep_eta",
            "cut":["Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"],
        },
        "sig":["bLepCandFrom bquark","All bCand From bquark"],
        "bkg":["Not From bquark","bHadCandFrom bquark"],
        "ymax":0.05,
        "xbins":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4]

    },



}
