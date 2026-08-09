ARR_YEAR=(2016preVFP 2016postVFP 2017 2018)
ARR_LEPTON=(LeptonPlus LeptonMinus)
ARR_DECAY=(bJetHadronicSide bJetLeptonicSide)
ARR_PT=(PT30To50 PT50To70 PT70To100 PT100To140 PT140ToInf)
ARR_ETA=(Eta0To0p8 Eta0p8To1p6 Eta1p6To2 Eta2To2p5)
ARR_TYPE=(jOthers jH)

for YEAR in ${ARR_YEAR[@]};do
    for LEPTON in ${ARR_LEPTON[@]};do
	for DECAY in ${ARR_DECAY[@]};do
	    for PT in ${ARR_PT[@]};do
		for ETA in ${ARR_ETA[@]};do
		    for TYPE in ${ARR_TYPE[@]};do

			python3 ReadTerminatedTime.py ${YEAR} ${LEPTON} ${DECAY} ${PT} ${ETA} ${TYPE}
			
		    done
		done
	    done
	done
    done
done
	    
	
