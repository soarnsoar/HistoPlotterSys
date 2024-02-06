import os
from glob import glob
exec(open("conf.py"))
#dict_out={
#    "TTsemilep_ChargeReliability":"/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/TTsemilep_ChargeReliability/"
#}

def DoCopy(name,year):
    dlist=glob(dict_out[name]+"/"+str(year)+"/RunSyst__*")
    os.system("mkdir -p "+name)
    for d in dlist:
        print d
        os.system("cp -r "+d+" "+name+"/")

if __name__ == '__main__':
    for year in [2017]:
        for name in sorted(dict_out):
            DoCopy(name,year)
    
