#!/usr/bin/env python
import sys

def processLine(line):
    """
    """
    print(line)

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            processLine(line)#Format and proccess the input line
if __name__=="__main__":
    main()
