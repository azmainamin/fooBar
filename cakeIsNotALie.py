# The Cake is not a lie

from __future__ import division
from __future__ import print_function
def allSubstrings(s):
  """
  Return a list containing all possible substrings.
  """
  _allSubs = []
  for i in range(len(s)):
    _allSubs.append(s[:i+1])
  return _allSubs
  
def answer(s):
  
  _allSubs = allSubstrings(s)
  _validCakePieces = []
  len_s = len(s)
  
  if len_s == 0:
    return 0
  
  # For each substring check if we can get s back by multiplying the substring
  
  for sub in _allSubs:
    lenSub = len(sub)
    #canDivide = len(s)/len(sub)
    canDivide = len_s % lenSub
    q = int(len_s/lenSub)
    #print(q)
    makesS = sub * q == s
    if canDivide == 0 and makesS: # meaning no remaining char
      _validCakePieces.append(s.count(sub))
  
  
  print(max(_validCakePieces))
  return max(_validCakePieces)
  
  
answer("ab")
