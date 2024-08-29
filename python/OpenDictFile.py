import ROOT
from collections import OrderedDict
import os


def OpenDictFile(_path):
    maindir=os.getenv("GIT_HistoPlotterSys")
    ret=OrderedDict()
    alllines=""    
    for line in open(_path,"r").readlines():
        alllines+=line
    if alllines.startswith("["):
        exec("ret=OrderedDict("+alllines+")")
    else:
        exec("ret="+alllines)
    return ret
    
