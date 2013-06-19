#!/usr/bin/env python

import sys
import fileinput

def hexToDec(number):
	return int(number,16)

def myfileInput(file):
	for line in fileinput.input([file]):
		print hexToDec(line.rstrip().strip())

if __name__=="__main__":
    myfileInput(sys.argv[1])
