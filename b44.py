# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:50:29 2024

@author: Admin
"""

n = int(input("Nhập số nguyên n: "))
S = 0 
while n <= 0 :
    n = int(input("Vui lòng nhập lại n: "))
for i in range(1, n+1, 2):
    S += (i/(i+1))
    S = float(S)
print("Kết quả là: ",S)
