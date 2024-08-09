##
import json
from collections import OrderedDict
class ConfMaker:
    def __init__(self,bname,CH_TTLJ,chargeType):
        self.bname=bname
        self.CH_TTLJ=CH_TTLJ
        self.chargeType=chargeType
        self.doNewBinning=0
        self.doYmax=0
        self.MakeCutName()
    def GetOtherB(self):
        if "bLep"==self.bname:return "bHad"
        if "bHad"==self.bname:return "bLep"
    def MakeCutName(self):
        ##let chargeType : muon, muon-,electron,electron-,jet,poorjet
        self.deno=[]
        self.nume=[]

        if self.chargeType == "muon":
            self.deno=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftMuonChargeNotOpposite", self.CH_TTLJ+"_TTLJ__"+self.bname+"_FailSoftMuon", self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftMuonChargeUseOpposite"]
            self.nume=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftMuonChargeNotOpposite"]
        elif chargeType=="muon-":
            self.deno=[self.CH_TTLJ+"_TTLJ__"+self.bname+"_FailSoftMuon",self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftMuonChargeUseOpposite"]
            self.nume=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftMuonChargeUseOpposite"]
        elif chargeType=="electron":
            self.deno=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftElectronChargeNotOpposite",self.CH_TTLJ+"_TTLJ__"+self.bname+"_FailSoftMuon__FailSoftElectron",self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftElectronChargeUseOpposite"]
            self.nume=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftElectronChargeNotOpposite"]
        elif chargeType=="electron-":
            self.deno=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftElectronChargeUseOpposite",self.CH_TTLJ+"_TTLJ__"+self.bname+"_FailSoftMuon__FailSoftElectron"]
            self.nume=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingSoftElectronChargeUseOpposite"]
        elif chargeType=="jet":
            self.deno=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingGoodJetCharge",self.CH_TTLJ+"_TTLJ__"+self.bname+"_FailSoftMuon__FailSoftElectron__FailGoodBJet"]
            self.nume=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingGoodJetCharge"]
        elif chargeType=="poor_jet":
            self.deno=[self.CH_TTLJ+"_TTLJ__"+self.bname+"UsingGoodJetCharge",self.CH_TTLJ+"_TTLJ__"+self.bname+"_FailSoftMuon__FailSoftElectron__FailGoodBJet"]
            self.nume=[self.CH_TTLJ+"_TTLJ__"+self.bname+"_FailSoftMuon__FailSoftElectron__FailGoodBJet"]

    def AddRebin(self,newbinning):
        self.newbinning=newbinning
        self.doNewBinning=1
    def SetX(self,x_deno,x_nume):
        self.x_deno=x_deno
        self.x_nume=x_nume
    def SetYmax(self,ymax):
        self.ymax=ymax
        self.doYmax=1
    def GetRegionName(self):
        suffix="Charge"
        if "-" in self.chargeType: suffix="OppositeCharge"
        return "Use"+self.chargeType+suffix
    def SetSigBkg(self):
        self.sig=[self.bname+"CandFrom bquark","All bCand From bquark"]
        self.bkg=["Not From bquark",self.GetOtherB()+"CandFrom bquark"]
    def GetDict(self):
        self.SetSigBkg()

        #outdict=OrderedDict()
        self.plotname=self.bname+"_"+self.x_deno+"__"+self.GetRegionName()
        outdict={
            "deno":{
                "x":self.x_deno,
                "cut":self.deno,
            },

            "nume":{
                "x":self.x_nume,
                "cut":self.nume,
            },
            "sig":self.sig,
            "bkg":self.bkg,            
            
        }
        if self.doYmax: 
            outdict["ymax"]=self.ymax
        if self.doNewBinning: 
            outdict["xbins"]=self.newbinning

        return outdict

bnames=["bLep","bHad"]
CH_TTLJ=["AllLep","Muon","Electron"]
chargeTypes=["muon","muon-","electron","electron-","jet","poor_jet"]

binnings={
    "pt":[30,40,50,60,70,80,90,100,120,140,160,180,200,300,1000],
    "eta":[-2.4,-2.2,-2.0,-1.8,-1.6,-1.4,-1.2,-1.0, -0.8,-0.6,-0.4,-0.2, 0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4],
}
ymax={
    "poor_jet":1.0,
    "jet":1.0,
    "muon":0.2,
    "muon-":0.05,
    "electron":0.2,
    "electron-":0.05,
}
xlist=["pt","eta"]


total_dict={}
for bname in bnames:
    for lep in CH_TTLJ:
        for chargeType in chargeTypes:
            for x  in xlist:
                this_conf=ConfMaker(bname,lep,chargeType)
                if x in binnings: this_conf.AddRebin(binnings[x])
                this_conf.SetYmax(ymax[chargeType])
                fullx=bname+"_"+x

                this_conf.SetX(fullx,fullx)
                #print this_conf.GetDict()
                total_dict[this_conf.plotname]=this_conf.GetDict()

##export
f=open("eff_def.py","w")
json.dump(total_dict,f,indent=4)
#f.write(str(total_dict))
#f.close()
