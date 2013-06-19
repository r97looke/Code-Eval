#!/usr/bin/env python

import sys
import fileinput

def findNModM(number):
	n, m = [int(num) for num in number.split(',')]#obtains numbers from the line
	while 1:
		if (n-m)>=0:
			n -= m
		else:
			return n

def myfileInput(file):
	for line in fileinput.input([file]):
		print findNModM(line.rstrip().strip())

if __name__=="__main__":
    myfileInput(sys.argv[1])
