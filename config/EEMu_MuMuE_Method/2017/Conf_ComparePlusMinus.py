{
    
    ##---MiNNLO---##
    

    "bPlus_vs_bMinus":{
        "cut":["bMinus","bPlus"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["Z b-","Z b+"],
        "title":"Z+b b vs #bar{b}",
        "extratext":"simulation"
    },
    


    "mum_vs_mup_In_Zee_b":{
        "cut":["EE__bMinus__muonMinus_InBJet","EE__bPlus__muonPlus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["#mu- in Z->ee b-","#mu+ in Z->ee b+" ],
        "title":"[ee+b] #mu- vs #mu+ , #DeltaR(l,j)<0.4",
        "extratext":"simulation"
    },

    "mum_vs_mup Zmumu b":{
        "cut":["MuMu__bMinus__muonMinus_InBJet","MuMu__bPlus__muonPlus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["#mu- in Z->#mu#mu b-","#mu+ in Z->#mu#mu b+" ],
        "title":"[#mu#mu+b] #mu- vs #mu+ #DeltaR(l,j)<0.4",
        "extratext":"simulation"
    },


    "em_vs_ep In Zee b":{
        "cut":["EE__bMinus__electronMinus_InBJet","EE__bPlus__electronPlus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e- in Z->ee b-","e+ in Z->ee b+" ],
        "title":"[ee+b] e- vs e+ , #DeltaR(l,j)<0.4",
        "extratext":"simulation"
    },

    "em_vs_ep_Zmumu_b":{
        "cut":["MuMu__bMinus__electronMinus_InBJet","MuMu__bPlus__electronPlus_InBJet"],
        "color":[2,4],
        "proc":["DY_MiNNLO"]*2,
        "label":["e- in Z->#mu#mu b-","e+ in Z->#mu#mu b+" ],
        "title":"[#mu#mu+b] e- vs e+ #DeltaR(l,j)<0.4",
        "extratext":"simulation"
    },


    
    
    
    
}
