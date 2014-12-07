#!/usr/bin/env python
import sys

def processLine(line, trimPoint):
    """
    """
    if len(line)>55:#if the line is too long
        print line[:40]
        if line[trimPoint] == " ":
            line = line[:trimPoint] #if we are, trim here
        else:
            processLine(line, trimPoint+1)
    print line

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            processLine(line, 40)#Format and proccess the input line
if __name__=="__main__":
    main()
