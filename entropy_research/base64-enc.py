#!/bin/python3

import sys
import base64

word = str(sys.argv[1])

print(word)

encbyte = base64.b64encode(word.encode("utf-8"))
encstr = str(encbyte, "utf-8")

print(encstr)