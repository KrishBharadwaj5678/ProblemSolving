"""
Pyramid Patterns in Python with Alphabet
      A 
     A B 
    A B C 
   A B C D 
  A B C D E 
"""

n=int(input("Enter no of rows and cols: "))
num=65
spaces=n
for i in range(1,n+1):
	spaces-=1
	for j in range(1,n+1):
		if(spaces>=j):
			print("",end=" ")
		else:
			print(chr(num),end=" ")
			num+=1
	print()
	num=65
