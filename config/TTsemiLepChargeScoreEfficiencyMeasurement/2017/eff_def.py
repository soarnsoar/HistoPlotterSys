{
    "Muon_bLep_pt__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_eta__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_eta__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_pt__UseelectronCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_pt__UsejetCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_pt__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_eta__UsemuonCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_pt__UseelectronCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_pt__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_eta__UsemuonCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_eta__UseelectronCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_eta__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_pt__UsejetCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_eta__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_eta__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_pt__UsemuonCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_eta__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_eta__UseelectronCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_pt__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_pt__UseelectronCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_eta__UseelectronCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_eta__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_pt__UsemuonCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_eta__UseelectronCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_eta__UsejetCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_pt__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_eta__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_eta__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_pt__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_pt__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_pt__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_eta__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_pt__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_eta__UsemuonCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_eta__UsejetCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_pt__UseelectronCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_pt__UsemuonCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_pt__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_eta__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_eta__UsejetCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_pt__UsemuonCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_eta__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_eta__UsemuonCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_pt__UsemuonCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_pt__UsejetCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingGoodJetCharge", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_pt__UseelectronCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "Muon_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_pt__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_eta__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLep_FailSoftMuon", 
                "AllLep_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_eta__UsemuonCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_pt__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_pt__UsejetCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_eta__UsejetCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLepUsingGoodJetCharge", 
                "Muon_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_eta__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_eta__UseelectronCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bLepUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_pt__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_pt__UsejetCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "Electron_TTLJ__bLepUsingGoodJetCharge", 
                "Electron_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_eta__UseelectronCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_pt__Usepoor_jetCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingGoodJetCharge", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_pt__UsemuonCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon", 
                "Electron_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_pt__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_eta__UsemuonCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftMuonChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon", 
                "AllLep_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_eta__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_pt__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHad_FailSoftMuon", 
                "Muon_TTLJ__bHadUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bLep_eta__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Muon_TTLJ__bLep_FailSoftMuon", 
                "Muon_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bHad_pt__UseelectronCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "AllLep_TTLJ__bHadUsingSoftElectronChargeNotOpposite", 
                "AllLep_TTLJ__bHad_FailSoftMuon__FailSoftElectron", 
                "AllLep_TTLJ__bHadUsingSoftElectronChargeUseOpposite"
            ]
        }, 
        "ymax": 0.2, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_pt__UsejetCharge": {
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
        "deno": {
            "x": "bLep_pt", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_pt__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_pt__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bHad_pt", 
            "cut": [
                "Muon_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bLep_eta__Usemuon-OppositeCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "Electron_TTLJ__bLep_FailSoftMuon", 
                "Electron_TTLJ__bLepUsingSoftMuonChargeUseOpposite"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Muon_bHad_eta__UsejetCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Muon_TTLJ__bHadUsingGoodJetCharge", 
                "Muon_TTLJ__bHad_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "Electron_bHad_eta__Useelectron-OppositeCharge": {
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
        "deno": {
            "x": "bHad_eta", 
            "cut": [
                "Electron_TTLJ__bHadUsingSoftElectronChargeUseOpposite", 
                "Electron_TTLJ__bHad_FailSoftMuon__FailSoftElectron"
            ]
        }, 
        "ymax": 0.05, 
        "bkg": [
            "Not From bquark", 
            "bLepCandFrom bquark", 
            "bkgs"
        ]
    }, 
    "AllLep_bLep_eta__UsejetCharge": {
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
        "deno": {
            "x": "bLep_eta", 
            "cut": [
                "AllLep_TTLJ__bLepUsingGoodJetCharge", 
                "AllLep_TTLJ__bLep_FailSoftMuon__FailSoftElectron__FailGoodBJet"
            ]
        }, 
        "ymax": 1.0, 
        "bkg": [
            "Not From bquark", 
            "bHadCandFrom bquark", 
            "bkgs"
        ]
    }
}