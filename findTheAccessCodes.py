# Find the access codes
# Version 1: Memory Inefficient


def makeHashMap(l):
  """
  Make a hashmap where key = (value, idx) and value = [(Multiple of key.value, idx),..]
  """
  hashMap = {}
  for idx, val in enumerate(l):
    counter = idx + 1
    _tmpList = []
    while counter < len(l):
      if l[counter] % val == 0:
        _tmpList.append((counter,l[counter]))
        hashMap[(idx,val)] = _tmpList
      counter += 1
    if (idx,val) not in hashMap:
      hashMap[(idx,val)] = []
  
  return hashMap
    
  
def answer(l):
  #Must have atleast 3 elements to make a tuple.
  if len(l) < 3:
    return 0
    
  l.sort() 
  hashMap = makeHashMap(l)
  count = 0
  for key in hashMap:
    for value in hashMap[key]:

      if len(hashMap[value]) > 0:
        count += len(hashMap[value])

  return count
l = range(1,2001)  
print(answer(l))
