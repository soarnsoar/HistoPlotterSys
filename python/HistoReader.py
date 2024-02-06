import ROOT
class HistoReader:
    def __init__(self):
        self.SetNuisance("nominal")
    def SetInputPath(self,_path):
        self.fpath=_path
    def SetProcs(self,_procs):
        self.procs=_procs
        #TTbarLep__bHadFail/Thad_M/TTLL_powheg/btaglfcorr
    def SetCut(self,_cut):
        self.cut=_cut
    def SetX(self,_x):
        self.x=_x
    def SetNuisance(self,_nui):
        self.nui=_nui
    def OpenFile(self):
        self.tfile=ROOT.TFile.Open(self.fpath)
    def GetHistPathTillNui(self,_p):
        return self.cut+"/"+self.x+"/"+_p+"/"+self.nui+"/"
    def SetHistogramsWithSetMem(self,iset,nmem):
        self.dict_h={}
        for imem in range(nmem):
            #self.dict_h[iset][imem]={}
            for ip,p in enumerate(self.procs):
                if ip==0:
                    this_path=self.GetHistPathTillNui(p)+str(iset)+"__"+str(imem)
                    self.dict_h[imem]=self.tfile.Get(this_path).Clone()
                else:
                    self.dict_h[imem].Add(self.tfile.Get(this_path).Clone())
        
    def SetHistograms(self,n): ## common systematics
        self.dict_h={}
        for i in range(n):
            #self.dict_h[iset][imem]={}
            for ip,p in enumerate(self.procs):
                if ip==0:
                    this_path=self.GetHistPathTillNui(p)+str(i)
                    self.dict_h[i]=self.tfile.Get(this_path).Clone()
                else:
                    self.dict_h[i].Add(self.tfile.Get(this_path).Clone())
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

