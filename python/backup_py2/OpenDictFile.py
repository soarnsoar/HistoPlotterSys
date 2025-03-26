import ROOT
from collections import OrderedDict
import os


def OpenDictFile(_path,YEAR=""):

    maindir=os.getenv("GIT_HistoPlotterSys")
    ret=OrderedDict()
    alllines=""    
    for line in open(_path,"r").readlines():
        if "__YEAR__" in line : line=line.replace("__YEAR__",str(YEAR))
        alllines+=line
    if alllines.startswith("["):
        exec("ret=OrderedDict("+alllines+")")
    else:
        exec("ret="+alllines)
    return ret
    
