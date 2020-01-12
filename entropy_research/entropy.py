#!/bin/python3
#inspiration from http://code.activestate.com/recipes/577476-shannon-entropy-calculation/
#might have have to adjust the plaintext one because of accuracy because english letters arent perfectly random

import sys
import math
import sets

word = str(sys.argv[1])

symlist = list(word)
wordset = list(set(symlist))
print(word)

freqlist = []
for symbol in wordset:
	ctr = 0
	for sym in symlist:
		if sym == symbol:
			ctr += 1
	freqlist.append(float(ctr) / len(symlist))
print(freqlist)

ent = 0.0
for prob in freqlist:
	padj = 1/prob
	ent = ent + prob * math.log(padj, 2)

print(ent)

