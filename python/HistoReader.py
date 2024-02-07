import ROOT
DEBUG=False
class HistoReader:
    def __init__(self):
        self.dict_h={}
    def Reset(self):
        self.dict_h={}
    def SetInputPath(self,_path):
        self.fpath=_path
    def SetProcs(self,_procs):
        self.procs=_procs
        #TTbarLep__bHadFail/Thad_M/TTLL_powheg/btaglfcorr
    def SetCut(self,_cut):
        self.cut=_cut
    def SetX(self,_x):
        self.x=_x
    def SetNuisanceConf(self,_dict_nui):
        self.dict_nui=_dict_nui
    def OpenFile(self):
        self.tfile=ROOT.TFile.Open(self.fpath)
        if DEBUG : print self.fpath
    def GetHistPathBeforeNui(self,_p):
        return self.cut+"/"+self.x+"/"+_p
    def IsHistExist(self,_path):
        if not self.tfile.Get(_path):
            if DEBUG:
                print "fail to get ",_path
                print'IN'
                print self.fpath
            return False
        else:
            return True
    def SetHistogramsNominal(self):
        if not "nominal" in self.dict_h: self.dict_h["nominal"]={}
        ip = 0
        for p in self.procs:
            _nominal_path=self.GetHistPathBeforeNui(p)+"/nominal/0"
            if not self.IsHistExist(_nominal_path): continue
            this_path=_nominal_path
            if ip == 0:
                self.dict_h["nominal"]=self.tfile.Get(this_path).Clone()
            else:
                self.dict_h["nominal"].Add(self.tfile.Get(this_path).Clone())
            ip += 1
    def SetHistogramsEffTool(self,nui,structure):
        if not nui in self.dict_h: self.dict_h[nui]={}
        for iset in structure:
           nmem=structure[iset]["nmem"] 
           #if not iset in self.dict_h[nui]: self.dict_h[nui][iset]={}
           for imem in range(nmem):
               suffix=str(iset)+"__"+str(imem)
               if not suffix in self.dict_h[nui]: self.dict_h[nui]={}
               ip = 0
               for p in self.procs:
                   _nominal_path=self.GetHistPathBeforeNui(p)+"/nominal/0"
                   if not self.IsHistExist(_nominal_path): ##if no process at this cut
                       continue
                   this_path=self.GetHistPathBeforeNui(p)+"/"+nui+"/"+suffix
                   if not p in self.dict_nui[nui]["procs"]: ##no variation for this nuisance
                       this_path=self.GetHistPathBeforeNui(p)+"/nominal/0"
                   if ip==0:
                       self.dict_h[nui][suffix]=self.tfile.Get(this_path).Clone()
                   else:
                       self.dict_h[nui][suffix].Add(self.tfile.Get(this_path).Clone())
                   ip += 1
    def SetHistogramsOthers(self,nui,structure): ## common systematics
        if not nui in self.dict_h: self.dict_h[nui]={}
        for var in structure:
            if not var in self.dict_h[nui]: self.dict_h[nui][var]={}
            ip = 0
            for p in self.procs:
                _nominal_path=self.GetHistPathBeforeNui(p)+"/nominal/0"
                if not self.IsHistExist(_nominal_path): ##if no process at this cut
                    continue
                this_path=self.GetHistPathBeforeNui(p)+"/"+nui+"/"+str(var)
                if not p in self.dict_nui[nui]["procs"]: ##no variation for this nuisance
                    this_path=_nominal_path
                if DEBUG : print this_path
                #self.tfile.Get(self.GetHistPathTillNui(p)).ls()
                if ip==0:
                    self.dict_h[nui][var]=self.tfile.Get(this_path).Clone()
                else:
                    self.dict_h[nui][var].Add(self.tfile.Get(this_path).Clone())
                ip += 1
if __name__ == '__main__':
    tester=HistoReader()
    tester.SetInputPath("../SKFlatOutput/TTsemilep_ChargeReliability/RunSyst__RunJet__RunHadronSide__RunChAcc__/combine.root")
    tester.OpenFile()    
    tester.SetProcs(["QCD_bEnriched_HT200to300"])
    tester.SetCut("TTbarLep__bHadFail")
    tester.SetX("Thad_M")
    #tester.SetNuisance("electronid")
    #tester.SetHistogramsWithSetMem(0,20)
    tester.SetNuisance("btaglfcorr")
    tester.SetHistograms(2)
    c=ROOT.TCanvas()
    #for i in range(20):
    for i in range(2):
        tester.dict_h[i].Draw()
        c.SaveAs("test"+str(i)+".pdf")

