#hadd_2016postVFP.root
import ROOT
import os
class plotter:
    def __init__(self,year,suffix=""):
        self.year=year
        self.suffix=suffix
        self.dict_grid=[]
        self.dict_tgr={}
        self.dict_name={
            "maxMET":"max(MET)",
            "min_dphi_z_b":"min(#Delta#phi(z,b))",
            "min_z_pt":"min(pT(Z))",
            "max_ptzb":"max(pT(Z+b))"
            }
    def SetInputTree(self,_tree):
        self.tree=_tree
    def ScanAllGrid(self):
        
        for grid in self.tree:
            maxMET=grid.maxMET
            min_dphi_z_b=grid.min_dphi_z_b
            min_z_pt=grid.min_z_pt
            max_ptzb=grid.max_ptzb
            signif=grid.signif
            self.dict_grid.append({"maxMET":maxMET,"min_dphi_z_b":min_dphi_z_b,"min_z_pt":min_z_pt,"max_ptzb":max_ptzb,"signif":signif})

    def DrawByXY(self,xname,yname):
        print("<DrawByXY>")
        print(xname,yname)
        xs = list(set([d[xname] for d in self.dict_grid if xname in d]))
        print(xs)
        ys = list(set([d[yname] for d in self.dict_grid if yname in d]))
        print(ys)
        graph = ROOT.TGraph2D()
        
        graph.SetTitle("X:"+xname+" Y:"+yname+" Z:max(Significance)")
        best_signif=-1
        best_x=-1
        best_y=-1
        k=0
        for x in xs:
            for y in ys:
                filtered = [r for r in self.dict_grid if float(r[xname])==x and float(r[yname])==y ]        
                this_best = max(filtered, key=lambda r: r['signif'])
                this_best_signif=this_best['signif']
                graph.SetPoint(k,x,y,this_best_signif)
                if this_best_signif > best_signif:
                    best_signif=this_best_signif
                    best_x= x
                    best_y= y
                k+=1
        c=ROOT.TCanvas("","",800,600)
        graph.Draw("COLZ")
        graph.GetHistogram().GetXaxis().SetTitle(self.dict_name[xname])
        graph.GetHistogram().GetYaxis().SetTitle(self.dict_name[yname])

        ##---draw best auc point---##        
        pm = ROOT.TGraph()
        pm.SetPoint(0, best_x, best_y)
        pm.SetMarkerStyle(5)
        pm.SetMarkerSize(2.0)
        pm.SetMarkerColor(ROOT.kBlack)
        

        pm.Draw("Psame")
        pm.GetHistogram().GetXaxis().SetTitle(self.dict_name[xname])
        pm.GetHistogram().GetYaxis().SetTitle(self.dict_name[yname])
        os.system('mkdir -p plots/')
        c.SaveAs('plots/'+xname+"__"+yname+"__"+self.year+".pdf")

    def DrawAll(self):
        #            self.dict_grid.append({"maxMET":maxMET,"min_dphi_z_b":min_dphi_z_b,"min_z_pt":min_z_pt,"max_ptzb":max_ptzb,"signif":signif})
        keylist=["maxMET","min_dphi_z_b","min_z_pt","max_ptzb"]
        for i1,key1 in enumerate(keylist):
            for i2,key2 in enumerate(keylist):
                if i1 <= i2:continue
                self.DrawByXY(key1,key2)
def runYear(year):
    #year="2018"
    myplot=plotter(year)
    inputpath="output_hadd/hadd_"+year+".root"
    tfile=ROOT.TFile.Open(inputpath)
    ttree=tfile.Get("SignifByCuts")
    myplot.SetInputTree(ttree)
    myplot.ScanAllGrid()
    myplot.DrawAll()
if __name__ == '__main__':
    for year in ['2016preVFP','2016postVFP','2017','2018']:
        runYear(year)
