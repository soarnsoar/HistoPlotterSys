import ROOT
class Plotter:
    def SetDataHist(self,_h):
        self.h_data=_h.Clone()
    def SetMCHist(self,_h):
        self.h_mc=_h.Clone()
    def SetMCStack(self,_hlist):
        self.h_stack=ROOT.THStack("","")
        for _h in _hlist:
            self.h_stack.Add(_h)
    def SetRatio(self):
        True
    def Draw(self):
        True
    def SaveAs(self):
        True
    def SetMCup(self,_h):
        True
    def SetMCdown(self,_h):
        True

