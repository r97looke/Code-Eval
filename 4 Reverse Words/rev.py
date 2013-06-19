#!/usr/bin/python
import sys
import fileinput

def input(file):

    for line in fileinput.input([file]):
        rev(line)

def rev(line):
    #here we reverse and print the line.
    out = line.split() #splits the line into words
    out.reverse()
    printOut(out)

def printOut(line):
    #print out the list
    for x in line:
        print x,
    print ''

if __name__=="__main__":
    input(sys.argv[1])