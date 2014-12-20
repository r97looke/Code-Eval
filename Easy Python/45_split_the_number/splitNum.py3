#!/usr/bin/env python
import sys
def processLine(inputList):
    print inputList
    instructions = getInstructions(inputList[1])
    print instructions

def getInstructions(inputString):
    return inputString 

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            processLine(line.strip().split())
if __name__=="__main__":
    main()
