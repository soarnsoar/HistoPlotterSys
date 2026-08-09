import pickle
import  math
best_3yrs={
        '3yrs':{
                'maxMET':70.0,
                'min_dphi_z_b':0,
                'min_z_pt':5.0,
                'max_ptzb':500.0,
        },
        '2016preVFP':{
                'maxMET':65.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':520.0,
                'init_signif':185.70146875508885,
        },
        '2016postVFP':{
                'maxMET':70.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':-1,
                'init_signif':172.63982240508156,
        },
        '2017':{
                'maxMET':75.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':600.0,
                'init_signif':277.4719361483125,
        },
        '2018':{
                'maxMET':75.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':500.0,
                'init_signif':341.86413717050215,
        },

}


###---
best_3yrs_no_jetveto={
        '3yrs':{
                'maxMET':75.0,
                'min_dphi_z_b':0,
                'min_z_pt':5.0,
                'max_ptzb':500.0,
        },
        '2016preVFP':{
                'maxMET':65.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':520.0,
                'init_signif':183.9864559944922,
        },
        '2016postVFP':{
                'maxMET':70.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':480.0,
                'init_signif':171.0806225382251,
        },
        '2017':{
                'maxMET':75.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':600.0,
                'init_signif':273.90567932014585,
        },
        '2018':{
                'maxMET':75.0,
                'min_dphi_z_b':0.0,
                'min_z_pt':5.0,
                'max_ptzb':500.0,
                'init_signif':337.8058228201545,
        },        
        
}


def CalcSignif(S,S_sumw2,B1,B1_sumw2,B2,B2_sumw2,data):
        if S == 0 :
                return 0
        if 0:
                print('S=',S)
                print('S_sumw2=',S_sumw2)
                print('B1=',B1)
                print('B1_sumw2=',B1_sumw2)
                print('B2=',B2)
                print('B2_sumw2=',B2_suxmw2)        
        ret = S / math.sqrt(data)
        return ret

def ReadPickle(path):
    #print('READ->',path)
    with open(path, "rb") as f:
        this_dict = pickle.load(f)
        return this_dict



    
def ComparePoints(year):
        print('<',year,'>')
        #print('best_3yrs=')
        #print(best_3yrs)
        inputpath_S="output_pickle/eventname__S__nsplit__10__"+year+".pkl"
        inputpath_B1="output_pickle/eventname__B1__nsplit__10__"+year+".pkl"
        inputpath_B2="output_pickle/eventname__B2__nsplit__70__"+year+".pkl"
        inputpath_data="output_pickle/eventname__data__nsplit__10__"+year+".pkl"
        #self.dict_S[maxMET][min_dphi_z_b][min_z_pt][max_ptzb]['S']
        dict_S=ReadPickle(inputpath_S)
        dict_B1=ReadPickle(inputpath_B1)
        dict_B2=ReadPickle(inputpath_B2)
        dict_data=ReadPickle(inputpath_data)
        #'maxMET':65.0,
        #'min_dphi_z_b':0.0,
        #'min_z_pt':5.0,
        #'max_ptzb':500.0,
        
        point_year_specific=[best_3yrs[year]['maxMET'],best_3yrs[year]['min_dphi_z_b'],best_3yrs[year]['min_z_pt'],best_3yrs[year]['max_ptzb']]+[]
        point_combine=[best_3yrs['3yrs']['maxMET'],best_3yrs['3yrs']['min_dphi_z_b'],best_3yrs['3yrs']['min_z_pt'],best_3yrs['3yrs']['max_ptzb']]+[]

        print('point_year_specific=',point_year_specific)
        print('point_combine=',point_combine)
        
        S_specific=dict_S[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['S']
        S_sumw2_specific=dict_S[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['S_sumw2']
        B1_specific=dict_B1[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B1']
        B1_sumw2_specific=dict_B1[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B1_sumw2']
        B2_specific=dict_B2[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B2']
        B2_sumw2_specific=dict_B2[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['B2_sumw2']
        data_specific=dict_data[point_year_specific[0]][point_year_specific[1]][point_year_specific[2]][point_year_specific[3]]['data']
        
        siginif_specific=CalcSignif(S_specific,S_sumw2_specific,B1_specific,B1_sumw2_specific,B2_specific,B2_sumw2_specific,data_specific)
        
        S_combine=dict_S[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['S']
        S_sumw2_combine=dict_S[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['S_sumw2']
        B1_combine=dict_B1[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B1']
        B1_sumw2_combine=dict_B1[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B1_sumw2']
        B2_combine=dict_B2[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B2']
        B2_sumw2_combine=dict_B2[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['B2_sumw2']
        data_combine=dict_data[point_combine[0]][point_combine[1]][point_combine[2]][point_combine[3]]['data']
        
        siginif_combine=CalcSignif(S_combine,S_sumw2_combine,B1_combine,B1_sumw2_combine,B2_combine,B2_sumw2_combine,data_combine)
        

        print('[init]=',best_3yrs[year]['init_signif'])
        print('[year-specific]=',siginif_specific)
        print('[combined]=',siginif_combine)
if __name__ == '__main__' :
        years=['2016preVFP','2016postVFP','2017','2018']
        for year in years:
                ComparePoints(year)
