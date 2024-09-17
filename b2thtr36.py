# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:10:48 2024

@author: Admin
"""

e = input("Nhập vào một email: ")
khoảng_cách = " "
kí_tự = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '.', '/']
tên_đuôi_hợp_lệ = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
if "@" not in e or e.count("@") != 1:
    print("Email không hợp lệ")
else:
    user, tên_đuôi = e.split("@")
    print(user)
    print(tên_đuôi)
    if tên_đuôi not in tên_đuôi_hợp_lệ or len(user) < 6:
        print("email không hợp lệ")
    else:
        for i in user:
            if i == khoảng_cách or i in kí_tự:
                print("Email không hợp lệ")
                break
        else:
            print("Email hợp lệ")