#!/bin/bash

declare "wordlist=$(cat 4_letter)"

for i in $wordlist 
do
python3 entropy.py $i
done