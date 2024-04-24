from collections import OrderedDict
def OpenDictFile(_path):
    ret={}
    alllines=""    
    for line in open(_path,"r").readlines():
        alllines+=line
    exec("ret="+alllines)
    #print ret
    return ret
