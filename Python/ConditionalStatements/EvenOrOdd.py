"""
Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)

Your Task:
Your task is to complete the function checkOddEven(), which returns True (In python, True starts with caps T) if the number is even, else return False (In Python, False starts with caps F).
"""

def checkOddEven(num):
  if(num%2==0):
    return True
  else:
    return False
result=checkOddEven(18)
print(result)