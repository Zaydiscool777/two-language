#!/bin/python3
import sys
print(sys.argv)
f = open(sys.argv[1], 'r')
for i in f.readlines():
    print(i, end='')
f.seek(0)
print(f.readlines())
f.close()