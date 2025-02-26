""""
  Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

  Return True for the following cases:

  Either a or b (not both) is non-negative and the flag is false.
  Both a and b are negative and the flag is true.
  Otherwise, return False.
"""

a=int(input())
b=int(input())
flag=True
if(a>0 or b>0 and flag==False):
  print(True)
elif((a<0 and b<0) and flag==True):
  print(True) 
else:
  print(False)