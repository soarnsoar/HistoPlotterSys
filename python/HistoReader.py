import ROOT
from JHHist import JHHist
DEBUG=False
class HistoReader:
    def __init__(self):
        self.dict_h={}
    def Reset(self):
        self.dict_h={}
    def RunWithConf(self,_filepath,_dict_nui,_dict_proc):
        self.SetInputPath(_filepath)
        self.OpenFile()
        self.SetNuisanceConf(_dict_nui)
        self.SetProcConf(_dict_proc)
        for mainp in _dict_proc:
            IsData=False
            if "IsData" in _dict_proc[mainp]:
                if _dict_proc[mainp]["IsData"]:
                    IsData=True
            if IsData:
                self.SetProcs(["Data"])
            else:
                self.SetProcs(_dict_proc[mainp]["procs"])
            self.SetHistogramsNominal(mainp)
            for nui in _dict_nui:
                isEffTool=_dict_nui[nui]["EffTool"]
                if isEffTool:
                    #print "self.SetHistogramsEffTool"
                    self.SetHistogramsEffTool(mainp,nui,_dict_nui[nui]['structure'])
                else:
                    #print "self.SetHistogramsOthers"
                    self.SetHistogramsOthers(mainp,nui,_dict_nui[nui]['structure'])

    def GetVariations(self,nui,_proclist):
        _allvar=set([])
        for p in _proclist:
            #print sorted(self.dict_h[p][nui])
            _allvar=(_allvar | set(sorted(self.dict_h[p][nui])))

        return list(_allvar)
    def MakeCombineShape(self,_name,_proclist):
        self.dict_h[_name]={}
        ##--nominal--##
        ip=0
        for p in _proclist:
            if ip==0:
                self.dict_h[_name]["nominal"]=self.dict_h[p]["nominal"].Clone()
            else:
                self.dict_h[_name]["nominal"].Add(self.dict_h[p]["nominal"])
            ip+=1

        ip=0
        ##--nuiance--##
        for nui in sorted(self.dict_nui):
            #print "<MakeCombineShape>nui=",nui
            if not nui in self.dict_h[_name] : self.dict_h[_name][nui]={}
            _varlist = self.GetVariations(nui,_proclist)
            for var in _varlist:
                self.dict_h[_name][nui][var]=self.GetCombineShapes(_proclist,nui,var)

    def GetCombinedSysShape(self,_name,_nuilist):
        _h_combiner=JHHist(self.dict_h[_name]["nominal"])
        for nui in _nuilist:
           _varlist=self.GetVariations(nui,[_name])
           for var in _varlist:
               _hvar=self.dict_h[_name][nui][var]
               _h_combiner.AddSys([_hvar])

        return _h_combiner.hup, _h_combiner.hdown
    def GetCombineShapes(self,_proclist,_nui,_var):
        for i,p in enumerate(_proclist):
            #print _nui,_var,p,self.dict_h[p][_nui][_var].Integral()
            if i ==0:
                hcomb=self.dict_h[p][_nui][_var].Clone()
            else:
                hcomb.Add(self.dict_h[p][_nui][_var])
        return hcomb.Clone()
    def __del__(self):
        #self.tfile.Close()
        del self.tfile
        self.Reset()
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
    def SetProcConf(self,_dict_proc):
        self.dict_proc=_dict_proc
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
    def GetNominalShape(self,_proc):
        return self.dict_h[_proc]["nominal"]
    def GetNuisanceShape(self,_proc,_nui,_var):
        return self.dict_h[_proc][_nui][_var]

    def SetHistogramsNominal(self,mainp):
        if not mainp in self.dict_h: self.dict_h[mainp]={}
        #if not "nominal" in self.dict_h[mainp]: self.dict_h[mainp]["nominal"]={}
        ip = 0
        for p in self.procs:
            _nominal_path=self.GetHistPathBeforeNui(p)+"/nominal/0"
            if not self.IsHistExist(_nominal_path): continue
            this_path=_nominal_path
            if ip == 0:
                self.dict_h[mainp]["nominal"]=self.tfile.Get(this_path).Clone()
            else:
                self.dict_h[mainp]["nominal"].Add(self.tfile.Get(this_path).Clone())
            _color=self.dict_proc[mainp]["color"]
            self.dict_h[mainp]["nominal"].SetFillColor(_color)
            self.dict_h[mainp]["nominal"].SetLineColor(_color)
            ip += 1
    def SetHistogramsEffTool(self,mainp,nui,structure):
        if not mainp in self.dict_h: self.dict_h[mainp]={}
        if not nui in self.dict_h[mainp]: self.dict_h[mainp][nui]={}
        for iset in structure:
           nmem=structure[iset]["nmem"] 
           #if not iset in self.dict_h[nui]: self.dict_h[nui][iset]={}
           for imem in range(nmem):
               suffix=str(iset)+"__"+str(imem)
               #if not suffix in self.dict_h[mainp][nui]: self.dict_h[mainp][nui]={}
               ip = 0
               for p in self.procs:
                   _nominal_path=self.GetHistPathBeforeNui(p)+"/nominal/0"
                   if not self.IsHistExist(_nominal_path): ##if no process at this cut
                       #print p,"doesn't have nominal"
                       #print self.fpath
                       #print _nominal_path
                       #print self.cut
                       continue
                   this_path=self.GetHistPathBeforeNui(p)+"/"+nui+"/"+suffix

                   if not p in self.dict_nui[nui]["procs"]: ##no variation for this nuisance
                       this_path=self.GetHistPathBeforeNui(p)+"/nominal/0"
                   
                   #print p,nui,suffix,self.tfile.Get(this_path).Integral()
                   if ip==0:
                       self.dict_h[mainp][nui][suffix]=self.tfile.Get(this_path).Clone()
                   else:
                       self.dict_h[mainp][nui][suffix].Add(self.tfile.Get(this_path).Clone())
                   ip += 1
    def SetHistogramsOthers(self,mainp,nui,structure): ## common systematics
        if not mainp in self.dict_h: self.dict_h[mainp]={}
        if not nui in self.dict_h[mainp]: self.dict_h[mainp][nui]={}
                
        for var in structure:
            #if not var in self.dict_h[mainp][nui]: self.dict_h[mainp][nui][var]={}
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
                    self.dict_h[mainp][nui][var]=self.tfile.Get(this_path).Clone()
                else:
                    self.dict_h[mainp][nui][var].Add(self.tfile.Get(this_path).Clone())
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

