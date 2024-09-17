# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:14:57 2024

@author: Admin
"""

s = float(input("Nhập quãng đường xe đi(km): "))
while s <= 0:
    s = float("Nhập lại quãng đường: ")
money = 0
if s < 1:
    money += s * 150000
if 2 <= s < 6:
    money += 15000 + ((s - 1) * 13500)
if 6 <= s:
    money += 15000 + 67500 + ((s - 6) * 11000)
if s > 120:
    money *= 0.9
print("Số tiền của bạn là: ", money)