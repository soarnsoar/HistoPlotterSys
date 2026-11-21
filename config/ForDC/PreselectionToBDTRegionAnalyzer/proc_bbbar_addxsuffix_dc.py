[

    
    ("Bkg_Others",{
        "procs":["VV"]+["WJets_MG"],
        "color":5,
        "name":"OtherBkg",
    }),
    ("Bkg_QCD",{
        "procs":["QCD_bEnriched"],
        "color":5,
        "name":"QCD",
    }),
    ("SingleTop_sch",{
        "procs":["SingleTop_sch_Lep"],
        "color":5,
        "name":"SingleTop_sch_Lep",
    }),

    ("SingleTop_tch_top",{
        "procs":["SingleTop_tch_top_Incl"],
        "color":5,
        "name":"SingleTop_tch_top",
    }),
    ("SingleTop_tch_antitop",{
        "procs":["SingleTop_tch_antitop_Incl"],
        "color":5,
        "name":"SingleTop_tch_antitop",
    }),
    ("SingleTop_tW",{
        "procs":["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"],
        "color":5,
        "name":"SingleTop_tW",
    }),            

    ("TTLL",{
        "procs":["TTLL_powheg"],
        "color":5,
        "name":"TTLL",
    }),
    ("TTLJ",{
        "procs":["TTLJ_powheg"],
        "color":5,
        "name":"TTLJ",
    }),                
    
    ("DYothers",{
        "procs":["DY"],
        "color":8,
        "name":"DY others",
    }),

    ##  __logx_-InfTo-4.5
    ##  __logx_-4.5To-3.5
    ##  __logx_-3.5To0

    ("DYbminus_logx_Under_m4.5",{
        "procs":["DYgb__blogx_-InfTo-4.5"],
        "color":61,
        "name":"DY b^{-}, log(xb)<-4.5",
        "IsSig":True,
    }),
    ("DYbminus_logx_m4.5_To_m3.5",{
        "procs":['DYgb__blogx_-4.5To-3.5'],
        "color":65,
        "name":"DY b^{-}, -4.5<log(xb)<-3.5",
        "IsSig":True,
    }),
    ("DYbminus_logx_Over_m3.5",{
        "procs":['DYgb__blogx_-3.5To0'],
        "color":70,
        "name":"DY b^{-}, log(xb)>-3.5",
        "IsSig":True,
    }),    

    

    ("DYbplus_logx_Under_m4.5",{
        "procs":['DYgb__bbarlogx_-InfTo-4.5'],
        "color":91,
        "name":"DY b^{+}, log(xb)<-4.5",
        "IsSig":True,
    }),

    ("DYbplus_logx_m4.5_To_m3.5",{
        "procs":['DYgb__bbarlogx_-4.5To-3.5'],
        "color":95,
        "name":"DY b^{+}, -4.5<log(xb)<-3.5",
        "IsSig":True,
    }),

    ("DYbplus_logx_Over_m3.5",{
        "procs":['DYgb__bbarlogx_-3.5To0'],
        "color":99,
        "name":"DY b^{+}, log(xb)>-3.5",
        "IsSig":True,
    }),            

    ("Data",{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
]


