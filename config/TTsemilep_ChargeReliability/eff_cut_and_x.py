dict_eff_cut_and_x={
    "CompareHadLep":{
        "bjet_eta":{
            "MuonHadReliab":{##eff definition
                "nume_cut":"TTbarLep__bMuonInbHadPass",
                "nume_x":"bHad_eta",
                "deno_cut":"TTbarLep__bMuonInbHadFail",
                "deno_x":"bHad_eta",
            },
            "MuonLepReliab":{##eff definition
                "nume_cut":"TTbarLep__bMuonInbLepPass",
                "nume_x":"bLep_eta",
                "deno_cut":"TTbarLep__bMuonInbLepFail",
                "deno_x":"bLep_eta",
            },

            "ElectronHadReliab":{##eff definition
                "nume_cut":"TTbarLep__bElectronInbHadPass",
                "nume_x":"bHad_eta",
                "deno_cut":"TTbarLep__bElectronInbHadFail",
                "deno_x":"bHad_eta",
            },
            "ElectronLepReliab":{##eff definition
                "nume_cut":"TTbarLep__bElectronInbLepPass",
                "nume_x":"bLep_eta",
                "deno_cut":"TTbarLep__bElectronInbLepFail",
                "deno_x":"bLep_eta",
            },

            "JetHadReliab":{##eff definition
                "nume_cut":"TTbarLep__bHadPass",
                "nume_x":"bHad_eta",
                "deno_cut":"TTbarLep__bHadFail",
                "deno_x":"bHad_eta",
            },
            "JetLepReliab":{##eff definition
                "nume_cut":"TTbarLep__bLepPass",
                "nume_x":"bLep_eta",
                "deno_cut":"TTbarLep__bLepFail",
                "deno_x":"bLep_eta",
            },


            
            
        },
        "bjet_pt":{
            "MuonHadReliab":{##eff definition
                "nume_cut":"TTbarLep__bMuonInbHadPass",
                "nume_x":"bHad_pt",
                "deno_cut":"TTbarLep__bMuonInbHadFail",
                "deno_x":"bHad_pt",
            },
            "MuonLepReliab":{##eff definition
                "nume_cut":"TTbarLep__bMuonInbLepPass",
                "nume_x":"bLep_pt",
                "deno_cut":"TTbarLep__bMuonInbLepFail",
                "deno_x":"bLep_pt",
            },

            "ElectronHadReliab":{##eff definition
                "nume_cut":"TTbarLep__bElectronInbHadPass",
                "nume_x":"bHad_pt",
                "deno_cut":"TTbarLep__bElectronInbHadFail",
                "deno_x":"bHad_pt",
            },
            "ElectronLepReliab":{##eff definition
                "nume_cut":"TTbarLep__bElectronInbLepPass",
                "nume_x":"bLep_pt",
                "deno_cut":"TTbarLep__bElectronInbLepFail",
                "deno_x":"bLep_pt",
            },

            "JetHadReliab":{##eff definition
                "nume_cut":"TTbarLep__bHadPass",
                "nume_x":"bHad_pt",
                "deno_cut":"TTbarLep__bHadFail",
                "deno_x":"bHad_pt",
            },
            "JetLepReliab":{##eff definition
                "nume_cut":"TTbarLep__bLepPass",
                "nume_x":"bLep_pt",
                "deno_cut":"TTbarLep__bLepFail",
                "deno_x":"bLep_pt",
            },


        }
    },
    "CompareDatasubMC":{
        "MuonHadReliab":{
            "bHad_eta":{##eff definition
                "nume_cut":"TTbarLep__bMuonInbHadPass",
                "nume_x":"bHad_eta",
                "deno_cut":"TTbarLep__bMuonInbHadFail",
                "deno_x":"bHad_eta",
            },
            "bHad_pt":{##eff definition
                "nume_cut":"TTbarLep__bMuonInbHadPass",
                "nume_x":"bHad_pt",
                "deno_cut":"TTbarLep__bMuonInbHadFail",
                "deno_x":"bHad_pt",
            },
        },
        
        "MuonLepReliab":{##eff definition
            "bLep_eta":{
                "nume_cut":"TTbarLep__bMuonInbLepPass",
                "nume_x":"bLep_eta",
                "deno_cut":"TTbarLep__bMuonInbLepFail",
                "deno_x":"bLep_eta",
            },
            "bLep_pt":{
                "nume_cut":"TTbarLep__bMuonInbLepPass",
                "nume_x":"bLep_pt",
                "deno_cut":"TTbarLep__bMuonInbLepFail",
                "deno_x":"bLep_pt",
            },
        },

        ##
        "ElectronHadReliab":{
            "bHad_eta":{##eff definition
                "nume_cut":"TTbarLep__bElectronInbHadPass",
                "nume_x":"bHad_eta",
                "deno_cut":"TTbarLep__bElectronInbHadFail",
                "deno_x":"bHad_eta",
            },
            "bHad_pt":{##eff definition
                "nume_cut":"TTbarLep__bElectronInbHadPass",
                "nume_x":"bHad_pt",
                "deno_cut":"TTbarLep__bElectronInbHadFail",
                "deno_x":"bHad_pt",
            },
        },
        
        "ElectronLepReliab":{##eff definition
            "bLep_eta":{
                "nume_cut":"TTbarLep__bElectronInbLepPass",
                "nume_x":"bLep_eta",
                "deno_cut":"TTbarLep__bElectronInbLepFail",
                "deno_x":"bLep_eta",
            },
            "bLep_pt":{
                "nume_cut":"TTbarLep__bElectronInbLepPass",
                "nume_x":"bLep_pt",
                "deno_cut":"TTbarLep__bElectronInbLepFail",
                "deno_x":"bLep_pt",
            },
        },
        ##
        "JetHadReliab":{
            "bHad_eta":{##eff definition
                "nume_cut":"TTbarLep__bHadPass",
                "nume_x":"bHad_eta",
                "deno_cut":"TTbarLep__bHadFail",
                "deno_x":"bHad_eta",
            },
            "bHad_pt":{##eff definition
                "nume_cut":"TTbarLep__bHadPass",
                "nume_x":"bHad_pt",
                "deno_cut":"TTbarLep__bHadFail",
                "deno_x":"bHad_pt",
            },
        },
        
        "JetLepReliab":{##eff definition
            "bLep_eta":{
                "nume_cut":"TTbarLep__bLepPass",
                "nume_x":"bLep_eta",
                "deno_cut":"TTbarLep__bLepFail",
                "deno_x":"bLep_eta",
            },
            "bLep_pt":{
                "nume_cut":"TTbarLep__bLepPass",
                "nume_x":"bLep_pt",
                "deno_cut":"TTbarLep__bLepFail",
                "deno_x":"bLep_pt",
            },
        },

    }            

}
    #"ElectronHadReliab":{
    #    "TTbarLep__bElectronInbHadPass":["Thad_M","bHad_eta","bHad_pt","belectron_in_bHad_eta","belectron_in_bHad_pt"],
    #},
    #"JetHadReliab":{
    #    "TTbarLep__bHadPass":["Thad_M","bHad_eta","bHad_pt"],
    #    "TTbarLep__bHadFail":["Thad_M","bHad_eta","bHad_pt"],
    #},
    #}
