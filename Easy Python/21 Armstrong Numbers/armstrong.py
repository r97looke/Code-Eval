#!/usr/bin/env python

import sys
import fileinput

"""
 An Armstrong number of three digits is an integer such that 
 The sum of the cubes of its digits is equal to the number itself. 
 For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371. 
"""

def findArmstrong(number):

	#need to loop once per digit in number
	armstrong = 0
	for x in number:
		armstrong += int(x)**len(number)

	print armstrong
	print number

	if armstrong == int(number):
		return True
	else:
		return False

def myfileInput(file):
	for line in fileinput.input([file]):
		print findArmstrong(line.rstrip().strip())

if __name__=="__main__":
    myfileInput(sys.argv[1])
