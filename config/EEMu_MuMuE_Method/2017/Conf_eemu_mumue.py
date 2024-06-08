{
    
    ##---MiNNLO---##
    ##---- no dR between lepton and bjet----##

    ##---Z->MuMu b-, e+ vs e-
    "ZToMuMu_bMinus__Eplus_vs_Eminus_MiNNLO":{
        "cut":["MuMu__bMinus__electronPlus","MuMu__bMinus__electronMinus"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b-","e- in Z->#mu#mu b-" ],
        "title":"Z->#mu#mu b-",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },


    ##---Z->MuMu b-, e+ vs e- @EB
    "ZToMuMu_bMinus__Eplus_vs_Eminus_MiNNLO_EB":{
        "cut":["MuMu__bMinus__electronPlus_EB","MuMu__bMinus__electronMinus_EB"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b-","e- in Z->#mu#mu b-" ],
        "title":"Z->#mu#mu b- @EcalBarrel",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },
    ##---Z->MuMu b-, e+ vs e- @EE
    "ZToMuMu_bMinus__Eplus_vs_Eminus_MiNNLO_EE":{
        "cut":["MuMu__bMinus__electronPlus_EE","MuMu__bMinus__electronMinus_EE"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b-","e- in Z->#mu#mu b-" ],
        "title":"Z->#mu#mu b- @EcalEndcap",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },
    
    
    ##---Z->MuMu b+, e+ vs e-
    "ZToMuMu_bPlus__Eplus_vs_Eminus_MiNNLO":{
        "cut":["MuMu__bPlus__electronPlus","MuMu__bPlus__electronMinus"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b+","e- in Z->#mu#mu b+" ],
        "title":"Z->#mu#mu b+",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },

    ##---Z->MuMu b+, e+ vs e- @EB
    "ZToMuMu_bPlus__Eplus_vs_Eminus_MiNNLO_EB":{
        "cut":["MuMu__bPlus__electronPlus_EB","MuMu__bPlus__electronMinus_EB"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b+","e- in Z->#mu#mu b+" ],
        "title":"Z->#mu#mu b+ @EcalBarrel",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },

    ##---Z->MuMu b+, e+ vs e- @EE
    "ZToMuMu_bPlus__Eplus_vs_Eminus_MiNNLO_EE":{
        "cut":["MuMu__bPlus__electronPlus_EE","MuMu__bPlus__electronMinus_EE"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b+","e- in Z->#mu#mu b+" ],
        "title":"Z->#mu#mu b+ @EcalEndcap",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },

    
    
    ##---Z->EE b-, mu+ vs mu-
    "ZToEE_bMinus__MuPlus_vs_MuMinus_MiNNLO":{
        "cut":["EE__bMinus__muonPlus","EE__bMinus__muonMinus"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["#mu+ in Z->ee b-","#mu- in Z->ee b-" ],
        "title":"Z->ee b-",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },
    
    
    ##---Z->EE b+, mu+ vs mu-
    "ZToEE_bPlus__MuPlus_vs_MuMinus_MiNNLO":{
        "cut":["EE__bPlus__muonPlus","EE__bPlus__muonMinus"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["#mu+ in Z->ee b+","#mu- in Z->ee b+" ],
        "title":"Z->ee b+",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },
    
    
    ##---with dR<0.4 l,bjet----# InBJet

    ##---Z->MuMu b-, e+ vs e-
    "ZToMuMu_bMinus__Eplus_vs_Eminus_InBJet_MiNNLO":{
        "cut":["MuMu__bMinus__electronPlus_InBJet","MuMu__bMinus__electronMinus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b-","e- in Z->#mu#mu b-" ],
        "title":"Z->#mu#mu b- (dR<0.4)",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },


    ##---Z->MuMu b-, e+ vs e- @EB
    "ZToMuMu_bMinus__Eplus_vs_Eminus_InBJet_MiNNLO_EB":{
        "cut":["MuMu__bMinus__electronPlus_InBJet_EB","MuMu__bMinus__electronMinus_InBJet_EB"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b-","e- in Z->#mu#mu b-" ],
        "title":"Z->#mu#mu b- (dR<0.4)@EcalBarrel",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },
    ##---Z->MuMu b-, e+ vs e- @EE
    "ZToMuMu_bMinus__Eplus_vs_Eminus_InBJet_MiNNLO_EE":{
        "cut":["MuMu__bMinus__electronPlus_InBJet_EE","MuMu__bMinus__electronMinus_InBJet_EE"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b-","e- in Z->#mu#mu b-" ],
        "title":"Z->#mu#mu b- (dR<0.4)@EcalEndcap",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },
    
    
    ##---Z->MuMu b+, e+ vs e-
    "ZToMuMu_bPlus__Eplus_vs_Eminus_InBJet_MiNNLO":{
        "cut":["MuMu__bPlus__electronPlus_InBJet","MuMu__bPlus__electronMinus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b+","e- in Z->#mu#mu b+" ],
        "title":"Z->#mu#mu b+(dR<0.4)",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },

    ##---Z->MuMu b+, e+ vs e- @EB
    "ZToMuMu_bPlus__Eplus_vs_Eminus_InBJet_MiNNLO_EB":{
        "cut":["MuMu__bPlus__electronPlus_InBJet_EB","MuMu__bPlus__electronMinus_InBJet_EB"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b+","e- in Z->#mu#mu b+" ],
        "title":"Z->#mu#mu b+(dR<0.4) @EcalBarrel",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },

    ##---Z->MuMu b+, e+ vs e- @EE
    "ZToMuMu_bPlus__Eplus_vs_Eminus_InBJet_MiNNLO_EE":{
        "cut":["MuMu__bPlus__electronPlus_InBJet_EE","MuMu__bPlus__electronMinus_InBJet_EE"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e+ in Z->#mu#mu b+","e- in Z->#mu#mu b+" ],
        "title":"Z->#mu#mu b+(dR<0.4) @EcalEndcap",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },

    
    
    ##---Z->EE b-, mu+ vs mu-
    "ZToEE_bMinus__MuPlus_vs_MuMinus_InBJet_MiNNLO":{
        "cut":["EE__bMinus__muonPlus_InBJet","EE__bMinus__muonMinus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["#mu+ in Z->ee b-","#mu- in Z->ee b-" ],
        "title":"Z->ee b-(dR<0.4)",
        "extratext":"simulation",
        "indexToCompare":0 ,##bkg
    },
    
    
    ##---Z->EE b+, mu+ vs mu-
    "ZToEE_bPlus__MuPlus_vs_MuMinus_InBJet_MiNNLO":{
        "cut":["EE__bPlus__muonPlus_InBJet","EE__bPlus__muonMinus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["#mu+ in Z->ee b+","#mu- in Z->ee b+" ],
        "title":"Z->ee b+(dR<0.4)",
        "extratext":"simulation",
        "indexToCompare":1 ,##bkg
    },
    
    
    ##---Jet to b+ vs b-  ---##
    "bPlus_vs_bMinus_MiNNLO":{
        "cut":["bPlus","bMinus"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z->ll b+","Z->ll b-"],
        "title":"Z->ll",
        "extratext":"simulation",
        
    },

    ##---Jet to b+ vs b-  ---##bPlus_nlepm1
    "bPlus_vs_bMinus_MiNNLO_nlepm1":{
        "cut":["bPlus_nlepm1","bMinus_nlepm1"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z->ll b+","Z->ll b-"],
        "title":"Z->ll if n(lep-)==1 in bjet ",
        "extratext":"simulation",
        
    },

    ##---Jet to b+ vs b-  ---##bPlus_nlepm1
    "bPlus_vs_bMinus_MiNNLO_nmum1":{
        "cut":["bPlus_nmum1","bMinus_nmum1"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z->ll b+","Z->ll b-"],
        "title":"Z->ll if n(mu-)==1 in bjet ",
        "extratext":"simulation",
        
    },

    ##---Jet to b+ vs b-  ---##bPlus_nlepm1
    "bPlus_vs_bMinus_MiNNLO_nem1":{
        "cut":["bPlus_nem1","bMinus_nem1"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z->ll b+","Z->ll b-"],
        "title":"Z->ll if n(e-)==1 in bjet ",
        "extratext":"simulation",
        
    },

    ##---Jet to b+ vs b-  ---##bPlus_nlepp1
    "bPlus_vs_bMinus_MiNNLO_nlepp1":{
        "cut":["bPlus_nlepp1","bMinus_nlepp1"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z->ll b+","Z->ll b-"],
        "title":"Z->ll if n(lep+)==1 in bjet ",
        "extratext":"simulation",
        
    },

    ##---Jet to b+ vs b-  ---##bPlus_nmup1
    "bPlus_vs_bMinus_MiNNLO_nmup1":{
        "cut":["bPlus_nmup1","bMinus_nmup1"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z->ll b+","Z->ll b-"],
        "title":"Z->ll if n(mu+)==1 in bjet ",
        "extratext":"simulation",
        
    },

    ##---Jet to b+ vs b-  ---##bPlus_nep1
    "bPlus_vs_bMinus_MiNNLO_nep1":{
        "cut":["bPlus_nep1","bMinus_nep1"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z->ll b+","Z->ll b-"],
        "title":"Z->ll if n(e+)==1 in bjet ",
        "extratext":"simulation",
        
    },
    

    

    
}
