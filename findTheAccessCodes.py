# Find the access codes
# Version 1: Memory Inefficient

"""
Access codes
============
You've discovered the evil laboratory of Dr. Boolean, and you've found that the
vile doctor is transforming your fellow rabbit kin into terrifying
rabbit-zombies! Naturally, you're less-than-happy about this turn of events.
Of course where there's a will, there's a way. Your top-notch assistant,
Beta Rabbit, managed to sneak in and steal some access codes for Dr. Boolean's
lab in the hopes that the two of you could then return and rescue some of the
undead rabbits. Unfortunately, once an access code is used it cannot be used
again. Worse still, if an access code is used, then that code backwards won't
work either! Who wrote this security system?
Your job is to compare a list of the access codes and find the number of
distinct codes, where two codes are considered to be "identical" (not distinct)
if they're exactly the same, or the same but reversed. The access codes only
contain the letters a-z, are all lowercase, and have at most 10 characters.
Each set of access codes provided will have at most 5000 codes in them.
For example, the access code "abc" is identical to "cba" as well as "abc."
The code "cba" is identical to "abc" as well as "cba." The list
["abc," "cba," "bac"] has 2 distinct access codes in it.
Write a function answer(x) which takes a list of access code strings, x, and
returns the number of distinct access code strings using this definition of
identical.
"""


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
