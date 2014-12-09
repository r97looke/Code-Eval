#!/usr/bin/env python
import sys
def processList(line):
    """
    takes a list of numbers, doubles every second number.
    If greater than 9, we sum the digits
    """
    return line#placeholder
def formatLine(line):
    """
    converts a formatted string into reversed list without whitespace
    """
    line = line.replace(" ", "")
    return list(line[::-1])
def main():
    with open(sys.argv[1]) as f:
        for line in f:
            workingList = formatLine(line.strip())
            print workingList
if __name__=="__main__":
    main()
