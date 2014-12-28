#!/usr/bin/env python
import sys
import string
def processInput(inputList):
    instructions = getInstructions(inputList[1])
    print (processLine(instructions,inputList[0]))

def getInstructions(inputString):
    """
    Takes an input string that contains an '+' or '-'
    Returns the index of anf the value of the symbol.
    """
    for each in inputString:
        if each not in string.ascii_lowercase:
            return each+str(inputString.index(each))
    return "+" #this should never be called

def processLine(instructions,number):
    """
    Takes instructions and a number.
    Determines the first and second half of the number
    Uses the instructions to insert a symbol at the provided index.
    """
    firstHalf = number[0:int(instructions[len(instructions)-1])]
    secondHalf = number[len(firstHalf):]

    if instructions[0] is '+':
        return int(firstHalf) + int(secondHalf)
    else:
        return int(firstHalf) - int(secondHalf)
    return "This should never execute"

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            #print (line.strip())
            processInput(line.strip().split())
if __name__=="__main__":
    main()
