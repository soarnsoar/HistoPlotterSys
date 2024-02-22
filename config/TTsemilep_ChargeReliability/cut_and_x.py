dict_cut_and_x={
    "MuonHadReliab":{
        "TTbarLep":["Thad_M","bHad_eta","bHad_pt"],
        "TTbarLep__bMuonInbHadFail":["Thad_M","bHad_eta","bHad_pt"],
        "TTbarLep__bMuonInbHadPass":["Thad_M","bHad_eta","bHad_pt","bmuon_in_bHad_eta","bmuon_in_bHad_pt"],
    },

    "MuonLepReliab":{
        "TTbarLep":["MT_LeptonicTop","bLep_eta","bLep_pt"],
        "TTbarLep__bMuonInbLepFail":["MT_LeptonicTop","bLep_eta","bLep_pt"],
        "TTbarLep__bMuonInbLepPass":["MT_LeptonicTop","bLep_eta","bLep_pt","bmuon_in_bLep_eta","bmuon_in_bLep_pt"],
    },
}
dict_eff_cut_and_x={
    "MuonHadReliab":[
        {
            "nume":["TTbarLep__bMuonInbHadPass","Thad_M"],
            "deno":["TTbarLep","Thad_M"]
        },

        {
            "nume":["TTbarLep__bMuonInbHadPass","bHad_eta"],
            "deno":["TTbarLep","bHad_eta"]
        },
        {
            "nume":["TTbarLep__bMuonInbHadPass","bHad_pt"],
            "deno":["TTbarLep","bHad_pt"]
        },
    ],

    "MuonLepReliab":[
        {
            "nume":["TTbarLep__bMuonInbLepPass","MT_LeptonicTop"],
            "deno":["TTbarLep","MT_LeptonicTop"]
        },

        {
            "nume":["TTbarLep__bMuonInbLepPass","bLep_eta"],
            "deno":["TTbarLep","bLep_eta"]
        },
        {
            "nume":["TTbarLep__bMuonInbLepPass","bLep_pt"],
            "deno":["TTbarLep","bLep_pt"]
        },
    ],
    
    
}
    #"ElectronHadReliab":{
    #    "TTbarLep__bElectronInbHadPass":["Thad_M","bHad_eta","bHad_pt","belectron_in_bHad_eta","belectron_in_bHad_pt"],
    #},
    #"JetHadReliab":{
    #    "TTbarLep__bHadPass":["Thad_M","bHad_eta","bHad_pt"],
    #    "TTbarLep__bHadFail":["Thad_M","bHad_eta","bHad_pt"],
    #},
    #}
