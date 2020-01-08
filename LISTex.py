# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:14:06 2020

@author: Admin
"""

#python program to find largest number in a list
a=[]
n=int(input("enter the number of elements:"))
for i in range(1,n+1):
    b=int(input("enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])