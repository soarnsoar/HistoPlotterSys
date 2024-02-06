#!/usr/bin/env python 
##---
import JHHist
import Plotter
import sys
from config.TTsemilep_ChargeReliability.input import dict_input



if __name__ == '__main__':
    ##---
    print sys.argv[0]
    ListToRun=["MuonHadReliab","MuonLepReliab",
           "ElectronHadReliab","ElectronLepReliab",
           "JetHadReliab","JetLepReliab",
           ]
    print ToRun
    for run in ListToRun:
        Plotter(run)
