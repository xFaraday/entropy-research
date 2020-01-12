#!/bin/python3

import sys
import blowfish
from os import urandom

word = str(sys.argv[1])

print(word)

cipher = blowfish.Cipher(b"keyislitski")

testdata = urandom(10 * 8)

test = b"".join(cipher.encrypt_ecb(word))

print(test)