#hadd_2016postVFP.root
import ROOT
import pickle
import os
import math
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
    def SetInputDict(self,dict_S,dict_B1,dict_B2):
        self.dict_S=dict_S
        self.dict_B1=dict_B1
        self.dict_B2=dict_B2
        #self.tree=_tree
        #                            self.dict_out[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][eventname+"_sumw2"]+= this_weight**2
        #maxMET
        #min_dphi_z_b
        #min_z_pt
        #max_ptzb
        self.grid_maxMET=[]
        self.grid_min_dphi_z_b=[]
        self.grid_min_z_pt=[]
        self.grid_max_ptzb=[]

        for d in [dict_S,dict_B1,dict_B2]:
            for maxMET in d:
                if not maxMET in self.grid_maxMET : self.grid_maxMET.append(maxMET)
                for min_dphi_z_b in d[maxMET]:
                    if not min_dphi_z_b in self.grid_min_dphi_z_b : self.grid_min_dphi_z_b.append(min_dphi_z_b)
                    for min_z_pt in d[maxMET][min_dphi_z_b]:
                        if not min_z_pt in self.grid_min_z_pt : self.grid_min_z_pt.append(min_z_pt)
                        for max_ptzb in d[maxMET][min_dphi_z_b][min_z_pt]:
                            if not max_ptzb in self.grid_max_ptzb : self.grid_max_ptzb.append(max_ptzb)

        self.grid_maxMET=sorted(self.grid_maxMET)
        self.grid_min_dphi_z_b=sorted(self.grid_min_dphi_z_b)
        self.grid_min_z_pt=sorted(self.grid_min_z_pt)
        self.grid_max_ptzb=sorted(self.grid_max_ptzb)

    def CalcSignif(self,S,S_sumw2,B1,B1_sumw2,B2,B2_sumw2):
        ####
        ##numerator = S
        ##denominator = sqrt( S+B1 + B2 + S_sumw2 + B1_sumw2 + B2_sumw2 )
        if S == 0 :
            return 0


        ret = S / math.sqrt(S + B1 + B2 + S_sumw2 + B1_sumw2 + B2_sumw2)
        return ret
    def ScanAllGrid(self):
        
        for maxMET in self.grid_maxMET:
            for min_dphi_z_b in self.grid_min_dphi_z_b:
                for min_z_pt in self.grid_min_z_pt:
                    for max_ptzb in self.grid_max_ptzb:
                        S=self.dict_S[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['S']
                        S_sumw2=self.dict_S[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['S_sumw2']
                        B1=self.dict_B1[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['B1']
                        B1_sumw2=self.dict_B1[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['B1_sumw2']                        
                        B2=self.dict_B2[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['B2']
                        B2_sumw2=self.dict_B2[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['B2_sumw2']
                        
                        signif=self.CalcSignif(S,S_sumw2,B1,B1_sumw2,B2,B2_sumw2)
                        self.dict_grid.append({"maxMET":maxMET,"min_dphi_z_b":min_dphi_z_b,"min_z_pt":min_z_pt,"max_ptzb":max_ptzb,"signif":signif})
        ##---init significance
        _S=self.dict_S[-1][0][0][-1]['S']
        _S_sumw2=self.dict_S[-1][0][0][-1]['S_sumw2']
        _B1=self.dict_B1[-1][0][0][-1]['B1']
        _B1_sumw2=self.dict_B1[-1][0][0][-1]['B1_sumw2']        
        _B2=self.dict_B2[-1][0][0][-1]['B2']
        _B2_sumw2=self.dict_B2[-1][0][0][-1]['B2_sumw2']
        self.init_signif=self.CalcSignif(_S,_S_sumw2,_B1,_B1_sumw2,_B2,_B2_sumw2)
        
    def DrawByXY(self,xname,yname):
        print("<DrawByXY>")
        print(xname,yname)
        xs = list(set([d[xname] for d in self.dict_grid if xname in d]))
        print(xs)
        ys = list(set([d[yname] for d in self.dict_grid if yname in d]))
        print(ys)
        graph = ROOT.TGraph2D()
        
        graph.SetTitle("X:"+xname+" Y:"+yname+" Z:max(Significance rel. to init.)")
        best_signif_rel=0
        best_signif=-1
        best_x=-1
        best_y=-1
        k=0
        for x in xs:
            for y in ys:
                filtered = [r for r in self.dict_grid if float(r[xname])==x and float(r[yname])==y ]        
                this_best = max(filtered, key=lambda r: r['signif'])
                this_best_signif=this_best['signif']
                this_best_signif_rel=this_best_signif/self.init_signif
                graph.SetPoint(k,x,y,this_best_signif_rel)
                if this_best_signif > best_signif:
                    best_signif=this_best_signif
                    best_signif_rel=this_best_signif_rel
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

        #print('<BEST>')
        #print(xname,best_x)
        #print(yname,best_y)
        return best_x,best_y,best_signif
    def DrawAll(self):
        #            self.dict_grid.append({"maxMET":maxMET,"min_dphi_z_b":min_dphi_z_b,"min_z_pt":min_z_pt,"max_ptzb":max_ptzb,"signif":signif})
        keylist=["maxMET","min_dphi_z_b","min_z_pt","max_ptzb"]
        dict_best={
        }
        best_signif=-1
        for i1,key1 in enumerate(keylist):
            for i2,key2 in enumerate(keylist):
                if i1 <= i2:continue
                best_x,best_y,best_signif=self.DrawByXY(key1,key2)
                if not key1 in dict_best : dict_best[key1]=best_x
                if not key2 in dict_best : dict_best[key2]=best_y
        print('<BEST>=>',best_signif)
        print('INIT->',self.init_signif)
        for key in keylist:
            print(key,dict_best[key])
def ReadPickle(path):
    print('READ->',path)
    with open(path, "rb") as f:
        this_dict = pickle.load(f)
        return this_dict


def runYear(year):
    #year="2018"
    myplot=plotter(year)
    inputpath_S="output_pickle/eventname__S__nsplit__15__"+year+".pkl"
    inputpath_B1="output_pickle/eventname__B1__nsplit__15__"+year+".pkl"
    inputpath_B2="output_pickle/eventname__B2__nsplit__70__"+year+".pkl"

    dict_S=ReadPickle(inputpath_S)
    dict_B1=ReadPickle(inputpath_B1)
    dict_B2=ReadPickle(inputpath_B2)
    
    myplot.SetInputDict(dict_S,dict_B1,dict_B2)
    myplot.ScanAllGrid()
    myplot.DrawAll()

def RunAllYear():
    years=['2016preVFP','2016postVFP','2017','2018']
    #years=['2016preVFP','2016postVFP','2017']
    for year in years:
        runYear(year)
if __name__ == '__main__':
    import sys
    year=sys.argv[1]
    runYear(year)
