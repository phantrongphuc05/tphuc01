# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:52:11 2024

@author: Admin
"""

time = input("Nhập ngày tháng năm: ")
day, month, year = time.split("/")
day = int(day)
month = int(month)
year = int(year)
nhuận = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {month} có 31 ngày")
elif month in [4, 6, 9, 11]:
    print(f"Tháng {month} có 30 ngày")
elif month == 2:
    if nhuận:
        print("Tháng", month, "có 29 ngày")
    else:
        print("Tháng", month, "có 28 ngày")