# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:30:21 2024

@author: Admin
"""

n = int(input("Nhập vào số n: "))
S = 1 
while n<0 or n%2==0:
    n = int(input("Nhập lại n: "))
for i in range(1, n+1):
    S *= i
print("Tích là: ", S)