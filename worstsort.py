import random
from collections import Counter

def _create_rand_list(l):
  return [random.randint(min(l), max(l)) for x in l]

def _is_sorted(l):
  if l == []:
    return True
  f = l[0]
  for i in l:
    if i < f:
      return False
    f = i 
  return True 

def _contains_same_items(l1, l2):
  return dict(Counter(l1)) == dict(Counter(l2))
  
def sort(l):
  final_list = []             
  counter = 0
  matches = 0
  while True: 
    counter += 1
    rand_l = _create_rand_list(l) # type: ignore
    if counter % 10000000 == 0:
      print(f"Iteration {counter}: {rand_l}. Unsorted matches found: {matches}")
    if _contains_same_items(l, rand_l): # type: ignore
      matches += 1
      if _is_sorted(rand_l):  # type: ignore
        final_list = rand_l
        break
  print(f"Successful after {counter} attempts") 
  return final_list
