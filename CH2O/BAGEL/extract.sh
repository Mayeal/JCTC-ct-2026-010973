#!/bin/bash

name=CH2O-nacme
rm -rf result.csv
for i in $(seq 0 7); do
    for j in $(seq $((i+1)) 7); do
        grep "Nuclear energy gradient" -A 17 CH2O-nacme-$i-$j.out|grep "^        "|awk '{print $2}' >> result.csv
    done
done
