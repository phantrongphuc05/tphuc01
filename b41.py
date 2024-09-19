# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:24:28 2024

@author: Admin
"""

n = int(input("Nhập vào số nguyên n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1, 2):
    S += (1 / i)
    S = float(S)
print("Tổng là: ", S)