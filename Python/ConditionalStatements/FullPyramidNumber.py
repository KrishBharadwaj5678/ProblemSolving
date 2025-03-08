"""
Pyramid Patterns in Python with Number

      1
    123
   12345
  1234567
123456789
"""

n=int(input("Enter no of rows and cols: "))
count=1
spaces=n-1
for i in range(1,n+1):
	for j in range(1,n+i):
		if(spaces>=j):
			print("",end=" ")
		else:
			print(count,end="")
			count+=1
	print()
	count=1
	spaces-=1
			