#!/usr/bin/env python
import sys
def countOccurance(numList):
    """
    Takes a list and countes the occurances of the first entry,
    until the number changes.
    """
    curr = numList[0]
    counter = 0
    for each in numList:
        if curr == each:
            counter += 1
        else:
            return counter
    return counter
def main():
    with open(sys.argv[1]) as f:
        for line in f:
            outline = ''#our output
            numList = line.strip().split() #clean input
            while(len(numList)>0):#while we have unproccessed input
                counter = countOccurance(numList)#count occurances of the first number
                outline += str(counter)+" "+numList[0]+" "#formatting it for output
                for each in range(0,counter):#removes proccessed numbers
                    numList.pop(0)
            print(outline)
if __name__=="__main__":
    main()
