#!/bin/sh

for number in `seq 200 200`
do
    python convert_b2BMP_S.py result_$number input_$number.bmp
done
