# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:33:46 2024

@author: Admin
"""
n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
a = 0
S = 0 
while n <= 0:
    n = int(input("Vui lòng nhập lại n: "))
for i in range(1, n+1):
    a = a + i 
    S += ((x**i)/a)
print("Kết quả là: ", round(S, 2))
