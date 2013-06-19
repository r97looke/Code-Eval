#!/usr/bin/python

def go():

	high = 2
	for x in range(1000):
		if (palindrome(x) and isprime(x)):
			high = x

	print high

def palindrome(x):
	#check if the number is a palindrome
	num = str(x)
	rev = num[::-1]#reverses the string
	if num == rev:
		return True

	return False


def isprime(n):
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

if __name__=="__main__":
	go()