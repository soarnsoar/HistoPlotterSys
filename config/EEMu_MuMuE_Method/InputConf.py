{
    ##---Z->MuMu b-, e+ vs e-
    "MuMu_bMinus__Eplus_vs_Eminus":{
        "Year":"scanall", ##if all, denominator and numerators have the common value iterating all available ones.
        "x":"scanall",
        "cut":["MuMu__bMinus__electronPlus","MuMu__bMinus__electronMinus"],
        "proc":"scanall",
        "color":[2,4],
    },


    ##---Z->MuMu b+, e+ vs e-
    "MuMu_bPlus__Eplus_vs_Eminus":{
        "Year":"scanall", ##if all, denominator and numerators have the common value iterating all available ones.
        "x":"scanall",
        "cut":["MuMu__bPlus__electronPlus","MuMu__bPlus__electronMinus"],
        "proc":"scanall",
        "color":[2,4],
    },


    ##---Z->EE b-, mu+ vs mu-
    "EE_bMinus__MuPlus_vs_MuMinus":{
        "Year":"scanall", ##if all, denominator and numerators have the common value iterating all available ones.
        "x":"scanall",
        "cut":["EE__bMinus__muonPlus","EE__bMinus__muonMinus"],
        "proc":"scanall",
        "color":[2,4],
    },


    ##---Z->EE b+, mu+ vs mu-
    "EE_bPlus__MuPlus_vs_MuMinus":{
        "Year":"scanall", ##if all, denominator and numerators have the common value iterating all available ones.
        "x":"scanall",
        "cut":["EE__bPlus__muonPlus","MuMu__bPlus__muonMinus"],
        "proc":"scanall",
        "color":[2,4],
    },


}
