#!/usr/bin/env python

import sys
import fileinput
import collections
import string

"""
Rate the beauty of a string of text. Each letter is rated between 1-26.
So given a string work out the highest possible scpore it could get

So in English we count the most common occuring strings and rate the most common
as having the highest possible score.
"""

def beautifulString(line):
	line = line.lower()

	l = collections.Counter(line)
	add = 26
	beauty = 0

	for key,value in l.most_common():
		if key in string.letters[:26]:
			beauty += value*add
			add -= 1

	return beauty


def myfileInput(file):
	for line in fileinput.input([file]):
		print beautifulString(line.rstrip().strip())

if __name__=="__main__":
    myfileInput(sys.argv[1])

                          