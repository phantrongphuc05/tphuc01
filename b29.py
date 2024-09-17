# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:32:05 2024

@author: Admin
"""

N = int(input("Nhập số nguyên dương N: "))
tong = 0
while N < 0:
    N = int(input("Nhập lại số nguyên dương N: "))
for a in str(N):
    tong += int(a)
print("Tổng các chữ số của N là: ", tong)