#!/usr/bin/python
import sys

def FizzBuzz(file):

	f = open(file, 'r') 
	while 1:	
		line = f.readline()#read a line
		if not line:
			break
		game(line)
		pass	
	f.close
	

def game(read_data):
	fizz = getNum(read_data)#take a number
	read_data = update(read_data)#remove that number
	buzz = getNum(read_data)#take a number
	read_data = update(read_data)#remove that number
	limit = getNum(read_data)
	play(int(fizz), int(buzz), int(limit))


def play(Fizz, Buzz, Limit):#this plays the game
	result = ''
	for x in range(Limit):

		y=x+1#we add one to the range
		if ((y%Fizz==0)and(y%Buzz==0)):
			result += ' FB'
		elif (y % Fizz) == 0: 
			result += ' F'
		elif (y % Buzz) == 0:
			result += ' B'
		else:
			result += ' '+str(y)
	print result[1:]

def getNum(data):#returns the first number from a list
	a = ''
	for x in range(len(data)):
		if data[x] != ' ':
			data[x+2:]
			a += data[x]
		else:
			return a
	return a#this should never happen.	
	   

def update(data):
	for x in range(len(data)):
		if data[x] != ' ':
			return data[x+2:]#returns the list minus the first number
	return data

if __name__=="__main__":

		FizzBuzz(sys.argv[1])