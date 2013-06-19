#!/usr/bin/python

def go():
    sop = 0
    count = 0
    x = 0
    while count != 1000: #we want the first 1000 primes
        if isprime(x):
            sop += x
            count = count+1
        x = x+1#not too important
    print sop

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