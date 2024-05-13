from GetBinsX import GetBinsX
from copy import deepcopy
from OpenDictFile import OpenDictFile
import ROOT
from math import sqrt
class JHProcHist:## Hists Container of a proc
    def __init__(self,cut,x,proc):
        self.cut=cut
        self.x=x
        self.proc=proc
        self.hdict={}
        self.IsErrorSet=False
        self.nmin_replica=10 ## # of members for replica sys.
        self.nmaxprint=5
    def Scale(self,norm):
        for sys in self.hdict:
            for idx1 in self.hdict[sys]:
                for idx2 in self.hdict[sys][idx1]:
                    self.hdict[sys][idx1][idx2].Scale(norm)
        True
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
    def GetCut(self):
        return self.cut

    def SetHist(self,h,sys="nom",idx1=0,idx2=0):
        idx1=str(idx1)
        idx2=str(idx2)
        if not sys in self.hdict:
            self.hdict[sys]={}
        if not idx1 in self.hdict[sys]:
            self.hdict[sys][idx1]={}
        self.hdict[sys][idx1][idx2]=deepcopy(h)

    def GetHist(self,sys="nom",idx1=0,idx2=0):
        idx1=str(idx1)
        idx2=str(idx2)
        if not sys in self.hdict:##No hist for this sys
            return self.hdict["nom"]['0']['0']
        if not idx1 in self.hdict[sys]:
            return self.hdict["nom"]['0']['0']
        if not idx2 in self.hdict[sys][idx1]:
            return self.hdict["nom"]['0']['0']

        return self.hdict[sys][idx1][idx2]
    def GetSysList(self):
        return sorted(self.hdict)
    def GetSysIdx1List(self,sys):
        if not sys in self.hdict:
            return []
        return sorted(self.hdict[sys])
    def GetSysIdx2List(self,sys,idx1):
        if not sys in self.hdict:
            return []
        if not idx1 in self.hdict[sys]:
            return []
        return sorted(self.hdict[sys][idx1])
    def GetCombinedList(self,list1,list2):
        return list(set(list1+list2))
    def Divide(self, h2, cut="",x="",proc=""):
        h_over_h2=JHProcHist(cut,x,proc)
        this_syslist=self.GetCombinedList(self.GetSysList(),h2.GetSysList())
        for this_sys in this_syslist:
            this_idx1list=self.GetCombinedList(self.GetSysIdx1List(this_sys),h2.GetSysIdx1List(this_sys))
            for this_idx1 in this_idx1list:
                this_idx2list=self.GetCombinedList(self.GetSysIdx2List(this_sys,this_idx1),h2.GetSysIdx2List(this_sys,this_idx1))
                for this_idx2 in this_idx2list:
                    this_shape=deepcopy(self.GetHist(this_sys,this_idx1,this_idx2))
                    this_shape.Divide(h2.GetHist(this_sys,this_idx1,this_idx2))
                    h_over_h2.SetHist(this_shape,this_sys,this_idx1,this_idx2)
        return h_over_h2
    def MakeBinErrorZero(self):
        Nbins=self.hdict["nom"]['0']['0'].GetNbinsX()
        for i in range(Nbins+2):
            self.hdict["nom"]['0']['0'].SetBinError(i,0.0)

    def Subtract(self,h2,cut="",x="",proc=""):
        h_minus_h2=JHProcHist(cut,x,proc)
        this_syslist=self.GetCombinedList(self.GetSysList(),h2.GetSysList())
        for this_sys in this_syslist:
            this_idx1list=self.GetCombinedList(self.GetSysIdx1List(this_sys),h2.GetSysIdx1List(this_sys))
            for this_idx1 in this_idx1list:
                this_idx2list=self.GetCombinedList(self.GetSysIdx2List(this_sys,this_idx1),h2.GetSysIdx2List(this_sys,this_idx1))
                for this_idx2 in this_idx2list:
                    this_shape=deepcopy(self.GetHist(this_sys,this_idx1,this_idx2))
                    this_shape.Add(h2.GetHist(this_sys,this_idx1,this_idx2),-1)
                    h_minus_h2.SetHist(this_shape,this_sys,this_idx1,this_idx2)
        return h_minus_h2

    def Combine(self,h2,cut="",x="",proc=""):
        h_plus_h2=JHProcHist(cut,x,proc)
        this_syslist=self.GetCombinedList(self.GetSysList(),h2.GetSysList())
        for this_sys in this_syslist:
            this_idx1list=self.GetCombinedList(self.GetSysIdx1List(this_sys),h2.GetSysIdx1List(this_sys))
            for this_idx1 in this_idx1list:
                this_idx2list=self.GetCombinedList(self.GetSysIdx2List(this_sys,this_idx1),h2.GetSysIdx2List(this_sys,this_idx1))
                for this_idx2 in this_idx2list:
                    this_shape=deepcopy(self.GetHist(this_sys,this_idx1,this_idx2))
                    this_shape.Add(h2.GetHist(this_sys,this_idx1,this_idx2))
                    h_plus_h2.SetHist(this_shape,this_sys,this_idx1,this_idx2)

        ##--Check--##
        this_syslist=self.GetCombinedList(self.GetSysList(),h2.GetSysList())
        for this_sys in this_syslist:
            this_idx1list=self.GetCombinedList(self.GetSysIdx1List(this_sys),h2.GetSysIdx1List(this_sys))
            for this_idx1 in this_idx1list:
                this_idx2list=self.GetCombinedList(self.GetSysIdx2List(this_sys,this_idx1),h2.GetSysIdx2List(this_sys,this_idx1))
                for this_idx2 in this_idx2list:
                    if h_plus_h2.GetHist().Integral()>0:
                        if h_plus_h2.GetHist(this_sys,this_idx1,this_idx2).Integral()/h_plus_h2.GetHist().Integral()>2:
                            print "[Combine]"
                            print "nom"
                            print h_plus_h2.GetHist().Integral()
                            print this_sys,this_idx1,this_idx2
                            print h_plus_h2.GetHist(this_sys,this_idx1,this_idx2).Integral()
        return h_plus_h2

    def Clone(self,h2):
        this_syslist=h2.GetSysList()
        for this_sys in this_syslist:
            this_idx1list=h2.GetSysIdx1List(this_sys)
            for this_idx1 in this_idx1list:
                this_idx2list=h2.GetSysIdx2List(this_sys,this_idx1)
                for this_idx2 in this_idx2list:
                    this_shape=deepcopy(h2.GetHist(this_sys,this_idx1,this_idx2))
                    self.SetHist(this_shape,this_sys,this_idx1,this_idx2)
                
    def SetEffTool(self,dict_efftool):
        self.dict_efftool=dict_efftool
    def SetFillColor(self,_color):
        self.hdict["nom"]['0']['0'].SetFillColor(_color)
    def SetLineColor(self,_color):
        self.hdict["nom"]['0']['0'].SetLineColor(_color)
    def MakeStatNuiShapes(self,add_suffix=""):
        nui_name_base="__".join(["stat",self.GetCut(),self.GetX(),self.GetProc(),add_suffix])
        ##--Get NuisanceShape
        h=self.GetHist()
        Nbin=h.GetNbinsX()
        for i in range(1,Nbin+1):
            nui_name=nui_name_base+"__bin"+str(i)
            y=h.GetBinContent(i)
            yerr=h.GetBinError(i)
            yup=y+yerr
            ydown=y-yerr if y > yerr else 0.
            hup=deepcopy(h)
            hup.SetName(h.GetName()+nui_name+"Up")
            hup.SetBinContent(i,yup)
            hdown=deepcopy(h)
            hdown.SetName(h.GetName()+nui_name+"Down")
            hdown.SetBinContent(i,ydown)            
            self.SetHist(hup,nui_name,i,"Up")
            self.SetHist(hdown,nui_name,i,"Down")
        
    def Get_dy(self,ibin,sys,idx1,idx2):
        hsys=self.GetHist(sys,idx,idx2)
        ysys=hsys.GetBinContent(ibin)
        ynom=self.GetHist().GetBinContent(ibin)
        return ysys-ynom
    def GetReplicaError(self,ynom,ibin,sys,idx1):
        ##---Split them into plus/minus error
        Nrep_plus=0
        Nrep_minus=0
        sum_dyplus2=0
        sum_dyminus2=0
        xvalue=self.hdict[sys][idx1]["0"].GetBinLowEdge(ibin)
        for idx2 in self.hdict[sys][idx1]:
            ysys=self.hdict[sys][idx1][idx2].GetBinContent(ibin)
            this_dy=ysys-ynom
            if this_dy > 0:
                sum_dyplus2+=(this_dy**2)
                Nrep_plus+=1
            else:
                sum_dyminus2+=(this_dy**2)
                Nrep_minus+=1
            #sum_dy2+=(this_dy**2)
        
        variance_plus=sum_dyplus2/Nrep_plus if Nrep_plus else 0.
        variance_minus=sum_dyminus2/Nrep_minus if Nrep_minus else 0.
        std_dev_plus=sqrt(variance_plus)
        std_dev_minus=sqrt(variance_minus)
        return std_dev_plus,std_dev_minus
    def GetDiffError(self,ynom,ibin,sys,idx1):
        dylist_plus=[0]
        dylist_minus=[0]
        for idx2 in self.hdict[sys][idx1]:
            ysys=self.hdict[sys][idx1][idx2].GetBinContent(ibin)
            this_dy=ysys-ynom
            if this_dy > 0:
                dylist_plus.append(this_dy)
            else:
                dylist_minus.append(this_dy)
        #maxdy=max(dylist)
        #mindy=min(dylist)
        return max(dylist_plus),min(dylist_minus)
    def GetSysError(self,ynom,ibin,sys):
        sum_err2_plus=0
        sum_err2_minus=0
        for idx1 in self.hdict[sys]:
            #if sys in self.dict_efftool and idx1 in self.dict_efftool[sys]:
            if len(self.hdict[sys][idx1]) > self.nmin_replica :##if number of mem > 10 -> replica
                this_err_plus, this_err_minus=self.GetReplicaError(ynom,ibin,sys,idx1)
            else:
                this_err_plus, this_err_minus=self.GetDiffError(ynom,ibin,sys,idx1)
            sum_err2_plus+= (this_err_plus**2)
            sum_err2_minus+= (this_err_minus**2)
        total_err_plus=sqrt(sum_err2_plus)
        total_err_minus=sqrt(sum_err2_minus)
        return total_err_plus,total_err_minus

    

    def SetErrorBand(self):
        self.gr_sys=ROOT.TGraphAsymmErrors()
        hnom=self.GetHist()
        Nbin=hnom.GetNbinsX()
        dict_err_plus={}
        dict_err_minus={}
        integral_total=0
        for ibin in range(1,Nbin+1):
            x1=hnom.GetBinLowEdge(ibin)
            x2=hnom.GetBinWidth(ibin)+x1
            x=(x1+x2)/2
            ynom=hnom.GetBinContent(ibin)
            integral_total+=ynom
            dy2sum_plus=0
            dy2sum_minus=0
            #print "----"
            #print ynom
            for sys in self.hdict:
                dy_plus,dy_minus=self.GetSysError(ynom,ibin,sys)
                dy2sum_plus+=(dy_plus**2)
                dy2sum_minus+=(dy_minus**2)
                if sys not in dict_err_plus: 
                    dict_err_plus[sys]=0
                if sys not in dict_err_minus: 
                    dict_err_minus[sys]=0
                dict_err_plus[sys]+=dy_plus
                dict_err_minus[sys]+=dy_minus
            dytotal_plus=sqrt(dy2sum_plus)
            dytotal_minus=sqrt(dy2sum_minus)
            self.gr_sys.SetPoint(ibin-1,x,ynom)
            self.gr_sys.SetPointError(ibin-1,x-x1,x2-x,dytotal_plus,dytotal_minus)
        ##----Print 
        print "----[Plus Error Rank]---"
        self.PrintSysRank(dict_err_plus,integral_total)
        print "----[Minus Error Rank]---"
        self.PrintSysRank(dict_err_minus,integral_total)
        self.IsErrorSet=1
    def GetErrorGraph(self):
        #if not self.IsErrorSet: self.SetErrorBand()
        self.SetErrorBand()
        return self.gr_sys
    def PrintSysRank(self,dict_err,integral_total):
        sorted_keys = sorted(dict_err, key=dict_err.get, reverse=True)
        #sorted_dict = {key: dict_err[key] for key in sorted_keys}
        idx_sys=0
        print "Proc=",self.proc
        for sys in sorted_keys:
            idx_sys+=1
            dy=dict_err[sys]
            relerr=0
            if not integral_total == 0 : relerr=dy/integral_total*100
            print '[',idx_sys,']',sys,round(relerr,3),"(%)"
            if idx_sys>self.nmaxprint:break

