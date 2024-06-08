import ROOT
from collections import OrderedDict 
class datacard:
    def __init__(self,binname):
        self.binname=binname
        self.dict_sig=OrderedDict()
        self.dict_bkg=OrderedDict()
        self.dict_nuisance=OrderedDict()
    def AddObs(self,ydata):
        self.obs=ydata
    def AddSignal(self,name,rate,n_unweight,AddMCstat=True):
        self.dict_sig[name]={"rate":rate,"n_unweight":n_unweight}
        if AddMCstat:
            _statnuiname="mcstat__"+self.binname+"__"+name
            _nuitype="gmN "+str(n_unweight)
            _alpha=rate/n_unweight
            _dict_proc_factor={name:_alpha}
            self.AddNuisance(_statnuiname,_nuitype,_dict_proc_factor)
    def AddBkg(self,name,rate,n_unweight,AddMCstat=True):
        self.dict_bkg[name]={"rate":rate,"n_unweight":n_unweight}
        if AddMCstat:
            _statnuiname="mcstat__"+self.binname+"__"+name
            _nuitype="gmN "+str(n_unweight)
            _alpha=rate/n_unweight
            _dict_proc_factor={name:_alpha}
            self.AddNuisance(_statnuiname,_nuitype,_dict_proc_factor)        
    def AddNuisance(self,nuiname,nuitype,dict_proc_factor):
        self.dict_nuisance[nuiname]={
            "type":nuitype,
            "proc_factor":dict_proc_factor
        }
    def ExportCard(self):
        self.MakeCard()
        self.Save()

    def MakeCard(self):
        ##----setup some variables----##
        nsig=len(self.dict_sig)
        nbkg=len(self.dict_bkg)
        mclist=list(self.dict_sig)+list(self.dict_bkg)
        mcratelist=[]
        for sig in self.dict_sig:
            _rate=self.dict_sig[sig]["rate"]
            mcratelist.append(_rate)
        for bkg in self.dict_bkg:
            _rate=self.dict_bkg[bkg]["rate"]
            mcratelist.append(_rate)

        self.imax=1
        self.jmax=nsig+nbkg-1
        self.kmax="*"

        ##---datacard contents---##
        
        ##---basic lines ,obs and rates
        self.lines=[]
        self.lines.append("imax "+str(self.imax)+"  number of channels")
        self.lines.append("jmax "+str(self.jmax)+"  number of processes minus 1")
        self.lines.append("kmax "+str(self.kmax)+"  number of nuisance parameters (sources of systematical uncertainties")
        self.lines.append("-------------")
        self.lines.append("bin         "+self.binname)
        self.lines.append("observation         "+str(self.obs))
        self.lines.append("-------------")
        self.lines.append("bin              "+"  ".join([self.binname]*(self.jmax+1)))
        self.lines.append("process          "+"  ".join(mclist))
        self.lines.append("process          "+"  ".join([str(i) for i in range(1-nsig,self.jmax+2-nsig)]))
        self.lines.append("rate             "+"  ".join(str(rate) for rate in mcratelist))
        ##--nuisance lines
        for nui in self.dict_nuisance:
            nuitype=self.dict_nuisance[nui]["type"]
            nuiname=nui
            factorlist=[]
            for mc in mclist:
                if mc in self.dict_nuisance[nui]["proc_factor"]:
                    factor=self.dict_nuisance[nui]["proc_factor"][mc]
                else:
                    factor="-"
                factorlist.append(str(factor))
            ##--add a line for this nui
            self.lines.append(nui+"  "+nuitype+"   "+"  ".join(factorlist))
        
    def Save(self):
        filename=self.binname+".txt"
        print "CreateCard -->",filename
        f=open(filename,"w")
        for line in self.lines:
            f.write(line+"\n")
        f.close()
    
if __name__ == "__main__":
    testbin=datacard("testcard")
    testbin.AddObs(117241)
    testbin.AddSignal("DYbbar",18476.6155959,41811)
    testbin.AddSignal("DYbevt",32185.2180621,72890)
    testbin.AddBkg("DYothers",60585.6027818,135532)
    testbin.AddBkg("Bkg",5993.5849478,172592)
    testbin.AddNuisance("QCDscale","lnN",{"DYbbar":1.1, "DYbevt":1.1, "DYothers":1.1, "Bkg":1.1})
    testbin.AddNuisance("BkgNorm","lnN",{"Bkg":1.2})
    testbin.AddNuisance("Efficiency","lnN",{"DYbbar":1.05, "DYbevt":1.05, "DYothers":1.05, "Bkg":1.05})
    testbin.ExportCard()
