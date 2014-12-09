#!/usr/bin/env python
import sys
def processList(line):
    """
    takes a list of numbers, doubles every second number.
    If greater than 9, we sum the digits
    """
    sumOfLine = 0
    tempNum = 0
    for each in range(len(line)): #iterate through the line
        if each % 2 == 1: #for every second number
            
            #This just got too complex, break this part into its own def
            tempNum = line[each] * 2
            if tempNum > 9:
                tempNum = tempNum[0] + tempNum[1]
        else:
            sumOfLine += line[each]
    print ""
    print line
    return line#placeholder
def formatLine(line):
    """
    Converts a formatted string into reversed int list without whitespace
    """
    line = line.replace(" ", "")#replaces whitespace with nothing
    outlist = []
    print "Input line: "+line
    for each in list(line[::-1]): #iterates through the revered string
        outlist.append(int(each)) #appends each number as an int
    return outlist
def main():
    with open(sys.argv[1]) as f:
        for line in f:
            workingList = formatLine(line.strip())
            print "Reversed Line: ",workingList
            processList(workingList)
            print ''
if __name__=="__main__":
    main()
