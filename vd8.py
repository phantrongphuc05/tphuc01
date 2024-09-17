# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:00:50 2024

@author: Admin
"""

count = 0
n = int(input("Nhập vào số lần cần lặp: "))
while (count < n):
    print ("Lần lặp thứ:", count + 1,"\t Biến đếm:",count)
    count +=1
else:
    print("\n Thực hiện lệnh trong else do: ",
          "\n count = ", count, "\n n= ", n, 
          "\n bool (count < n) = ",bool(count<n))