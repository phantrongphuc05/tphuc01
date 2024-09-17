# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:43:02 2024

@author: Admin
"""

ch = (input("Nhập chuỗi: "))
print("Độ dài của chuỗi là: ",len(ch))
đặc_biệt=["!","@","#","$","%","^","&","*","(",")","-","+",".","/"]
đếm_ktdb=0 
đếm_ktt=0
đếm_kts=0
đếm_kth=0
for i in ch:
    if i in đặc_biệt:
        print("Kí tự đặc biệt : ",i,"\t")
        đếm_ktdb += 1
print("Số kí tự đặc biệt: ", đếm_ktdb)
for a in ch:
    if a.islower():
        print("Kí tự chữ cái thường: ", a,"\t")
        đếm_ktt += 1
print("Số kí tự chữ cái thường: ",đếm_ktt)
chữ_số=["0","1","2","3","4","5","6","7","8","9"]
for b in ch:
    if b in chữ_số:
        print("Kí tự chữ số: ",b,"\t")
        đếm_kts += 1
print("Số kí tự chữ số: ",đếm_kts)
for c in ch:
    if c.isupper():
        print("Kí tự in hoa :",c,"\t")
        đếm_kth += 1
print("Số kí tự in hoa: ",đếm_kth)
        

