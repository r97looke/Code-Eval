#!/usr/bin/python

import sys
import fileinput

def findHappy(previous,line):
	number = sumFactor(line)#Gets the first
	while 1:
		#if our sum of factors is 1, it is a happy number and we are finished
		if number == 1:
			return 1 	

		#Check if we have seen this number before
		# Yes == we are looping, this is not a happy number, return 0, we are done here
		# No == add it to the list and keep going
		if str(number) in previous:
			return 0
		else:
			previous += str(number)
		number = sumFactor(str(number))


#	This method sums the factors of a number
#	Given 130
#	returns 1*1 + 3*3 + 0*0
def sumFactor(number):
	end = 0
	for  x in number:
		end += int(x)*int(x)
	return end


#	Simple file input
#	Reads file and places each line into 'line'
#	Program then runs seperatly for each line
def input(file):
	for line in fileinput.input([file]):
		previous = ''#set of previously seen numbers, always starts empty
		print findHappy(previous,line.rstrip().strip())

#	Main method, just takes the file from the command line
if __name__=="__main__":
    input(sys.argv[1])
