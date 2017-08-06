# Approach using caching

def answer(l):
  #Must have atleast 3 elements to make a tuple.
  
  # [1, 2 ,3, 4 ,6, 8]
  if len(l) < 3:
    return 0
    
  memoizedArray = [0] * len(l) 
  for i in range(len(l)):
      multiples = 0
      for j in range(i+1,len(l)):
          if l[j] % l[i] == 0:
              multiples += 1
      memoizedArray[i] = multiples
  print(memoizedArray)
  answer = 0
  for i in range(len(l)-1):
      for j in range(i+1,len(l)):
          if l[j] % l[i] == 0:
              answer += memoizedArray[j]
  return answer   
