#!/usr/bin/env python

import sys
import fileinput

'''
Core Method

Takes an input string,
and counts how many times each digit occurs.
incrementing the values in answer at the location of the digit.
(so for digit 2 in number, we increment answer[2])

if the number is self describing number and answer[:len(number)]  will match
So we use map to turn answer into and string and compare it with number
'''
def findDescription(number):
	answer = [0,0,0,0,0,0,0,0,0,0]

	for x in number:  
		answer[int(x)] = int(answer[int(x)])+1  

	if ''.join(map(str, answer[:len(number)])) == number:
		return 1
	else:
		return 0

def myfileInput(file):
	for line in fileinput.input([file]):
		print findDescription(line.rstrip().strip())

if __name__=="__main__":
    myfileInput(sys.argv[1])
