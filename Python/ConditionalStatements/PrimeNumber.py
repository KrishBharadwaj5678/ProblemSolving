"""
Given a positive integer N, the task is to write a Python program to check if the number is Prime or not in Python.
"""

N=int(input("Enter a number: "))
if(N==0 or N==1 or N<0):
	print("Not Prime Number")
else:
	for i in range(2,N+1):
		if(N==i):
			print("Prime Number")
		elif(N%i==0):
			print("Not Prime Number")
			break
			
