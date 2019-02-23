
# https://www.hackerrank.com/challenges/py-if-else/problem

number = int(input())

if number % 2 == 1 : 
  # Number is odd 
  print("Weird")

elif number % 2 == 0 : 
  # Number is even 

  if number in range (2,6) : 
    print ("Not Weird")
  elif number in range (6,21) : 
    print ("Weird")
  elif number > 20 : 
    print ("Not Weird")
