#! /bin/bash

for file in *.txt
do
  echo $file
  grep -Fxv -f $file cities.txt
done > output.txt
