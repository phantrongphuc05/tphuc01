# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:59:18 2024

@author: Admin
"""

N = int(input("Nhập số nguyên dương N: "))
a = []
while N < 0:
    N = int(input("Nhập lại sô nguyên dương"))
for i in range(1, N + 1):
    a += [i]
print(a)