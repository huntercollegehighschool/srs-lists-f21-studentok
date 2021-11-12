'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lst):
  odds = []
  length = len(lst)
  for i in range(length):
    if i%2 != 0:
      odds.append(lst[i])
  odds.reverse()
  return odds 
