
mkdir -p logs
StartTime=$(date +%s)

#    parser = argparse.ArgumentParser(description='Plotter configuration')
#    parser.add_argument('-a', dest='AnalyzerName', default="")
#    parser.add_argument('-y', dest='year', default="")
#    parser.add_argument('-d', dest=dirctory, default="")
ARR_YEAR=(2016preVFP 2016postVFP 2017 2018)
Ana=DiLeptonAnalyzer
#YEAR=2016preVFP
#YEAR=2016postVFP
#YEAR=2017
#YEAR=2018
#RunPlotterDataMC.py -a $Ana -y 2017 -d plot/$Ana --nosys
#suffix=checksf__
suffix=runSys__
#suffix="/"
for YEAR in ${ARR_YEAR[@]};do
    echo ${YEAR}
    ParseSKFlatOutput.py -a ${Ana} -y ${YEAR} -s ${suffix}
    (_StartTime=$(date +%s);RunPlotterDataMC.py -a $Ana -y ${YEAR} -d plot/${YEAR}/${suffix} -s ${suffix};EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec") &> logs/${suffix}${ANA}__${YEAR}.log&
    EndTime=$(date +%s)
done
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
