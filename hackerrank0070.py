# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

count_students = int ( input ())

scores = map (int, raw_input().split())

scores.sort()
scores.reverse()

number, previous_number = -200, -200

for i in scores : 
  number = i 
  if previous_number == -200 : 
    previous_number = number 
  elif previous_number == number : 
    previous_number = number 
  elif previous_number > number :
    print ( number)
    break