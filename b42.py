# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:31:53 2024

@author: Admin
"""

n = int(input("Nhập số nguyên n: "))
S = 1
while n <= 0:
    n = int(input("Vui lòng nhập lại n: "))
for i in range(1, n + 1):
    S+=(1/(i*(i + 1)))
    S = float(S)
    print("Kết quả là: ", S)