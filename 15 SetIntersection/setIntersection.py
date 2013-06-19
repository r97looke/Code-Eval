#!/usr/bin/python

import sys
import fileinput


def input(file):#Simple input
	for line in fileinput.input([file]):
		lists = line.rstrip().split(';') #strip out new lines and such

		setA, setB = [l.split(',') for l in lists]

		intersection = list(set(setA).intersection(set(setB)))
		intersection.sort
		print ','.join(intersection)



        
if __name__=="__main__":
    input(sys.argv[1])
