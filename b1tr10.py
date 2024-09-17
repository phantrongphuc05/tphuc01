# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:57:38 2024

@author: Admin
"""
n= int(input("Nhập 1 số nguyên n: "))
if n<0:
    print("Vui lòng nhập số lớn hơn 0")
else:
    GiaiThua = 1
    for i in range (1,n+1):
        GiaiThua= GiaiThua*i
        print(GiaiThua)
    