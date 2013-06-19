#!/usr/bin/python
import sys
import fileinput

def input(file):#Simple input
    for line in fileinput.input([file]):
        n, p1, p2 = [int(num) for num in line.split(',')]#obtains numbers from the line
        print(check(n,p1,p2))

def check(n,p1,p2):

    #convert n to binary
    binary = bin(n)
    #print binary

    #compares the bit at p1 and p2, from right to left
    if binary[-p1] == binary[-p2]:
        return 'true'

    return 'false'

if __name__=="__main__":
    input(sys.argv[1])
