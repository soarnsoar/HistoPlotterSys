def GetBinsX(h):
    N=h.GetNbinsX()
    xbins=[]
    for i in range(1,N+2):
        xbins.append(h.GetBinLowEdge(i))
    return xbins
