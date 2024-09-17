# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:19:59 2024

@author: Admin
"""

n = int(input("Nhập vào số n: "))
S = 0
while n<0 or n%2!=0:
    n = int(input("Nhập lại n: "))
for i in range(2, n + 1, 2):
    S += i
print("Tổng là: ", S)
  