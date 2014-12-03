#!/usr/bin/env python
import sys

def processLine(line):
    """
    takes a string of cities and distances.
    collects the distances and returns them as a sorted list of numbers
    """
    cities = []
    line = line.rstrip().split(';')#Split the cities
    for entry in line:
        if len(entry)>1:#Ignore empty entrys
            entry = entry.split(',')#split the city from its distance
            cities.append(entry[1])
    cities = [int(x) for x in cities]#convert distances from string to int
    return sorted(cities)

def formattedOutput(outlist):
    """
    Takes the finished list and outputs it as expected by the test
    """
    stringed = ''
    for value in outlist:
        stringed = stringed+','+str(value)
    print(stringed[1:])
        

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            finishedOutput = []
            cities = processLine(line)#Format and proccess the input line
            finishedOutput.append(cities[0])
            for x in range(0,len(cities)-1):
                finishedOutput.append(cities[x+1]-cities[x])
            formattedOutput(finishedOutput)
if __name__=="__main__":
    main()
