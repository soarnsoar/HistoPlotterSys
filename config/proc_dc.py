[
    ##-----bjet origin == NON Top Bkgs-----##
    ("from_Others__OtherProc",{
        "procs":
        [bkg+"_From"+p+"__HadronOthers" for bkg in ["WW_pythia","WZ_pythia","ZZ_pythia"]+["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO","WJets_MG"] for p in ["bminus","bplus","Others"]] +\
        [bkg+"_From"+p+"__HadronB" for bkg in ["WW_pythia","WZ_pythia","ZZ_pythia"]+["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO","WJets_MG"] for p in ["Others"]],
        "color":2,
        "name":"from_Others__OtherProc",
    }),


    ("from_bminus__OtherProc",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["WW_pythia","WZ_pythia","ZZ_pythia"]+["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO","WJets_MG"] for p in ["bminus"]],
        "color":3,
        "name":"from_bminus__OtherProc",

    }),

    ("from_bplus__OtherProc",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["WW_pythia","WZ_pythia","ZZ_pythia"]+["DYJetsToEE_MiNNLO","DYJetsToMuMu_MiNNLO","DYJetsToTauTau_MiNNLO","WJets_MG"] for p in ["bplus"]],
        "color":3,
        "name":"from_bplus__OtherProc",

    }),

    #0) QCD processes
    #["QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"]
    ("from_Others__QCD",{
        "procs":
        [bkg+"_From"+p+"__HadronOthers" for bkg in ["QCD_bEnriched_HT100to200","QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"]  for p in ["bminus","bplus","Others"]]+\
        [bkg+"_From"+p+"__HadronB" for bkg in ["QCD_bEnriched_HT100to200","QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"]  for p in ["Others"]],
        "color":5,
        "name":"from_Others__QCD",
    }),
    ("from_bminus__QCD",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["QCD_bEnriched_HT100to200","QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"]  for p in ["bminus"]],
        "color":6,
        "name":"from_bminus__QCD",

    }),
    ("from_bplus__QCD",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["QCD_bEnriched_HT100to200","QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"] for p in ["bplus"]],
        "color":7,
        "name":"from_bplus__QCD",
        #"IsSig":True
    }),
    
    ##-----bjet origin == Top-related -------##
    ##---separates the processes because of XSEC syst variation..
    ##--SingleTops =>SingleTop_sch/SingleTop_tch_top/SingleTop_tch_antitop/SingleTop_tW


    #1) SingleTop_sch
    ("from_Others__SingleTop_sch",{
        "procs":
        [bkg+"_From"+p+"__HadronOthers" for bkg in ["SingleTop_sch_Lep"] for p in ["bminus","bplus","Others"]]+\
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_sch_Lep"] for p in ["Others"]],
        "color":5,
        "name":"from_Others__SingleTop_sch",
    }),
    ("from_bminus__SingleTop_sch",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_sch_Lep"] for p in ["bminus"]],
        "color":6,
        "name":"from_bminus__SingleTop_sch",

    }),
    ("from_bplus__SingleTop_sch",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_sch_Lep"] for p in ["bplus"]],
        "color":7,
        "name":"from_bplus__SingleTop_sch",
        #"IsSig":True
    }),

    #2) SingleTop_tch_top
    ("from_Others__SingleTop_tch_top",{
        "procs":
        [bkg+"_From"+p+"__HadronOthers" for bkg in ["SingleTop_tch_top_Incl"] for p in ["bminus","bplus","Others"]]+\
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tch_top_Incl"] for p in ["Others"]],
        "color":8,
        "name":"from_Others__SingleTop_tch_top",
    }),
    ("from_bminus__SingleTop_tch_top",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tch_top_Incl"] for p in ["bminus"]],
        "color":9,
        "name":"from_bminus__SingleTop_tch_top",
        #"IsSig":True
    }),        
    ("from_bplus__SingleTop_tch_top",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tch_top_Incl"] for p in ["bplus"]],
        "color":11,
        "name":"from_bplus__SingleTop_tch_top",
        #"IsSig":True
    }),        
    #3) SingleTop_tch_antitop
    ("from_Others__SingleTop_tch_antitop",{
        "procs":
        [bkg+"_From"+p+"__HadronOthers" for bkg in ["SingleTop_tch_antitop_Incl"] for p in ["bminus","bplus","Others"]]+\
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tch_antitop_Incl"] for p in ["Others"]],
        "color":29,
        "name":"from_Others__SingleTop_tch_antitop",
    }),
    ("from_bminus__SingleTop_tch_antitop",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tch_antitop_Incl"] for p in ["bminus"]],
        "color":30,
        "name":"from_bminus__SingleTop_tch_antitop",
        #"IsSig":True
    }),        
    ("from_bplus__SingleTop_tch_antitop",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tch_antitop_Incl"] for p in ["bplus"]],
        "color":40,
        "name":"from_bplus__SingleTop_tch_antitop",
        #"IsSig":True
    }),        

    #4)  SingleTop_tW
    ("from_Others__SingleTop_tW",{
        "procs":
        [bkg+"_From"+p+"__HadronOthers" for bkg in ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"] for p in ["bminus","bplus","Others"]]+\
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"] for p in ["Others"]],
        "color":41,
        "name":"from_Others__SingleTop_tW",
    }),
    ("from_bminus__SingleTop_tW",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"] for p in ["bminus"]],
        "color":45,
        "name":"from_bminus__SingleTop_tW",
        #"IsSig":True
    }),        
    ("from_bplus__SingleTop_tW",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"] for p in ["bplus"]],
        "color":38,
        "name":"from_bplus__SingleTop_tW",
        #"IsSig":True
    }),
    ##--TTbar
    #5) TTLL
    ("from_Others__TTLL",{
        "procs":
        [bkg+"_From"+p+"__HadronOthers" for bkg in ["TTLL_powheg"] for p in ["bminus","bplus","Others"]]+\
        [bkg+"_From"+p+"__HadronB" for bkg in ["TTLL_powheg"] for p in ["Others"]],
        "color":2,
        "name":"from_Others__TTLL",
        #"IsSig":True
    }),
    ("from_bminus__TTLL",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["TTLL_powheg"] for p in ["bminus"]],
        "color":2,
        "name":"from_bminus__TTLL",
        #"IsSig":True
    }),        
    ("from_bplus__TTLL",{
        "procs":
        [bkg+"_From"+p+"__HadronB" for bkg in ["TTLL_powheg"] for p in ["bplus"]],
        "color":2,
        "name":"from_bplus__TTLL",
        #"IsSig":True
    }),
    #6)TTLJ 
    ("from_Others__TTLJ",{
        "procs":["TTLJ_powheg_From"+p+"__HadronOthers" for p in ["bminus","bplus","Others"]]+\
        ["TTLJ_powheg_From"+p+"__HadronB" for p in ["Others"]],
        "name":"from_Others__TTLJ",
        "color":3,
        "IsSig":True
    }),

    ("from_bminus__TTLJ",{
        "procs":["TTLJ_powheg_From"+p+"__HadronB" for p in ["bminus"]],
        "name":"from_bminus__TTLJ",
        "color":3,
        "IsSig":True
    }),

    ("from_bplus__TTLJ",{
        "procs":["TTLJ_powheg_From"+p+"__HadronB" for p in ["bplus"]],
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


