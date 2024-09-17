# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:56:38 2024

@author: Admin
"""

import math
n = int(input("Nhập vào số nguyên dương n: "))
số_không_nguyên_tố = []
while n <= 0:
    n = int(input("Nhập lại số n: "))
kiểm_tra= math.sqrt(n)
for i in range(2, int(kiểm_tra) + 1):
    if n % i == 0:
        số_không_nguyên_tố += [i]
if len(số_không_nguyên_tố) == 0:
    print("Số", n, "là số nguyên tố")
else:
    print("Số", n, "không là số nguyên tố")