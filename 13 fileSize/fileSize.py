#!/usr/bin/python
import sys
import fileinput

def input(file):#Simple input
	byteSize = 0
	for line in fileinput.input([file]):
		byteSize += len(line)
	print byteSize        

        
if __name__=="__main__":
    input(sys.argv[1])
