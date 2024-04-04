#    parser = argparse.ArgumentParser(description='Plotter configuration')
#    parser.add_argument('-a', dest='AnalyzerName', default="")
#    parser.add_argument('-y', dest='year', default="")
#    parser.add_argument('-d', dest=dirctory, default="")
Ana=DiLeptonAnalyzer
YEAR=2017
#RunPlotterDataMC.py -a $Ana -y 2017 -d plot/$Ana --nosys
#suffix=checksf__
suffix=runSys__
RunPlotterDataMC.py -a $Ana -y ${YEAR} -d plot/${YEAR}/${suffix} -s ${suffix}
