#!/usr/bin/python

#key lesson here is string formatting.
#rjust is used to right align a string and add whitespace.

if __name__=="__main__":

	n = 1 
	while n <= 12:#working down
		x = 1
		while x <= 12:#working accross
			if x == 1:
				print n*x,
			else:
				print repr(n*x).rjust(3),#line formatting
			x += 1
		print ""#newline
		n += 1

