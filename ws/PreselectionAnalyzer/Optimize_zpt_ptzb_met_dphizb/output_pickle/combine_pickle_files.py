import os
import glob
import pickle
import sys

def ReadPickle(path):
    with open(path, "rb") as f:
        this_dict = pickle.load(f)
        return this_dict
def combine_dict(_list_dict):
    ret={}
    nToAdd=len(_list_dict)
    print('nToAdd=',nToAdd)
    idx=0
    for d in _list_dict:
        print(idx)
        idx+=1
    
        ##d = dict
        #print(sorted(d))
        for _maxMET in d:
            ##maxMET
            if not _maxMET in ret : ret[_maxMET]={}
            for _min_dphi_z_b in d[_maxMET]:
                ##min_dphi_z_b
                #print(sorted(d[_maxMET]))
                if not _min_dphi_z_b in ret[_maxMET] : ret[_maxMET][_min_dphi_z_b]={}
                for _min_z_pt in d[_maxMET][_min_dphi_z_b] :
                    ##min_z_pt
                    #print(sorted(d[_maxMET][_min_dphi_z_b]))
                    if not _min_z_pt in ret[_maxMET][_min_dphi_z_b] : ret[_maxMET][_min_dphi_z_b][_min_z_pt]={}
                    for _max_ptzb in d[_maxMET][_min_dphi_z_b][_min_z_pt]:
                        ##max_ptzb
                        #print(sorted(d[_maxMET][_min_dphi_z_b][_min_z_pt]))
                        if not _max_ptzb in ret[_maxMET][_min_dphi_z_b][_min_z_pt]:ret[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb]={}
                        for key in d[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb]:
                            #print(sorted(d[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb]))
                            if not key in ret[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb]:
                                ret[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][key]=0.
                            #print(key)
                            current_val=ret[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][key]
                            #print('current_val=',current_val)
                            #print('val to add=',d[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][key])
                            ret[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][key] = current_val + d[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][key]
                            
        
    return ret
#####
#../WORKDIR_outpickle/OptGrid__2016preVFP__PreselectionAnalyzer__jetpuid_loose__lepveto__/eventname__S__nsplit__15/0/PreselectionAnalyzer__jetpuid_loose__lepveto____2016preVFP.pkl
inputlist_str=sys.argv[1]
output_path=sys.argv[2]

inputlist=glob.glob(inputlist_str)
list_dict=[]
for path in inputlist:
    this_dict=ReadPickle(path)
    list_dict.append(this_dict)

combined_dict=combine_dict(list_dict)



dirpath=os.path.dirname(output_path)
if dirpath!='':
    os.system('mkdir -p '+dirpath)
with open(output_path, "wb") as f:
    pickle.dump(combined_dict, f)

