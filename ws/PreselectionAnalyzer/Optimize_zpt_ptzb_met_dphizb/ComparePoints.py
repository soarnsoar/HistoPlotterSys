import pickle
import math
best_3yrs={
        '3yrs':{
                'maxMET':80.0,
                'min_dphi_z_b':1.4000000000000001,
                'min_z_pt':20.0,
                'max_ptzb':420.0,
        },
        '2016preVFP':{
                'maxMET':65.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':500.0,
                'init_signif':149.28983908208474,
        },
        '2016postVFP':{
                'maxMET':50.0,
                'min_dphi_z_b':1.4000000000000001,
                'min_z_pt':15.0,
                'max_ptzb':360.0,
                'init_signif':87.8515953084612,
        },
        '2017':{
                'maxMET':80.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':20.0,
                'max_ptzb':580.0,
                'init_signif':143.1577233013101,
        },
        '2018':{
                'maxMET':75.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':600.0,
                'init_signif':261.9534375423984,                
        },        
        
}


def CalcSignif(S,S_sumw2,B1,B1_sumw2,B2,B2_sumw2):
        if S == 0 :
            return 0
        ret = S / math.sqrt(S + B1 + B2 + S_sumw2 + B1_sumw2 + B2_sumw2)
        return ret

def ReadPickle(path):
    #print('READ->',path)
    with open(path, "rb") as f:
        this_dict = pickle.load(f)
        return this_dict



    
def ComparePoints(year):
        inputpath_S="output_pickle/eventname__S__nsplit__15__"+year+".pkl"
        inputpath_B1="output_pickle/eventname__B1__nsplit__15__"+year+".pkl"
        inputpath_B2="output_pickle/eventname__B2__nsplit__70__"+year+".pkl"
        #self.dict_S[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['S']
        dict_S=ReadPickle(inputpath_S)
        dict_B1=ReadPickle(inputpath_B1)
        dict_B2=ReadPickle(inputpath_B2)
        #'maxMET':65.0,
        #'min_dphi_z_b':0.0,
        #'min_z_pt':5.0,
        #'max_ptzb':500.0,
        
        point_year_specific=[best_3yrs[year]['maxMET'],best_3yrs[year]['min_dphi_z_b'],best_3yrs[year]['min_z_pt'],best_3yrs[year]['max_ptzb']]
        point_combine=[best_3yrs['3yrs']['maxMET'],best_3yrs[year]['min_dphi_z_b'],best_3yrs[year]['min_z_pt'],best_3yrs[year]['max_ptzb']]
        
        S_specific=dict_S[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['S']
        S_sumw2_specific=dict_S[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['S_sumw2']
        B1_specific=dict_B1[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B1']
        B1_sumw2_specific=dict_B1[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B1_sumw2']
        B2_specific=dict_B2[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B2']
        B2_sumw2_specific=dict_B2[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B2_sumw2']
        
        siginif_specific=CalcSignif(S_specific,S_sumw2_specific,B1_specific,B1_sumw2_specific,B2_specific,B2_sumw2_specific)
        
        S_combine=dict_S[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['S']
        S_sumw2_combine=dict_S[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['S_sumw2']
        B1_combine=dict_B1[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B1']
        B1_sumw2_combine=dict_B1[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B1_sumw2']
        B2_combine=dict_B2[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B2']
        B2_sumw2_combine=dict_B2[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B2_sumw2']    
        
        siginif_combine=CalcSignif(S_combine,S_sumw2_combine,B1_combine,B1_sumw2_combine,B2_combine,B2_sumw2_combine)
        
        print('<',year,'>')
        print('[init]=',best_3yrs[year]['init_signif'])
        print('[year-specific]=',siginif_specific)
        print('[combined]=',siginif_combine)
if __name__ == '__main__' :
        years=['2016preVFP','2016postVFP','2017','2018']
        for year in years:
                ComparePoints(year)
