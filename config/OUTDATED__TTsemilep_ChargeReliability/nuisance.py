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
        "type":"EffTool",
        "structure":{
            ##--type
            #replica -> rms sum
            #group -> envelop among variation members in the group 
            0:{"name":"stat","nmem":20,"type":"replica"},##rms for mem
            1:{"name":"altbkg","nmem":1,"type":"group","group":"altbkg"},## envelop among all group element
            2:{"name":"altbkg2","nmem":1,"type":"group","group":"altbkg"},
            3:{"name":"altsig","nmem":1,"type":"group","group":"altsig"},
            4:{"name":"altsig2","nmem":1,"type":"group","group":"altsig"},
            5:{"name":"alttag","nmem":1,"type":"group","group":"alttag"},
            6:{"name":"alttag2","nmem":1,"type":"group","group":"alttag"},
            7:{"name":"PUweight","nmem":2,"direction":["Up","Down"]},
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
        "procs":allmc,
    },##[end] electronid
    "electronreco":{
        "info":"Electron_RECO",
        "type":"EffTool",
        "structure":{
            0:{"name":"stat","nmem":20,"type":"replica"},
            1:{"name":"altbkg","nmem":1,"type":"group","group":"algbkg"},
            2:{"name":"altbkg2","nmem":1,"type":"group","group":"algbkg"},
            3:{"name":"altsig","nmem":1,"type":"group","group":"algsig"},
            4:{"name":"altsig2","nmem":1,"type":"group","group":"algsig"},
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
        "procs":allmc,
    },

    "electrontrigger":{
        "info":"Electron_Trigger",
        "type":"EffTool",
        "structure":{
            0:{"name":"stat","nmem":20,"type":"replica"},
            1:{"name":"altbkg","nmem":1,"type":"group","group":"altbkg"},
            2:{"name":"altbkg2","nmem":1,"type":"group","group":"altbkg"},
            3:{"name":"altsig","nmem":1,"type":"group","group":"altsig"},
            4:{"name":"altsig2","nmem":1,"type":"group","group":"altsig"},
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
        "procs":allmc,
    },

    "muonreco":{
        "info":"Muon_RECO",
        "type":"EffTool",
        "structure":{
            0:{"name":"stat","nmem":20,"type":"replica"},
            1:{"name":"altbkg","nmem":1,"type":"group","group":"altbkg"},
            2:{"name":"altbkg2","nmem":1,"type":"group","group":"altbkg"},
            3:{"name":"altsig","nmem":1,"type":"group","group":"altsig"},
            4:{"name":"altsig2","nmem":1,"type":"group","group":"altsig"},
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
        "procs":allmc,
    },

    "muontrk":{
        "info":"Muon_Tracking",
        "type":"EffTool",
        "structure":{
            0:{"name":"stat","nmem":20,"type":"replica"},
            1:{"name":"altbkg","nmem":1,"type":"group","group":"altbkg"},
            2:{"name":"altbkg2","nmem":1,"type":"group","group":"altbkg"},
            3:{"name":"altsig","nmem":1,"type":"group","group":"altsig"},
            4:{"name":"altsig2","nmem":1,"type":"group","group":"altsig"},
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
        "procs":allmc,
    },


    "muonid":{
        "info":"Muon_ID",
        "type":"EffTool",
        "structure":{
            0:{"name":"stat","nmem":20,"type":"replica"},
            1:{"name":"altbkg","nmem":1,"type":"group","group":"altbkg"},
            2:{"name":"altbkg2","nmem":1,"type":"group","group":"altbkg"},
            3:{"name":"altsig","nmem":1,"type":"group","group":"altsig"},
            4:{"name":"altsig2","nmem":1,"type":"group","group":"altsig"},
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
            16:{"name":"residual","nmem":1},
        },##[end] structure
        "procs":allmc,
    },
    

    "muontrigger":{
        "info":"Muon_Trigger",
        "type":"EffTool",
        "structure":{
            0:{"name":"stat","nmem":20,"type":"replica"},
            1:{"name":"altbkg","nmem":1,"type":"group","group":"altbkg"},
            2:{"name":"altbkg2","nmem":1,"type":"group","group":"altbkg"},
            3:{"name":"altsig","nmem":1,"type":"group","group":"altsig"},
            4:{"name":"altsig2","nmem":1,"type":"group","group":"altsig"},
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
        "procs":allmc,
    },
    ##---[end] efftool
    "btaglfcorr":{
        "info":"btaglfcorr",
        "structure":{
            0:{"name":"Up","type":"group","group":"btaglfcorr"},
            1:{"name":"Down","type":"group","group":"btaglfcorr"}
        },
        "procs":allmc
    },
    "btaglfuncorr":{
        "info":"btaglfuncorr",
        "structure":{
            0:{"name":"Up","type":"group","group":"btaglfuncorr"},
            1:{"name":"Down","type":"group","group":"btaglfuncorr"}
        },
        "procs":allmc
    },
    
    "btaghfcorr":{
        "info":"btaghfcorr",
        "structure":{
            0:{"name":"Up","type":"group","group":"btaghfcorr"},
            1:{"name":"Down","type":"group","group":"btaghfcorr"},
        },
        "procs":allmc
    },

    "btaghfuncorr":{
        "info":"btaghfuncorr",
        "structure":{
            0:{"name":"Up","type":"group","group":"btaghfuncorr"},
            1:{"name":"Down","type":"group","group":"btaghfuncorr"}
        },
        "procs":allmc
    },

    "jer":{
        "info":"JER",
        "structure":{
            "Up":{"name":"Up","type":"group","group":"jer"},
            "Down":{"name":"Down","type":"group","group":"jer"}
        },
        "procs":allmc
    },
    "jesTotal":{
        "info":"JEC",
        "structure":{
            "Up":{"name":"Up","type":"group","group":"jes"},
            "Down":{"name":"Down","type":"group","group":"jes"}
        },
        "procs":allmc

    },
    "prefire":{
        "info":"prefire",

        "structure":{
            0:{"name":"Up","type":"group","group":"prefire"},
            1:{"name":"Down","type":"group","group":"prefire"}
        },
        "procs":allmc
    },
    "pu":{
        "info":"PileUp",
        "structure":{
            0:{"name":"Up","type":"group","group":"pu"},
            1:{"name":"Down","type":"group","group":"pu"}
        },
        "procs":allmc
    },
    "ps":{
        "info":"PartonShower",
        "structure":{
            0:{"name":"fsrDown","type":"group","group":"fsr"},
            1:{"name":"fsrUp","type":"group","group":"fsr"},
            2:{"name":"isrDown","type":"group","group":"isr"},
            3:{"name":"isrUp","type":"group","group":"isr"},
        },
        "procs":[p for p in allmc if p!="WJets_Sherpa"]
    },


    
}

#for p in dict_proc:
#    dict_nui["stat_"+p]={
#            "structure":["Up","Down"],
#            "type":"stat",
#    }
