def binary_search (list, item ):
low = 0
high  = len (list) -1 
  while low <= high :
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item :
      return  mid 
    if guess > list
      hing = mid -1
else:
     low = mid +1
  return None
my_ list =  [1,2,3,4,5,6,7]
print (binay_search (my_list , 2))
