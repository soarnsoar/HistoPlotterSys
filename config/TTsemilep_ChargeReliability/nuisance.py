from proc import dict_proc
allmc=[]
for p in dict_proc:
    if "IsData" in dict_proc[p]:
        if dict_proc[p]["IsData"] : continue
    allmc+=dict_proc[p]["procs"]
allmc=list(set(allmc))   
dict_nui={
    ##----
    "electronid":{
        "info":"Electron_MediumID",
        "EffTool":True,
        "structure":{
            0:{"name":"stat","nmem":20,},
            1:{"name":"altbkg","nmem":1,},
            2:{"name":"altbkg2","nmem":1,},
            3:{"name":"altsig","nmem":1,},
            4:{"name":"altsig2","nmem":1,},
            5:{"name":"alttag","nmem":1,},
            6:{"name":"alttag2","nmem":1,},
            7:{"name":"PUweight","nmem":2,},
            8:{"name":"prefireweight","nmem":2,"direction":["Up","Down"]},
            9:{"name":"zptweight","nmem":1,},
            10:{"name":"z0weight","nmem":1,},
            11:{"name":"fitrange","nmem":2,"direction":["Up","Down"]},
            12:{"name":"countrange","nmem":2,"direction":["Up","Down"]},
            13:{"name":"nmassbin","nmem":2,"direction":["Up","Down"]},
            14:{"name":"genmatching","nmem":1,},
            15:{"name":"fitting","nmem":1,},
            16:{"name":"altsub","nmem":1,},
            17:{"name":"pTbelow20","nmem":1,},
            18:{"name":"residual","nmem":1,},
        },##[end] structure
        "procs":allmc
    },##[end] electronid
    "electronreco":{
        "info":"Electron_RECO",
        "EffTool":True,
        "structure":{
            0:{"name":"stat","nmem":20},
            1:{"name":"altbkg","nmem":1},
            2:{"name":"altbkg2","nmem":1},
            3:{"name":"altsig","nmem":1},
            4:{"name":"altsig2","nmem":1},
            5:{"name":"alttag","nmem":1},
            6:{"name":"altmc","nmem":1},
            7:{"name":"PUweight","nmem":2,"direction":["Up","Down"]},
            8:{"name":"prefireweight","nmem":2,"direction":["Up","Down"]},
            9:{"name":"zptweight","nmem":1},
            10:{"name":"z0weight","nmem":1},
            11:{"name":"fitrange","nmem":2,"direction":["Up","Down"]},
            12:{"name":"countrange","nmem":2,"direction":["Up","Down"]},
            13:{"name":"nmassbin","nmem":2,"direction":["Up","Down"]},
            14:{"name":"genmatching","nmem":1},
            15:{"name":"fitting","nmem":1},
            16:{"name":"altsub","nmem":1},
        },##[end] structure
        "procs":allmc
    },

    "electrontrigger":{
        "info":"Electron_Trigger",
        "EffTool":True,
        "structure":{
            0:{"name":"stat","nmem":20},
            1:{"name":"altbkg","nmem":1},
            2:{"name":"altbkg2","nmem":1},
            3:{"name":"altsig","nmem":1},
            4:{"name":"altsig2","nmem":1},
            5:{"name":"alttag","nmem":1},
            6:{"name":"altmc","nmem":1},
            7:{"name":"PUweight","nmem":2,"direction":["Up","Down"]},
            8:{"name":"prefireweight","nmem":2,"direction":["Up","Down"]},
            9:{"name":"zptweight","nmem":1},
            10:{"name":"z0weight","nmem":1},
            11:{"name":"fitrange","nmem":2,"direction":["Up","Down"]},
            12:{"name":"countrange","nmem":2,"direction":["Up","Down"]},
            13:{"name":"nmassbin","nmem":2,"direction":["Up","Down"]},
            14:{"name":"genmatching","nmem":1},
            15:{"name":"fitting","nmem":1},
            16:{"name":"altsub","nmem":1},
        },##[end] structure
        "procs":allmc
    },

    "muonreco":{
        "info":"Muon_RECO",
        "EffTool":True,
        "structure":{
            0:{"name":"stat","nmem":20},
            1:{"name":"altbkg","nmem":1},
            2:{"name":"altbkg2","nmem":1},
            3:{"name":"altsig","nmem":1},
            4:{"name":"altsig2","nmem":1},
            5:{"name":"alttag","nmem":1},
            6:{"name":"altmc","nmem":1},
            7:{"name":"PUweight","nmem":2,"direction":["Up","Down"]},
            8:{"name":"prefireweight","nmem":1},
            9:{"name":"zptweight","nmem":1},
            10:{"name":"z0weight","nmem":1},
            11:{"name":"fitrange","nmem":2},
            12:{"name":"countrange","nmem":2,"direction":["Up","Down"]},
            13:{"name":"nmassbin","nmem":2,"direction":["Up","Down"]},
            14:{"name":"genmatching","nmem":1},
            15:{"name":"fitting","nmem":1},
        },##[end] structure
        "procs":allmc
    },

    "muontrk":{
        "info":"Muon_Tracking",
        "EffTool":True,
        "structure":{
            0:{"name":"stat","nmem":20},
            1:{"name":"altbkg","nmem":1},
            2:{"name":"altbkg2","nmem":1},
            3:{"name":"altsig","nmem":1},
            4:{"name":"altsig2","nmem":1},
            5:{"name":"alttag","nmem":1},
            6:{"name":"altmc","nmem":1},
            7:{"name":"PUweight","nmem":2,"direction":["Up","Down"]},
            8:{"name":"prefireweight","nmem":2,"direction":["Up","Down"]},
            9:{"name":"zptweight","nmem":1},
            10:{"name":"z0weight","nmem":1},
            11:{"name":"fitrange","nmem":2,"direction":["Up","Down"]},
            12:{"name":"countrange","nmem":2,"direction":["Up","Down"]},
            13:{"name":"nmassbin","nmem":2,"direction":["Up","Down"]},
            14:{"name":"genmatching","nmem":1},
            15:{"name":"fitting","nmem":1},
        },##[end] structure
        "procs":allmc
    },


    "muonid":{
        "info":"Muon_ID",
        "EffTool":True,
        "structure":{
            0:{"name":"stat","nmem":20},
            1:{"name":"altbkg","nmem":1},
            2:{"name":"altbkg2","nmem":1},
            3:{"name":"altsig","nmem":1},
            4:{"name":"altsig2","nmem":1},
            5:{"name":"alttag","nmem":1},
            6:{"name":"altmc","nmem":1},
            7:{"name":"PUweight","nmem":2,"direction":["Up","Down"]},
            8:{"name":"prefireweight","nmem":2},
            9:{"name":"zptweight","nmem":1},
            10:{"name":"z0weight","nmem":1},
            11:{"name":"fitrange","nmem":2,"direction":["Up","Down"]},
            12:{"name":"countrange","nmem":2,"direction":["Up","Down"]},
            13:{"name":"nmassbin","nmem":2,"direction":["Up","Down"]},
            14:{"name":"genmatching","nmem":1},
            15:{"name":"fitting","nmem":1},
            16:{"name":"residual","nmem":1},
        },##[end] structure
        "procs":allmc
    },
    

    "muontrigger":{
        "info":"Muon_Trigger",
        "EffTool":True,
        "structure":{
            0:{"name":"stat","nmem":20},
            1:{"name":"altbkg","nmem":1},
            2:{"name":"altbkg2","nmem":1},
            3:{"name":"altsig","nmem":1},
            4:{"name":"altsig2","nmem":1},
            5:{"name":"alttag","nmem":1},
            6:{"name":"altmc","nmem":1},
            7:{"name":"PUweight","nmem":2,"direction":["Up","Down"]},
            8:{"name":"prefireweight","nmem":2,"direction":["Up","Down"]},
            9:{"name":"zptweight","nmem":1},
            10:{"name":"z0weight","nmem":1},
            11:{"name":"fitrange","nmem":2,"direction":["Up","Down"]},
            12:{"name":"countrange","nmem":2,"direction":["Up","Down"]},
            13:{"name":"nmassbin","nmem":2,"direction":["Up","Down"]},
            14:{"name":"genmatching","nmem":1},
            15:{"name":"fitting","nmem":1},
            
        },##[end] structure
        "procs":allmc
    },
    ##---[end] efftool
    "btaglfcorr":{
        "info":"btaglfcorr",
        "EffTool":0,
        "structure":{
            0:{"name":"Up"},
            1:{"name":"Down"}
        },
        "procs":allmc
    },
    "btaglfuncorr":{
        "info":"btaglfuncorr",
        "EffTool":0,
        "structure":{
            0:{"name":"Up"},
            1:{"name":"Down"}
        },
        "procs":allmc
    },
    
    "btaghfuncorr":{
        "info":"btaglfuncorr",
        "EffTool":0,
        "structure":{
            0:{"name":"Up"},
            1:{"name":"Down"}
        },
        "procs":allmc
    },

    "btaghfuncorr":{
        "info":"btaglfuncorr",
        "EffTool":0,
        "structure":{
            0:{"name":"Up"},
            1:{"name":"Down"}
        },
        "procs":allmc
    },

    "jer":{
        "info":"JER",
        "EffTool":0,
        "structure":{
            "Up":{"name":"Up"},
            "Down":{"name":"Down"}
        },
        "procs":allmc
    },
    "jesTotal":{
        "info":"JEC",
        "EffTool":0,
        "structure":{
            "Up":{"name":"Up"},
            "Down":{"name":"Down"}
        },
        "procs":allmc

    },
    "prefire":{
        "info":"prefire",
        "EffTool":0,
        "structure":{
            0:{"name":"Up"},
            1:{"name":"Down"}
        },
        "procs":allmc
    },
    "pu":{
        "info":"PileUp",
        "EffTool":0,
        "structure":{
            0:{"name":"Up"},
            1:{"name":"Down"}
        },
        "procs":allmc
    },
    "ps":{
        "info":"PartonShower",
        "EffTool":0,
        "structure":{
            0:{"name":"fsrDown"},
            1:{"name":"fsrUp"},
            2:{"name":"isrDown"},
            3:{"name":"isrUp"},
        },
        "procs":[p for p in allmc if p!="WJets_Sherpa"]
    },


    
}
