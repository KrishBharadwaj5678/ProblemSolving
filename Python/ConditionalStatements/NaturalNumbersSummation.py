"""
Given a natural number n, the task is to write a Python program to first find the sum of first n natural numbers and then print each step as a pattern.

Input: 5

Output:

1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15

"""

n=int(input("Enter a natural number: "))
for i in range(1,n+1):
	str=""
	sum=0
	for j in range(1,i+1):
		if(i==j):
			str+=f"{j}"
		else:
			str+=f"{j} + "
		sum=sum+j
	str=f"{str} = {sum}"
	print(str)
		
