#!/usr/bin/python
from itertools import ifilterfalse
import sys
import fileinput

def unique(iterable):
	seen = set()
	seen_add = seen.add 

	for element in ifilterfalse(seen.__contains__, iterable):
		seen_add(element)
		yield element

def input(file):#Simple input
	for line in fileinput.input([file]):
		print ','.join(unique(line.rstrip().split(','))) #string formatting

        
if __name__=="__main__":
    input(sys.argv[1])
