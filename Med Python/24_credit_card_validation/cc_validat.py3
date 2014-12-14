#!/usr/bin/env python
import sys
def processList(line):
    """
    Takes a list of numbers and sums them. 
    Every second number is doubled. If greater than 9, we sum the digits.
    We then mod the sum, if it is 0, return 0. Else return 1
    """
    sumOfLine = 0
    tempNum = 0
    testing = ''
    for each in range(len(line)): #iterate through the line
        if each % 2 == 1: #for every second number
            tempNum = line[each] * 2#double it
            if tempNum > 9: #if greater than 9
                testing = str(tempNum)
                sumOfLine += int(testing[0]) + int(testing[1])
        else:
            sumOfLine += line[each]
    sumOfLine = sumOfLine % 10
    if sumOfLine > 0:
        return 0 
    else:
        return 1
def formatLine(line):
    """
    Converts a formatted string into reversed int list without whitespace
    """
    line = line.replace(" ", "")#removes whitespace
    outlist = []
    print "input line : "+line
    for each in list(line[::-1]): #iterates through the revered string
        outlist.append(int(each)) #appends each number as an int
    return outlist
def main():
    with open(sys.argv[1]) as f:
        for line in f:
            workingList = formatLine(line.strip())
            print (processList(workingList))
if __name__=="__main__":
    main()
