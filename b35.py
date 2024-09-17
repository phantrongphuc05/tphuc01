# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:05:02 2024

@author: Admin
"""
n = int(input("Nhập một số nguyên dương n: "))
if n > 0:
    S = 0
    for i in range(1, n + 1):
        S += i
    print("Kết quả là: ", S)
else:
    print("Vui lòng nhập số nguyên dương")
    
        