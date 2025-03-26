#### use cvmfs for root ####                                                                                                      
export CMS_PATH=/cvmfs/cms.cern.ch
source $CMS_PATH/cmsset_default.sh
#export SCRAM_ARCH=slc7_amd64_gcc900
#export cmsswrel='cmssw/CMSSW_11_2_5'
#export SCRAM_ARCH=slc7_amd64_gcc820
#export cmsswrel='cmssw/CMSSW_10_6_4'
#export SCRAM_ARCH=slc7_amd64_gcc700
#export cmsswrel='cmssw/CMSSW_10_2_6'

export SCRAM_ARCH=el9_amd64_gcc12
export cmsswrel='cmssw/CMSSW_15_0_1'






cd /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/$cmsswrel/src
echo "@@@@ SCRAM_ARCH = "$SCRAM_ARCH
echo "@@@@ cmsswrel = "$cmsswrel
echo "@@@@ scram..."
eval `scramv1 runtime -sh`
cd -
source /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/$cmsswrel/external/$SCRAM_ARCH/bin/thisroot.sh
##add after os el9 update
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/bin/python2.7:$LD_LIBRARY_PATH

alias python=python3
