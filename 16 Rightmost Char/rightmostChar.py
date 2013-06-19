#!/usr/bin/python

import sys
import fileinput

def rightmost(line,target):
	indices = []
	idx = -1
	while True:
		try:
			idx = line.index(target, idx+1)
			indices.append(idx)
		except ValueError:
			break
	
	if not indices:
		return -1

	return indices[0]


def input(file):#Simple input
	for line in fileinput.input([file]):
		#print line
		line = line.rstrip() #remove training charactors
		target = line[-1] #obtain the char we need to find
		line = line[0:-2] #trim the end off the line

		print rightmost(line,target)

        
if __name__=="__main__":
    input(sys.argv[1])
