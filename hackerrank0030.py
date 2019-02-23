# https://www.hackerrank.com/challenges/python-division/problem

# This import is required for the float division to work on Python 2. 
from __future__ import division

firstNumber = int ( input())
secondNumber = int ( input() )

print (firstNumber // secondNumber)

# The float division will also work like int division if you dont do the import 
print (firstNumber / secondNumber)
