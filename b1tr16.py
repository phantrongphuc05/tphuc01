# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:45:30 2024

@author: Admin
"""

a = float(input("Nhập a: "))
while -99 > a and a > 99:
    a = float(input("Nhập lại a: "))
print("Giá trị đã nhập: ",a)