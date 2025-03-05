"""
Full Pyramid Patterns

    *
   ***
  *****
 *******
*********

"""

n=int(input("Enter no of rows and cols: "))

c=1
spaces=n-1
for i in range(1,n+1):
	spaces=n-i
	for j in range(1,n+c):
		if(spaces>=j):
			print(" ",end="")
		else:
			print("*",end="")
		
	c=c+1
	print()
