'''
*********
PROGRAM 1
*********
Define a function number_of_odds that takes a list of integers as an argument. The function returns how many odd integers are in the list.
'''
def number_of_odds(lst):
  odds = []
  for i in lst:
    if i%2 != 0:
      odds.append(i)
  return len(odds) 
