#!/usr/bin/python
import sys
import fileinput

def input(file):#Simple input
    for line in fileinput.input([file]):
        print Fibonacci(int(line))

def Fibonacci(n):
	
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)
	

        
if __name__=="__main__":
    input(sys.argv[1])
