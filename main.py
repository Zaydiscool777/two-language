#!/bin/python3
import sys
# get file contents
wfile = open(sys.argv[1], 'r')
file = wfile.readlines()
wfile.close()

# compile to nfile
nfile = open(sys.argv[2], 'w+')

# iterate through the file
for i in file:
    # set j to a list of tokens in line i
    j = i.split(" ")
    print(i, end="")
    if j[0] == "init":
        nfile.write(f"{j[1]} {j[2]} = {j[3][:-1]};\n")

print('')
# close the compiled file to be run by tcc
nfile.close()
