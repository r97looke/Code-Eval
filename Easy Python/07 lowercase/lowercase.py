#!/usr/bin/python
import sys
import fileinput

def input(file):#Simple input
    for line in fileinput.input([file]):
        print line.lower()
        
if __name__=="__main__":
    input(sys.argv[1])
