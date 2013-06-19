#!/usr/bin/python
import sys
import fileinput

def input(file):#Simple input
    for line in fileinput.input([file]):
        print sum_of_line(int(line))

def sum_of_line(n):

	sumout = 0 #output
	while(n > 0):
		sumout += n%10	# collect numbers under 10
		n /= 10			#remove them after collection
	return sumout

        
if __name__=="__main__":
    input(sys.argv[1])
