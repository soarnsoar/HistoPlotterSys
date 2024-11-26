{
    "XSEC_TopMass_TT":{##
        "nuisanceName":"XSEC_TopMass",
        "ref":"https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO",
        "sample_keys":["TTLJ_powheg","TTLL_powheg","TTJJ_powheg"], ##if a sample name has one of this keys, apply the uncertainty
        "exception":[],
        #Mass uncert. up / down only
        "up":1.0 - 22.5/833.9,
        "down":1.0 + 23.2/833.9,        
    },


    "XSEC_TopMass_ST_sch":{##
        "nuisanceName":"XSEC_TopMass",
        "ref":"https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_s_channel_cross_secti",
        "sample_keys":["SingleTop_sch"], ##if a sample name has one of this keys, apply the uncertainty
        "exception":[],

        "up":1.0 - 0.12/5.24 , ## Mass uncert= 0.12
        "down":1.0 + 0.12/5.24
    },


    "XSEC_TopMass_ST_tch_top":{##NNLO
        "nuisanceName":"XSEC_TopMass",
        "ref":"https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_t_channel_cross",
        "sample_keys":["SingleTop_tch_top"], ##if a sample name has one of this keys, apply the uncertainty
        "exception":[],
        ##Mass uncert. up / down	 -1.2 / +1.0
        "up":(1.0- 1.2/134.2),
        "down":(1.0 +1.0/134.2)
    },


    "XSEC_TopMass_ST_tch_antitop":{##NNLO
        "nuisanceName":"XSEC_TopMass",
        "ref":"https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_t_channel_cross",
        "sample_keys":["SingleTop_tch_antitop"], ##if a sample name has one of this keys, apply the uncertainty
        "exception":[],
        ##Mass uncert. up / down	 -0.7 / +0.7
        "up":(1.0- 0.7/80.0) ,
        "down":(1.0 +0.7/80.0)
    },
    
    
    "XSEC_TopMass_ST_tW":{##NNLO, tW top + antitop
        "nuisanceName":"XSEC_TopMass",
        "ref":"https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Single_top_quark_tW_channel_cros",
        #"ref":"https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect",
        "sample_keys":["SingleTop_tW"], ##if a sample name has one of this keys, apply the uncertainty
        "exception":[],
        ##Mass uncert. up / down	 -0.7 / +0.7
        "up":(1.0- 1.2/79.3) ,
        "down":(1.0 +1.2/79.3)
    },


    "XSEC_QCD":{##
        "nuisanceName":"XSEC_QCD",
        #"ref":"https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV",
        "sample_keys":["QCD_bEnriched"], ##if a sample name has one of this keys, apply the uncertainty
        "exception":[],
        ##
        "up":1.3 ,
        "down":0.7
    },


    
}
