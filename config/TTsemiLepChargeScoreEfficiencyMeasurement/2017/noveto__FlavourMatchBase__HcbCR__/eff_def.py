{
    "Muon_bLep_pt__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bHad_eta__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bHad_eta__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "AllLep_bLep_pt__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bHad_pt__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "AllLep_bLep_pt__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bLep_eta__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_pt__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_pt__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bLep_eta__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_eta__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bLep_eta__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bLep_pt__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "AllLep_bHad_eta__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_eta__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bLep_pt__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bLep_eta__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bHad_eta__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bHad_pt__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bHad_pt__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bLep_eta__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bLep_eta__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bLep_pt__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_eta__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_eta__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "AllLep_bLep_pt__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bLep_eta__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bHad_eta__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bHad_pt__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bHad_pt__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "AllLep_bLep_pt__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "Muon_bHad_eta__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bLep_pt__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "Electron_bHad_eta__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bHad_eta__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bHad_pt__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bHad_pt__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_pt__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bHad_eta__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bHad_eta__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bLep_pt__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_eta__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bLep_eta__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_pt__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bHad_pt__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bLep_pt__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_pt__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bLep_eta__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_eta__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_pt__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bHad_pt__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Muon_bLep_eta__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bLep_eta__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "AllLep_bLep_eta__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bLep_pt__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bLep_pt__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bHad_eta__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "Electron_bHad_pt__Usepoor_jetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bHad_pt__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bHad_pt__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bHad_eta__UsemuonCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_eta__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_pt__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bLep_eta__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bHad_pt__UseelectronCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.2, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }
    }, 
    "AllLep_bLep_pt__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bHad_pt__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "Muon_bHad_pt__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            30, 
            40, 
            50, 
            60, 
            70, 
            80, 
            90, 
            100, 
            120, 
            140, 
            160, 
            180, 
            200, 
            300
        ], 
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "Electron_bLep_eta__Usemuon-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }
    }, 
    "Muon_bHad_eta__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }, 
    "Electron_bHad_eta__Useelectron-OppositeCharge": {
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark"
        ], 
        "ymax": 0.05, 
        "nume": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "sig": [
            "bHadCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }
    }, 
    "AllLep_bLep_eta__UsejetCharge": {
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark"
        ], 
        "ymax": 1.0, 
        "nume": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge"
            ]
        }, 
        "sig": [
            "bLepCandFrom bquark", 
            "All bCand From bquark"
        ], 
        "xbins": [
            -2.4, 
            -2.2, 
            -2.0, 
            -1.8, 
            -1.6, 
            -1.4, 
            -1.2, 
            -1.0, 
            -0.8, 
            -0.6, 
            -0.4, 
            -0.2, 
            0, 
            0.2, 
            0.4, 
            0.6, 
            0.8, 
            1.0, 
            1.2, 
            1.4, 
            1.6, 
            1.8, 
            2.0, 
            2.2, 
            2.4
        ], 
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }
    }
}