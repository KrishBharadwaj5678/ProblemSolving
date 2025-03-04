"""
In this question, we'll learn to print characters of a string at even indices.

You are given a string str, you need to print its characters at even indices(index starts at 0).

Input:
str = DoctorPhenomenal

Output:
DcoPeoea

"""

str = "Krish Bharadwaj"
for i in range(0,len(str)):
	if (i%2==0):
		print(str[i],end="")
