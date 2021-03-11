#!/bin/bash

for i in 71/ 72/ 73/ 74/ 75/ 76/ 77/ 78/ 79/ 80/ 81/ 82/ 83/
do
cd $i
sbatch sub.sh
pwd
cd ../
sleep 7200
done

