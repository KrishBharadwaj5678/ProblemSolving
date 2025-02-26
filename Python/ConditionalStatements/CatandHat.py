"""
You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.

Your Task:
This is a function problem. You don't need to take any input. Just complete the function cat_hat() that takes a string str as input.
"""

def cat_hat(a):
  catCount=a.count("cat")
  hatCount=a.count("hat")
  if(catCount==hatCount):
    return True
  else:
    return False

result = cat_hat("CatinaHat".lower())
print(result)