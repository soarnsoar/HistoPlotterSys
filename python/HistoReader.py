import ROOT
from collections import OrderedDict
from JHHist import JHHist
DEBUG=False
class HistoReader:
    def __init__(self):
        self.dict_h=OrderedDict()
        self.dict_hstack=OrderedDict()
        self.dict_grerr=OrderedDict()
    def Reset(self):
        #del self.dict_h
        #del self.dict_hstack
        #del self.dict_grerr
        self.dict_h=OrderedDict()
        self.dict_hstack=OrderedDict()
        self.dict_grerr=OrderedDict()
    def IsEffTool(self,_nui):
        _IsEffTool=False
        if "type" in self.dict_nui[_nui]:
            if self.dict_nui[_nui]["type"]=="EffTool": _IsEffTool=True
        return _IsEffTool

    def IsStatType(self,_nui):
        _IsStatType=False
        if "type" in self.dict_nui[_nui]:
            if self.dict_nui[_nui]["type"]=="stat": _IsStatType=True
        return _IsStatType

    def LoadWithConf(self,_filepath,_dict_nui,_dict_proc):
        self.SetInputPath(_filepath)
        self.OpenFile()
        self.SetNuisanceConf(_dict_nui)
        self.SetProcConf(_dict_proc)
        ##--ReadAll--##
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

            for nui in self.dict_nui:
                if self.IsStatType(nui):continue
                self.SetHistograms(mainp,nui,self.dict_nui[nui]['structure'],self.IsEffTool(nui))

        ##---CloseFile----##
        self.CloseFile()


    def MakeBkgShape(self,_bkglist):
        self.MakeProcCombineShape("bkg",_bkglist)
        self.MakeBkgSubShape("data-bkg","Data","bkg")
        # def MakeBkgSubShape(self,_name,_dataname,_bkgname,_coeff=-1):
        ##---Combine Variations---##
        if not "allsys" in self.dict_h["data-bkg"] : self.dict_h["data-bkg"]["allsys"]={}
        self.dict_h["data-bkg"]["allsys"]["Up"],self.dict_h["data-bkg"]["allsys"]["Down"]=self.GetTotalUpDownShape("data-bkg",sorted(self.dict_nui),True)
        
        self.dict_grerr["data-bkg"]={}
        self.dict_grerr["data-bkg"]["allsys"]=self.Convert_HistToGraphAsymErr(self.dict_h["data-bkg"]["nominal"], self.dict_h["data-bkg"]["allsys"]["Up"],self.dict_h["data-bkg"]["allsys"]["Down"])
        #def Convert_HistToGraphAsymErr(self,_h,_hup,_hdown):

    def MakeAllMCShape(self,_allmclist):
        self.MakeProcCombineShape("allmc",_allmclist)
        self.dict_hstack["allmc"]=ROOT.THStack("allmc","allmc")
        for p in _allmclist:
            self.dict_hstack["allmc"].Add(self.dict_h[p]["nominal"])
        self.SetFillColorAlphaOnly("allmc",1,0.3)
        self.MakeProcDivideShape("data/allmc","Data","allmc")
        self.MakeProcDivideShape("allmc/allmc","allmc","allmc")
        self.SetFillColorAlphaOnly("allmc/allmc",1,0.3)
    def SetHistograms(self,mainp,nui,structure,isEffTool):
        if isEffTool:
            self.SetHistogramsEffTool(mainp,nui,self.dict_nui[nui]['structure'])
        else:
            self.SetHistogramsOthers(mainp,nui,self.dict_nui[nui]['structure'])
    def GetVariations(self,nui,_proclist):
        _allvar=set([])
        for p in _proclist:
            _allvar=(_allvar | set(sorted(self.dict_h[p][nui])))

        return list(_allvar)

    def MakeProcCombineShape(self,_name,_proclist):
        ## -proc whose name is _name is sum of procs in _proclist 
        self.dict_h[_name]={}
        ##--nominal--##
        ip=0
        for p in _proclist:
            if ip==0:
                self.dict_h[_name]["nominal"]=self.dict_h[p]["nominal"].Clone()
                self.dict_h[_name]["nominal"].SetDirectory(0)
            else:
                self.dict_h[_name]["nominal"].Add(self.dict_h[p]["nominal"])
            ip+=1

        ip=0
        ##--nuiance--##
        for nui in sorted(self.dict_nui):
            if not nui in self.dict_h[_name] : self.dict_h[_name][nui]={}

            ##[if efftool type]
            if self.IsEffTool(nui):
                ## dict_h[_name][nui][iset][imem]----->histogram
                for iset in self.dict_nui[nui]["structure"]:
                    if not iset in self.dict_h[_name][nui]: self.dict_h[_name][nui][iset]={}
                    nmem=self.dict_nui[nui]["structure"][iset]["nmem"]
                    for imem in range(nmem):
                        self.dict_h[_name][nui][iset][imem]=self.GetProcCombineShapesEffTool(_proclist,nui,iset,imem)
                        
            else:
                ##---NOT efftool type
                ## dict_h[_name][nui][var]
                for var in self.dict_nui[nui]["structure"]:
                    self.dict_h[_name][nui][var]=self.GetProcCombineShapes(_proclist,nui,var)

        ##---Make stat up down
        self.SetStatUpDown(_name,"stat_"+_name)
        ##---Make total up/down shape
        self.dict_h[_name]["total"]={}
        self.dict_h[_name]["total"]["Up"],self.dict_h[_name]["total"]["Down"]=self.GetTotalUpDownShape(_name,sorted(self.dict_nui))
        self.dict_grerr[_name]={}
        self.dict_grerr[_name]["total"]=self.Convert_HistToGraphAsymErr(self.dict_h[_name]["nominal"], self.dict_h[_name]["total"]["Up"],self.dict_h[_name]["total"]["Down"])        
        #def GetTotalUpDownShape(self,_name,_nuilist,sysonly=False)
    def SetStatUpDown(self,_name,_nuiname="stat"):##Using nominal
        Nbins=self.dict_h[_name]["nominal"].GetNbinsX()
        self.dict_h[_name][_nuiname]={}
        self.dict_h[_name][_nuiname]["Up"]=self.dict_h[_name]["nominal"].Clone()
        self.dict_h[_name][_nuiname]["Up"].SetDirectory(0)
        self.dict_h[_name][_nuiname]["Down"]=self.dict_h[_name]["nominal"].Clone()
        self.dict_h[_name][_nuiname]["Down"].SetDirectory(0)
        self.dict_h[_name][_nuiname]["Up"].Reset()
        self.dict_h[_name][_nuiname]["Down"].Reset()
        for i in range(1,Nbins+1):
            y=self.dict_h[_name]["nominal"].GetBinContent(i)
            yerr=self.dict_h[_name]["nominal"].GetBinError(i)
            yup=y+yerr
            ydown=y-yerr
            if ydown<0 : ydown=0
            self.dict_h[_name][_nuiname]["Up"].SetBinContent(i,yup)
            self.dict_h[_name][_nuiname]["Down"].SetBinContent(i,ydown)
        self.dict_nui[_nuiname]={
            "structure":["Up","Down"],
            "type":"stat",
        }

        
    def MakeProcDivideShape(self,_name,_nume,_deno, fix_deno_uncertainty=True):
        ## -proc whose name is _name is _nume/_deno
        self.dict_h[_name]={}
        ##--nominal--##
        self.dict_h[_name]["nominal"]=self.dict_h[_nume]["nominal"].Clone()
        self.dict_h[_name]["nominal"].SetDirectory(0)
        ##--nominal=h_deno_with_no_staterr--##
        h_deno_with_no_staterr=self.dict_h[_deno]["nominal"].Clone()
        h_deno_with_no_staterr.SetDirectory(0)
        for i in range(1,h_deno_with_no_staterr.GetNbinsX()+1):
            h_deno_with_no_staterr.SetBinError(i,0)
        self.dict_h[_name]["nominal"].Divide(h_deno_with_no_staterr)
        
        ##--nuiance--##
        for nui in sorted(self.dict_nui):
            if not nui in self.dict_h[_name] : self.dict_h[_name][nui]={}

            ##[if efftool type]
            #if self.dict_nui[nui]["EffTool"]:
            if self.IsEffTool(nui):            
                ## dict_h[_name][nui][iset][imem]----->histogram
                for iset in self.dict_nui[nui]["structure"]:
                    if not iset in self.dict_h[_name][nui]: 
                        self.dict_h[_name][nui][iset]={}
                    nmem=self.dict_nui[nui]["structure"][iset]["nmem"]
                    for imem in range(nmem):
                        ##--if numerator has this variation
                        if nui in self.dict_h[_nume]:
                            self.dict_h[_name][nui][iset][imem]=self.dict_h[_nume][nui][iset][imem].Clone()
                            self.dict_h[_name][nui][iset][imem].SetDirectory(0)
                        else: ##if not has this var
                            self.dict_h[_name][nui][iset][imem]=self.dict_h[_nume]["nominal"].Clone()
                            self.dict_h[_name][nui][iset][imem].SetDirectory(0)

                        if fix_deno_uncertainty:
                            self.dict_h[_name][nui][iset][imem].Divide(self.dict_h[_deno]["nominal"])
                        else:
                            if nui in self.dict_h[_deno]:##if denominator has this variation
                                self.dict_h[_name][nui][iset][imem].Divide(self.dict_h[_deno][nui][iset][imem])
                            else:##if not deno has the var 
                                self.dict_h[_name][nui][iset][imem].Divide(self.dict_h[_deno]["nominal"])
                            
            else:
                ##---NOT efftool type
                ## dict_h[_name][nui][var]
                for var in self.dict_nui[nui]["structure"]:
                    if nui in self.dict_h[_nume]: ##if numerator has this var
                        self.dict_h[_name][nui][var]=self.dict_h[_nume][nui][var].Clone()
                        self.dict_h[_name][nui][var].SetDirectory(0)
                    else:##if not has this var
                        self.dict_h[_name][nui][var]=self.dict_h[_nume]["nominal"].Clone()
                        self.dict_h[_name][nui][var].SetDirectory(0)
                    if fix_deno_uncertainty:
                            self.dict_h[_name][nui][var].Divide(self.dict_h[_deno]["nominal"])
                    else:
                        if nui in self.dict_h[_deno]:##if deno has this var
                            self.dict_h[_name][nui][var].Divide(self.dict_h[_deno][nui][var])
                        else:##if deno does not have this var
                            self.dict_h[_name][nui][var].Divide(self.dict_h[_deno]["nominal"])

        ##--Make TotalSysUpDown
        #def GetSysTotalUpDownShape(self,_name,_nuilist):
        self.dict_h[_name]["allsys"]={}
        self.dict_h[_name]["allsys"]["Up"],self.dict_h[_name]["allsys"]["Down"]=self.GetTotalUpDownShape(_name,sorted(self.dict_nui),True)
        self.dict_h[_name]["total"]={}
        self.dict_h[_name]["total"]["Up"],self.dict_h[_name]["total"]["Down"]=self.GetTotalUpDownShape(_name,sorted(self.dict_nui))
        
        self.dict_grerr[_name]={}
        self.dict_grerr[_name]["allsys"]=self.Convert_HistToGraphAsymErr(self.dict_h[_name]["nominal"], self.dict_h[_name]["allsys"]["Up"],self.dict_h[_name]["allsys"]["Down"])
        self.dict_grerr[_name]["total"]=self.Convert_HistToGraphAsymErr(self.dict_h[_name]["nominal"], self.dict_h[_name]["total"]["Up"],self.dict_h[_name]["total"]["Down"])
        
    def MakeBkgSubShape(self,_name,_dataname,_bkgname,_coeff=-1):
        ##---
        #data - bkg
        self.dict_h[_name]={}
        ##--nominal--##
        self.dict_h[_name]["nominal"]=self.dict_h[_dataname]["nominal"].Clone()
        self.dict_h[_name]["nominal"].SetDirectory(0)
        self.dict_h[_name]["nominal"].Add(self.dict_h[_bkgname]["nominal"],_coeff)

        ##--nuiance--##
        for nui in sorted(self.dict_nui):
            if not nui in self.dict_h[_name] : self.dict_h[_name][nui]={}
            ##---if efftool
            if self.IsEffTool(nui):
                for iset in self.dict_nui[nui]["structure"]:
                    if not iset in self.dict_h[_name][nui]:
                        self.dict_h[_name][nui][iset]={}
                    nmem=self.dict_nui[nui]["structure"][iset]["nmem"]    
                    for imem in range(nmem):
                        self.dict_h[_name][nui][iset][imem]=self.dict_h[_dataname]["nominal"].Clone()
                        self.dict_h[_name][nui][iset][imem].SetDirectory(0)
                        self.dict_h[_name][nui][iset][imem].Add(self.dict_h[_bkgname][nui][iset][imem],_coeff)
            else:##--if not efftool
                for var in self.dict_nui[nui]["structure"]:
                    self.dict_h[_name][nui][var]=self.dict_h[_dataname]["nominal"].Clone()
                    self.dict_h[_name][nui][var].SetDirectory(0)
                    self.dict_h[_name][nui][var].Add(self.dict_h[_bkgname][nui][var],_coeff)

    def SortVariationGroup(self,_nui):
        _dict_group={}
        for iset in self.dict_nui[_nui]["structure"]:
            _HasGroup=False
            if "type" in self.dict_nui[_nui]["structure"][iset]:
                if self.dict_nui[_nui]["structure"][iset]["type"]=="group":
                    _HasGroup=True
            _groupname=""
            if _HasGroup:
                _groupname=self.dict_nui[_nui]["structure"][iset]["group"]

            else:
                _groupname=iset
            if not _groupname in _dict_group: _dict_group[_groupname]=[]
            _dict_group[_groupname].append(iset)
        return _dict_group
        
    def GetTotalUpDownShape(self,_name,_nuilist,sysonly=False):
        _h_combiner=JHHist(self.dict_h[_name]["nominal"])
        for nui in _nuilist:
            #isEffTool=self.dict_nui[nui]["EffTool"]
            if sysonly:
                if self.IsStatType(nui): continue
            isEffTool=self.IsEffTool(nui)
            if isEffTool:
                _dict_group=self.SortVariationGroup(nui)
                for group in _dict_group:
                    isReplicaType=False
                    list_iset=_dict_group[group]
                    if "type" in self.dict_nui[nui]["structure"][list_iset[0]]:
                        _this_type= self.dict_nui[nui]["structure"][list_iset[0]]["type"]
                        if _this_type=="replica":isReplicaType=True
                    if isReplicaType:
                        _hlist=[]
                        for iset in list_iset:
                            nmem=self.dict_nui[nui]["structure"][iset]["nmem"]
                            for imem in range(nmem):
                                #_h_combiner.AddSys([self.dict_h[_name][nui][iset][imem]])
                                _hlist.append(self.dict_h[_name][nui][iset][imem])
                        _hup,_hdown=_h_combiner.GetShapeReplicaAsym(_hlist)
                        _h_combiner.AddSys([_hup,_hdown])
                    else:##Envelop among all elements
                        _hlist=[]
                        for iset in list_iset:
                            nmem=self.dict_nui[nui]["structure"][iset]["nmem"]
                            for imem in range(nmem):
                                _hlist.append(self.dict_h[_name][nui][iset][imem])
                        _h_combiner.AddSys(_hlist)

            else:##--if not efftool
                ##--envelop among variations
                _hlist=[]
                for var in self.dict_nui[nui]["structure"]:
                    _hlist.append(self.dict_h[_name][nui][var])
                _h_combiner.AddSys(_hlist)
            

        return _h_combiner.hup.Clone(), _h_combiner.hdown.Clone()

    def GetProcCombineShapes(self,_proclist,_nui,_var):
        for i,p in enumerate(_proclist):
            if _nui in self.dict_h[p]:
                _hToAdd=self.dict_h[p][_nui][_var]
            else:
                _hToAdd=self.dict_h[p]["nominal"]
            if i ==0:
                hcomb=_hToAdd.Clone()
                hcomb.SetDirectory(0)
            else:
                hcomb.Add(_hToAdd)
        return hcomb.Clone()

    def GetProcCombineShapesEffTool(self,_proclist,_nui,_iset,_imem):
        for i,p in enumerate(_proclist):
            if i ==0:
                hcomb=self.dict_h[p][_nui][_iset][_imem].Clone()
            else:
                hcomb.Add(self.dict_h[p][_nui][_iset][_imem])
        return hcomb.Clone()

    #def __del__(self):
    #    #self.tfile.Close()
    #    #del self.tfile
    #    #self.Reset()
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
    def CloseFile(self):
        self.tfile.Close()
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
                self.dict_h[mainp]["nominal"]=(self.tfile.Get(this_path)).Clone()
                self.dict_h[mainp]["nominal"].SetDirectory(0)
            else:
                self.dict_h[mainp]["nominal"].Add(self.tfile.Get(this_path))
            _color=self.dict_proc[mainp]["color"]
            self.dict_h[mainp]["nominal"].SetFillColor(_color)
            self.dict_h[mainp]["nominal"].SetLineColor(_color)
            self.dict_h[mainp]["nominal"].SetMarkerColor(_color)
            if mainp.lower()=="data" : 
                self.dict_h[mainp]["nominal"].SetFillColor(0)
                self.dict_h[mainp]["nominal"].SetMarkerSize(0.5)
                self.dict_h[mainp]["nominal"].SetMarkerStyle(20)
            ip += 1
        #print mainp,type(self.dict_h[mainp]["nominal"])
        self.SetStatUpDown(mainp,"stat_"+mainp)
    def SetHistogramsEffTool(self,mainp,nui,structure):
        if not mainp in self.dict_h: self.dict_h[mainp]={}
        if not nui in self.dict_h[mainp]: self.dict_h[mainp][nui]={}
        for iset in structure:
           nmem=structure[iset]["nmem"] 
           #if not iset in self.dict_h[nui]: self.dict_h[nui][iset]={}
           for imem in range(nmem):
               suffix=str(iset)+"__"+str(imem)
               #if not suffix in self.dict_h[mainp][nui]: self.dict_h[mainp][nui]={}
               if not iset in self.dict_h[mainp][nui]:
                   self.dict_h[mainp][nui][iset]={}

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
                       self.dict_h[mainp][nui][iset][imem]=self.tfile.Get(this_path).Clone()
                       self.dict_h[mainp][nui][iset][imem].SetDirectory(0)
                   else:
                       self.dict_h[mainp][nui][iset][imem].Add(self.tfile.Get(this_path))
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
                    self.dict_h[mainp][nui][var].SetDirectory(0)
                else:
                    self.dict_h[mainp][nui][var].Add(self.tfile.Get(this_path))
                ip += 1
    
    def SetFillColorAlphaOnly(self,_proc,_color,_alpha):
        self.dict_h[_proc]["nominal"].SetFillColor(0)
        self.dict_h[_proc]["nominal"].SetLineColor(0)
        if _proc in self.dict_grerr:
            if "total" in self.dict_grerr[_proc]:
                self.dict_grerr[_proc]["total"].SetFillColorAlpha(_color,_alpha)
            if "allsys" in self.dict_grerr[_proc]:
                self.dict_grerr[_proc]["allsys"].SetFillColorAlpha(_color,_alpha)
    def Convert_HistToGraphAsymErr(self,_h,_hup,_hdown):
        N=_h.GetNbinsX()
        gr=ROOT.TGraphAsymmErrors(N+1)

        for i in range(1,N+1):
            x1=_h.GetBinLowEdge(i)
            x2=x1+_h.GetBinWidth(i)
            x=(x1+x2)/2
            y=_h.GetBinContent(i)
            yup=_hup.GetBinContent(i)
            dyup=yup-y
            ydown=_hdown.GetBinContent(i)
            dydown=y-ydown
            #if y>0:
            #    print dyup/y
            #    print dydown/y
            #print x1,x2
            gr.SetPoint(i-1,x,y)
            gr.SetPointError(i-1,x-x1,x2-x,dydown,dyup)
        return ROOT.TGraphAsymmErrors(gr)
    def GetHistDict(self):
        return self.dict_h
    def GetStackDict(self):
        return self.dict_hstack
    def GetGrErrDict(self):
        return self.dict_grerr

if __name__ == '__main__':
    from config.TTsemilep_ChargeReliability.input import dict_input
    from config.TTsemilep_ChargeReliability.nuisance import dict_nui
    from config.TTsemilep_ChargeReliability.proc import dict_proc
    from config.TTsemilep_ChargeReliability.cut_and_x import dict_cut_and_x

    _filepath=dict_input["MuonHadReliab"]
    tester=HistoReader()
    tester.SetCut("TTbarLep__bMuonInbHadPass")
    tester.SetX("bHad_pt")
    
    tester.LoadWithConf(_filepath,dict_nui,dict_proc)
    allmc=[p for p in dict_proc if p!="Data"]
    bkg=[p for p in dict_proc if p!="Data" and p!="TTLJ_bMatched" and p!="TTLJ_bbarMatched"]
    tester.MakeBkgShape(bkg)
    tester.MakeAllMCShape(allmc)

    ##---test plotter
    from Plotter import Plotter
    plotter=Plotter("test")
    plotter.SetDir("test/")
    plotter.SetHistDict(tester.GetHistDict())
    plotter.SetStackDict(tester.GetStackDict())
    plotter.SetGrErrDict(tester.GetGrErrDict())
    plotter.SetLegendList(dict_proc)

    plotter.AddHistToPad1("Data",False,"e1")
    plotter.AddHistToPad1("allmc",True,"e2")
    plotter.AddTHStackToPad1("allmc","hist")

    plotter.AddHistToPad2("data/allmc",False,"e1")
    plotter.AddHistToPad2("allmc/allmc",True,"e2")

    plotter.Draw()
    
