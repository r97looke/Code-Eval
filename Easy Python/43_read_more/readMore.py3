#!/usr/bin/env python
import sys

def trimLine(line):
    """
    starts at 40 and finds the last space in the line.
    We trim to there and add the ending to the line.
    Return it for printing.
    """
    trimvalue = 40 #starting value
    while line[trimvalue-1:trimvalue] != " ":
        trimvalue -= 1
        if trimvalue == 0:#if doesn't have a space
            return line[:40]+"... <Read More>"
    return line[:trimvalue-1]+"... <Read More>"

def processLine(line):
    """
    Prints our lines and sends the long ones to be trimmed
    """
    if len(line)>55:
        line = trimLine(line)
    print (line)

def main():
    """
    Main handles input and passes each line to processLine
    """
    with open(sys.argv[1]) as f:
        for line in f:
            processLine(line.strip())
if __name__=="__main__":
    main()
