from math import sqrt
class JHHist:
    def __init__(self,_h):
        self.SetNominal(_h)
        self.SetUp(_h)
        self.SetDown(_h)
        self.AlwaysPositive=True
    def SetsAlwaysPositive(self,_AlwaysPositive):
        self.AlwaysPositive=_AlwaysPositive
    def SetNominal(self,_h):
        self.hnom=_h.Clone()
    def SetUp(self,_h):
        self.hup=_h.Clone()
    def SetDown(self,_h):
        self.hdown=_h.Clone()
        
    def AddSys(self,_hsyslist):##---->Take bigger one among Up /Down error
        for i in range(1,self.hnom.GetNbinsX()):
            ynom=self.hnom.GetBinContent(i)
            maxdiffup=0.
            maxdiffdown=0.
            for hsys in _hsyslist:
                ysys=hsys.GetBinContent(i)
                thisdiff=ysys-ynom
                if thisdiff>0:
                    if thisdiff > maxdiffup: maxdiffup=thisdiff
                else:
                    if thisdiff < maxdiffdown : maxdiffdown=thisdiff
                
            ##---Now calc sqrtsum of old and new err.
            yup_old=self.hup.GetBinContent(i)
            ydown_old=self.hdown.GetBinContent(i)
            dyup_old=yup_old-ynom
            dydown_old=ynom-ydown_old
            dyup=sqrt(dyup_old**2 + maxdiffup**2)
            dydown=sqrt(dydown_old**2 + maxdiffdown**2)
            yup=ynom+dyup
            ydown=ynom-dydown
            if ynom>=0 and ydown<0 and self.AlwaysPositive : ydown=0.
            self.hup.SetBinContent(i,yup)
            self.hdown.SetBinContent(i,ydown)

 
    ##---Replica Error:Asym case
    def MakeShapeReplicaAsym(self,_hsyslist):
        Nbin=self.h.GetNbinsX()
        hnom=self.hnom
        self.replicaAsymUp=hnom.Clone().Reset()
        self.replicaAsymDown=hnom.Clone().Reset()

        for ib in range(1,Nbin):
            ynom=hnom.GetBinContent(ib)
            dyup2sum=0.
            dydown2sum=0.
            for hsys in _hsyslist:
                ysys=hsys.GetBinContent(ib)
                diff=ysys-ynom
                if diff > 0:
                    dyup2sum+=diff**2
                else:
                    dydown2sum+=diff**2
            dyup=sqrt(dyup2sum)/(len(_hsyslist)-1)
            dydown=sqrt(dydown2sum)/(len(_hsyslist)-1)
            yup=ynom+dyup
            ydown=ynom-dydown
            if ynom>=0 and ydown<0 and self.AlwaysPositive:ydown=0.
            self.replicaAsymUp.SetBinContent(ib,yup)
            self.replicaAsymDown.SetBinContent(ib,ydown)
    def GetShapeReplicaAsym():
        return self.replicaAsymUp,self.replicaAsymDown

    ##---Replica Error:Sym case
    def MakeShapeReplicaSym(self,_hsyslist):
        Nbin=self.h.GetNbinsX()
        hnom=self.hnom
        self.replicaSymUp=hnom.Clone().Reset()
        self.replicaSymDown=hnom.Clone().Reset()

        for ib in range(1,Nbin):
            ynom=hnom.GetBinContent(ib)
            dy2sum=0.
            for hsys in _hsyslist:
                ysys=hsys.GetBinContent(ib)
                diff=ysys-ynom
                dy2sum+=diff**2
            dy=sqrt(dy2sum)/(len(_hsyslist)-1)
            yup=ynom+dy
            ydown=ynom-dy
            if ynom>=0 and ydown<0 and self.AlwaysPositive:ydown=0.
            self.replicaSymUp.SetBinContent(ib,yup)
            self.replicaSymDown.SetBinContent(ib,ydown)
    def GetShapeReplicaSym():
        return self.replicaSymUp, self.replicaSymDown
    ##--PDF shape
    #ref:https://arxiv.org/pdf/2203.05506.pdf
    def MakeHessianAsymShape(self,_hsyslist):
        Nbin=self.h.GetNbinsX()
        hnom=self.hnom
        self.hessianAsymUp=hnom.Clone().Reset()
        self.hessianAsymDown=hnom.Clone().Reset()

        for ib in range(1,Nbin):
            ynom=hnom.GetBinContent(ib)
            dyup2sum=0.
            dydown2sum=0.
            for hsys in _hsyslist:
                ysys=hsys.GetBinContent(ib)
                diff=ysys-ynom
                if diff > 0:
                    dyup2sum+=diff**2
                else:
                    dydown2sum+=diff**2
            dyup=sqrt(dyup2sum)
            dydown=sqrt(dydown2sum)
            yup=ynom+dyup
            ydown=ynom-dydown
            if ynom>=0 and ydown<0 and self.AlwaysPositive:ydown=0.
            self.hessianAsymUp.SetBinContent(ib,yup)
            self.hessianAsymDown.SetBinContent(ib,ydown)
    def GetHessianAsymShape():
        return self.hessianAsymUp, self.hessianAsymDown

    def MakeHessianSymShape(self,_hsyslist):
        Nbin=self.h.GetNbinsX()
        hnom=self.hnom
        self.hessianSymUp=hnom.Clone().Reset()
        self.hessianSymDown=hnom.Clone().Reset()


        for ib in range(1,Nbin):
            ynom=hnom.GetBinContent(ib)
            dy2sum=0.
            for hsys in _hsyslist:
                ysys=hsys.GetBinContent(ib)
                diff=ysys-ynom
                dy2sum+=diff**2
                
            dy=sqrt(dy2sum)
            yup=ynom+dy
            ydown=ynom-dy
            if ynom>=0 and ydown<0 and self.AlwaysPositive : ydown=0. 
            self.hessianSymUp.SetBinContent(ib,yup)
            self.hessianSymDown.SetBinContent(ib,ydown)
    def GetHessianSymShape():
        return self.hessianSymUp, self.hessianSymDown
        
