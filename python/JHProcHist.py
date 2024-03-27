import ROOT
class JHProcHist:## Hists Container of a proc
    def __init__(self,cut,x,proc):
        self.cut=cut
        self.x=x
        self.proc=proc
        self.hdict={}

    def SetX(self,x):
        self.x=x
    def SetProc(self,proc):
        self.proc=proc
    def SetCut(self,cut):
        self.cut=cut

    def GetX(self):
        return self.x
    def GetProc(self):
        return self.proc
    def GetCut(self)
        return self.cut

    def SetHist(self,h,sys,idx1,idx2):
        idx1=str(idx1)
        idx2=str(idx2)
        if not sys in self.hdict:
            self.hdict[sys]={}
        if not idx1 in self.hdict[sys]:
            self.hdict[sys][idx1]={}
        self.hdict[sys][idx1][idx2]=h.Clone()
    def GetHist(self,sys="norm",idx1=0,idx2=0):
        if not sys in self.hdict:##No hist for this sys
            return self.hdict["norm"][0][0]
        if not idx1 in self.hdict[sys]:
            return self.hdict["norm"][0][0]
        if not idx2 in self.hdict[sys][idx1]:
            return self.hdict["norm"][0][0]

        return self.hdict[sys][idx1][idx2]
    def GetSysList(self):
        return sorted(hdict)
    def GetSysIdx1List(self,sys):
        if not sys in hdict:
            return []
        return sorted(hdict[sys])
    def GetSysIdx2List(self,sys,idx1):
        if not sys in hdict:
            return []
        if not idx1 in hdict[sys]:
            return []
        return sorted(hdict[sys][idx1])
    def GetCombinedList(self,list1,list2):
        return list(set(list1,list2))
    def Divide(self, h2, cut="",x="",proc=""):
        h_over_h2=JHProcHist(cut,x,proc)
        this_syslist=GetCombinedList(self.GetSysList()+h2.GetSysList())
        for this_sys in this_syslist:
            this_idx1list=GetCombinedList(self.GetSysIdx1List()+h2.GetSysIdx1List())
            for this_idx1 in this_idx1list:
                this_idx2list=GetCombinedList(self.GetSysIdx2List()+h2.GetSysIdx2List())
                for this_idx2 in this_idx2list:
                    this_shape=self.GetHist(this_sys,this_idx1,this_idx2).Clone()
                    this_shape.Divide(h2.GetHist(this_sys,this_idx1,this_idx2))
                    h_over_h2.SetList(this_shape,this_sys,this_idx1,this_idx2)
        return h_over_h2
    
    def Subtract(self,h2,cut="",x="",proc=""):
        h_minus_h2=JHProcHist(cut,x,proc)
        this_syslist=GetCombinedList(self.GetSysList()+h2.GetSysList())
        for this_sys in this_syslist:
            this_idx1list=GetCombinedList(self.GetSysIdx1List()+h2.GetSysIdx1List())
            for this_idx1 in this_idx1list:
                this_idx2list=GetCombinedList(self.GetSysIdx2List()+h2.GetSysIdx2List())
                for this_idx2 in this_idx2list:
                    this_shape=self.GetHist(this_sys,this_idx1,this_idx2).Clone()
                    this_shape.Add(h2.GetHist(this_sys,this_idx1,this_idx2),-1)
                    h_minus_h2.SetList(this_shape,this_sys,this_idx1,this_idx2)
        return h_minus_h2

    def Combine(self,h2,cut="",x="",proc=""):
        h_plus_h2=JHProcHist(cut,x,proc)
        this_syslist=GetCombinedList(self.GetSysList()+h2.GetSysList())
        for this_sys in this_syslist:
            this_idx1list=GetCombinedList(self.GetSysIdx1List()+h2.GetSysIdx1List())
            for this_idx1 in this_idx1list:
                this_idx2list=GetCombinedList(self.GetSysIdx2List()+h2.GetSysIdx2List())
                for this_idx2 in this_idx2list:
                    this_shape=self.GetHist(this_sys,this_idx1,this_idx2).Clone()
                    this_shape.Add(h2.GetHist(this_sys,this_idx1,this_idx2))
                    h_plus_h2.SetList(this_shape,this_sys,this_idx1,this_idx2)
        return h_plus_h2
    

    def MakeStatNuiShapes(self):
        nui_name_base="__".join(["stat",self.GetCut(),self.GetX(),self.GetProc()])
        ##--Get NuisanceShape
        h=self.GetHist()
        Nbin=h.GetNbinsX()
        for i in range(1,Nbin+1):
            nui_name=nui_name_base+"__bin"+str(i)
            y=h.GetBinContent(i)
            yerr=h.GetBinError(i)
            yup=y+yerr
            ydown=y-yerr if y > yerr else 0.
            hup=h.Clone(h.GetName()+nui_name+"Up")
            hdown=h.Clone(h.GetName()+nui_name+"Down")
            
            self.SetHist(hup,nui_name,i,"Up")
            self.SetHist(hdown,nui_name,i,"Down")
        
