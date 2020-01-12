#!/bin/bash

declare "wordlist=$(cat /home/xfaraday/entropy_research/4_letter)"

for i in $wordlist 
do
python3 /home/xfaraday/entropy_research/base64-enc.py $i
done