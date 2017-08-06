# Power Hungry

def answer(xs):
  if len(xs) == 1:
      return str(xs[0])
  # Remove all zeroes:
  xs = [elem for elem in xs if elem != 0]
 
  # Store all positives since we always want to take them 
  pos = [elem for elem in xs if elem >0]
  
  # Only keep the negatives
  xs = [elem for elem in xs if elem < 0]

  # Check if number of negatives is even or odd
  if len(xs) % 2 != 0:
    # If odd, remove the biggest negative
    xs = sorted(xs)
    popped = xs.pop()

  resultList = xs + pos
  
  if len(pos) == 0 and len(xs) == 0:
    return 0
    
  print(resultList)
  
  result = reduce(lambda x,y: x * y, resultList) 
print(answer([0,2])) 
