class Plotter:
    def SetDataHist(self,_h):
        self.h_data=_h.Clone()
    def SetMCHist(self,_h):
        self.h_mc=_h.Clone()
    def SetMCStack(self,_h):
        self._h_stack=_h.Clone()
    def SetRatio(self):
        True
    def Draw(self):
        True
    def SaveAs(self):
        True

