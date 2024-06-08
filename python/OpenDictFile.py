import ROOT
from collections import OrderedDict
def OpenDictFile(_path):
    ret=OrderedDict()
    alllines=""    
    for line in open(_path,"r").readlines():
        alllines+=line
    if alllines.startswith("["):
        exec("ret=OrderedDict("+alllines+")")
    else:
        exec("ret="+alllines)
    return ret
    
