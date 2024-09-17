# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:58:52 2024

@author: Admin
"""

a = int(input("Nhập vào số thứ nhất: "))
b = int(input("Nhập vào số thứ hai: "))
c = int(input("Nhập vào số thứ ba: "))
while a < 0 or b < 0 or c < 0:
    if a < 0:
        a = int(input("Nhập lại số thứ nhất:"))
    if b < 0:
        b = int(input("Nhập lại số thứ hai:"))
    if c < 0:
        c = int(input("Nhập lại số thứ ba:"))
if a + b > c or a + c > b or b + c > a:
    if a == b == c:
        print("Ba cạnh a,b,c tạo thành tam giác đều")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Ba cạnh a,b,c tạo thành tam giác vuông")
    elif a == b != c or a == c != b or b == c != a:
        print("Ba cạnh a,b,c tạo thành tam giác cân")
    elif (a**2 + b**2== c**2 and a == b != c) or \
         (a**2 + c**2 == b**2 and a == c != b) or \
         (b**2 + c**2 == a**2 and b == c != a):
        print("Ba cạnh a,b,c tạo thành tam giác vuông cân")
    else:
        print("Ba cạnh a,b,c tạo thành tam giác thường")
else:
    print("Ba cạnh a,b,c không là tam giác")
        