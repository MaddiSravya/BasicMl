# -*- coding: utf-8 -*-
"""Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LkFOfU6OL03TzlPy2684gQ-WtjT87LYM
"""



"""check whether a number is odd or even"""

n=int(input())
if n%2==0:
  print('It is a even number ')
else:
  print('It is odd number')

"""Given an three digit number.find thesum of its digits

"""

n=int(input())
s=0
while n!=0:
  d=n%10
  s=s+d
  n=n//10
print(s)



"""factorial of a number"""

n=int(input())
s=1
for i in range (1,n+1):
  s*=i
print(s)