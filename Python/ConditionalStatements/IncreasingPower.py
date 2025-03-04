"""
Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

Example:

Input:
x = 10
Output:
1 4 9

"""

def printIncreasingPower(x):
	for i in range(1,x):
		if(x>i*i):
			print(i*i,end=" ")
		else:
			break

printIncreasingPower(20)
