"""
Full Pyramid using Recursion

    *
   ***
  *****
 *******
*********

"""

n=int(input("Enter no. of rows and cols: "))
spaces=n-1
star=1
c=1 #count

def printStar():
	global spaces,star,c
	for i in range(0,star):
		print("*",end="")
	star+=2
	c+=1
	print()
	fullPyramid()

def printSpaces():
	global spaces,star
	for i in range(0,spaces):
		print("",end=" ")
	spaces-=1
	printStar()

def fullPyramid():
	global spaces,star,n,c
	if(n>=c):
		printSpaces()
	
fullPyramid()
