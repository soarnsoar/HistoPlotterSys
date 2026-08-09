ARR_YEAR=(2016preVFP 2016postVFP 2017 2018 3yrs)

mkdir -p logs
for YEAR in ${ARR_YEAR[@]};do
    python3 -u Draw2D.py ${YEAR} 0 &> logs/Draw2D_${YEAR}_0.log&
    python3 -u Draw2D.py ${YEAR} 1 &> logs/Draw2D_${YEAR}_1.log&
    python3 -u Draw2D.py ${YEAR} 2 &> logs/Draw2D_${YEAR}_2.log&
done
