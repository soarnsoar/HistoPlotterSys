[
    ##-----bjet origin == NON Top Bkgs-----##

    ("OverlapPromptLep__OtherProc",{
        "procs":
        [proc+"_PromptContam" for proc in ["VJets","VV"]],
        "color":2,
        "name":"OverlapPromptLep__OtherProc",
    }),

    
    ("from_Others__OtherProc",{
        "procs":
        [proc+"_FromOthers" for proc in ["VJets","VV"]],
        "color":2,
        "name":"from_Others__OtherProc",
    }),


    ("from_bminus__OtherProc",{
        "procs":
        [proc+"_Frombminus" for proc in ["VJets","VV"]],
        "color":3,
        "name":"from_bminus__OtherProc",

    }),

    ("from_bplus__OtherProc",{
        "procs":
        [proc+"_Frombplus" for proc in ["VJets","VV"]],
        "color":3,
        "name":"from_bplus__OtherProc",

    }),

    #0) QCD processes
    #["QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"]

    ("OverlapPromptLep__QCD",{
        "procs":
        [proc+"_PromptContam" for proc in ['QCD_bEnriched']],
        "color":2,
        "name":"OverlapPromptLep__QCD",
    }),

    ("from_Others__QCD",{
        "procs":
        [proc+"_FromOthers" for proc in ['QCD_bEnriched']],
        "color":5,
        "name":"from_Others__QCD",
    }),
    ("from_bminus__QCD",{
        "procs":
        [proc+"_Frombminus" for proc in ['QCD_bEnriched']],
        "color":6,
        "name":"from_bminus__QCD",

    }),
    ("from_bplus__QCD",{
        "procs":
        [proc+"_Frombplus" for proc in ['QCD_bEnriched']],
        "color":7,
        "name":"from_bplus__QCD",
        #"IsSig":True
    }),
    
    ##-----bjet origin == Top-related -------##
    ##---separates the processes because of XSEC syst variation..
    ##--SingleTops =>SingleTop_sch/SingleTop_tch_top/SingleTop_tch_antitop/SingleTop_tW


    #1) SingleTop_sch

    ("OverlapPromptLep__SingleTop_sch",{
        "procs":
        [proc+"_PromptContam" for proc in  ["SingleTop_sch_Lep"]],
        "color":2,
        "name":"OverlapPromptLep__SingleTop_sch",
    }),

    
    ("from_Others__SingleTop_sch",{
        "procs":
        [proc+"_FromOthers" for proc in ["SingleTop_sch_Lep"]],
        "color":5,
        "name":"from_Others__SingleTop_sch",
    }),
    ("from_bminus__SingleTop_sch",{
        "procs":
        [proc+"_Frombminus" for proc in ["SingleTop_sch_Lep"]],
        "color":6,
        "name":"from_bminus__SingleTop_sch",

    }),
    ("from_bplus__SingleTop_sch",{
        "procs":
        [proc+"_Frombplus" for proc in ["SingleTop_sch_Lep"]],
        "color":7,
        "name":"from_bplus__SingleTop_sch",
        #"IsSig":True
    }),

    #2) SingleTop_tch_top
    
    ("OverlapPromptLep__SingleTop_tch_top",{
        "procs":
        [proc+"_PromptContam" for proc in  ["SingleTop_tch_top_Incl"]],
        "color":2,
        "name":"OverlapPromptLep__SingleTop_tch_top",
    }),

    
    ("from_Others__SingleTop_tch_top",{
        "procs":
        [proc+"_FromOthers" for proc in ["SingleTop_tch_top_Incl"]],
        "color":8,
        "name":"from_Others__SingleTop_tch_top",
    }),
    ("from_bminus__SingleTop_tch_top",{
        "procs":
        [proc+"_Frombminus" for proc in ["SingleTop_tch_top_Incl"]],
        "color":9,
        "name":"from_bminus__SingleTop_tch_top",
        #"IsSig":True
    }),        
    ("from_bplus__SingleTop_tch_top",{
        "procs":
        [proc+"_Frombplus" for proc in ["SingleTop_tch_top_Incl"]],
        "color":11,
        "name":"from_bplus__SingleTop_tch_top",
        #"IsSig":True
    }),        

    #3) SingleTop_tch_antitop

    ("OverlapPromptLep__SingleTop_tch_antitop",{
        "procs":
        [proc+"_PromptContam" for proc in  ["SingleTop_tch_antitop_Incl"]],
        "color":2,
        "name":"OverlapPromptLep__SingleTop_tch_antitop",
    }),

    
    ("from_Others__SingleTop_tch_antitop",{
        "procs":
        [proc+"_FromOthers" for proc in ["SingleTop_tch_antitop_Incl"]],
        "color":29,
        "name":"from_Others__SingleTop_tch_antitop",
    }),
    ("from_bminus__SingleTop_tch_antitop",{
        "procs":
        [proc+"_Frombminus" for proc in ["SingleTop_tch_antitop_Incl"]],
        "color":30,
        "name":"from_bminus__SingleTop_tch_antitop",
        #"IsSig":True
    }),        
    ("from_bplus__SingleTop_tch_antitop",{
        "procs":
        [proc+"_Frombplus" for proc in ["SingleTop_tch_antitop_Incl"]],
        "color":40,
        "name":"from_bplus__SingleTop_tch_antitop",
        #"IsSig":True
    }),        

    #4)  SingleTop_tW
    ("OverlapPromptLep__SingleTop_tW",{
        "procs":
        [proc+"_PromptContam" for proc in   ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"]],
        "color":2,
        "name":"OverlapPromptLep__SingleTop_tW",
    }),

    
    ("from_Others__SingleTop_tW",{
        "procs":
        [proc+"_FromOthers" for proc in ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"]],
        "color":41,
        "name":"from_Others__SingleTop_tW",
    }),
    ("from_bminus__SingleTop_tW",{
        "procs":
        [proc+"_Frombminus" for proc in ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"]],
        "color":45,
        "name":"from_bminus__SingleTop_tW",
        #"IsSig":True
    }),        
    ("from_bplus__SingleTop_tW",{
        "procs":
        [proc+"_Frombplus" for proc in ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"]],
        "color":38,
        "name":"from_bplus__SingleTop_tW",
        #"IsSig":True
    }),
    ##--TTbar
    #5) TTLL

    ("OverlapPromptLep__TTLL",{
        "procs":
        [proc+"_PromptContam" for proc in   ["TTLL_powheg"]],
        "color":2,
        "name":"OverlapPromptLep__TTLL",
    }),
    
    ("from_Others__TTLL",{
        "procs":
        [proc+"_FromOthers" for proc in ["TTLL_powheg"]],
        "color":2,
        "name":"from_Others__TTLL",
        #"IsSig":True
    }),
    ("from_bminus__TTLL",{
        "procs":
        [proc+"_Frombminus" for proc in ["TTLL_powheg"]],
        "color":2,
        "name":"from_bminus__TTLL",
        #"IsSig":True
    }),        
    ("from_bplus__TTLL",{
        "procs":
        [proc+"_Frombplus" for proc in ["TTLL_powheg"]],
        "color":2,
        "name":"from_bplus__TTLL",
        #"IsSig":True
    }),
    #6)TTLJ
    ("OverlapPromptLep__TTLJ",{
        "procs":
        [proc+"_PromptContam" for proc in   ["TTLJ_powheg"]],
        "color":2,
        "name":"OverlapPromptLep__TTLJ",
    }),

    
    ("from_Others__TTLJ",{
        "procs":
        [proc+"_FromOthers" for proc in   ["TTLJ_powheg"]],
        "name":"from_Others__TTLJ",
        "color":3,
        "IsSig":True
    }),

    ("from_bminus__TTLJ",{
        "procs":
        [proc+"_Frombminus" for proc in   ["TTLJ_powheg"]],
        "name":"from_bminus__TTLJ",
        "color":3,
        "IsSig":True
    }),

    ("from_bplus__TTLJ",{
        "procs":
        [proc+"_Frombplus" for proc in   ["TTLJ_powheg"]],
        "name":"from_bplus__TTLJ",
        "color":3,
        "IsSig":True
    }),        



    ("Data",{
        "procs":["Data"],
        "name":"Data",
        "IsData":True,
        "color":1,
    }),
]


