import math
import random as rd
import sys
import os
import palindrome
print(math.factorial(5))
aoc=2*math.pi*math.pow(5,2)
print(aoc)
print(rd.random())#random number between 0 and 1
#random number between 1 to 10
print("Random number between 1 to 10 ",math.floor(rd.random()*11))
print("Random number between 10 to 99 in steps of 10",rd.randrange(10,99,10))
print("random number between 10 to 99",rd.randint(10,99))
print(sys.modules)
print(sys.path)
print(os.name)
print(os.getcwd())
print("test")
print(palindrome.palindromeCheck('Malayalam'))
