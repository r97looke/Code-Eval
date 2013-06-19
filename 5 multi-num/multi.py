#!/usr/bin/python
import sys
import fileinput

def input(file):

    for line in fileinput.input([file]):
        x, n = [int(num) for num in line.split(',')]#obtains numbers from the line
        print(multiples(x,n))

#returns multiples of N
def find_mult(n):
    while True:
        n = n*2
        yield n

#finds the first mulitple of n, larger than x
def multiples(x,n):
    for ans in find_mult(n):
        if ans >= x:
            return ans

if __name__=="__main__":

    input(sys.argv[1])

    '''
    inputs = open(sys.argv[1], 'r') 
    for line in inputs:
        x, n = [int(num) for num in line.split(',')]#obtains numbers from the line
        print(multiples(x,n))
    line.close()
    '''