ARR_SUBD=("/" "cut_v2405.1__")
for d in ${ARR_SUBD[@]};do
    mkdir -p 2018/$d/
    mkdir -p 2016preVFP/$d/
    mkdir -p 2016postVFP/$d/

    cp 2017/$d/*.py 2018/$d/
    cp 2017/$d/*.py 2016preVFP/$d/
    cp 2017/$d/*.py 2016postVFP/$d/

done
