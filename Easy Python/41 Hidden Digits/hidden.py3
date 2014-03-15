#!/usr/bin/env python
import sys

def main():
	hidden = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}
	with open(sys.argv[1]) as f:
		for line in f:
			outString = ''
			for char in line:
				if char in hidden:#if the char is in our dictionary, convert it to a number
					outString += hidden[char]
				#or if the char is an integer add to the output String
				if char.isdigit():
					outString += char

			if len(outString) < 1:#for outputting, if we found nothing we need to output NONE
				print ('NONE')
			else:
				print (outString)
if __name__=="__main__":
   main()
