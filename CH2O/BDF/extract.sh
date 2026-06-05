#!/bin/bash

for func in SVWN5 BLYP B3LYP BHandHLYP; do
    for method in UTDDFT XTDDFT; do
        file=CH2O-$method-$func.out
        result=CH2O-$method-$func-result.csv
        grep "Gradient contribution from Final-NAC(S)-Escaled" -A 4 $file|grep "^      "|awk '{print $2 "\n" $3 "\n" $4}' > $result
    done
done
