#!/usr/bin/python
import sys
import fileinput

def input(file):#Simple input
	answer = 0
	for line in fileinput.input([file]):
		answer += int(line)
	print answer        

        
if __name__=="__main__":
    input(sys.argv[1])
