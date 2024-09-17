# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:52:26 2024

@author: Admin
"""

import math
n = int(input("Nhập vào số nguyên dương : "))
while n <= 0:
    n = int(input("Nhập lại số khác: "))
scp = math.sqrt(n)
số = int(scp)
kiểm_tra = số*số
if n == kiểm_tra:
    print("Số", n, "là số chính phương")
else:
    print("Số", n, "không là số chính phương")