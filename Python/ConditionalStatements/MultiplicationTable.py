"""
Writing for loop in Python is a tad different from C++ and Java counterparts. In this question, we'll learn to print table by using the for loop.

You are given a number N, you need to print its multiplication table.

Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the function multiplicationTable() that takes N as input.
"""

def multiplicationTable(N):
  for i in range(1,11):
    print(N*i,end=' ')

multiplicationTable(5)  