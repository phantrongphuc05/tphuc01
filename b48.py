# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:45:52 2024

@author: Admin
"""

print("Cho phương trình sau: 2x + 7y + 9z = 979 với x,y,z > 0 và x + y + z lớn nhất")
print("Nghiệm của phương trình là: ")
tập_nghiệm = []
for x in range(1, (int(979 // 2) + 1)):
    for y in range(1, (int(979 - (2*x))//7) + 1):
        for z in range(1, (int(979 - (2*x) - (7*y))//9) + 1):
            if (2*x)+(7*y)+(9*z)==979:
                tập_nghiệm += [[x, y, z]]
                print(f"(x={x}, y={y}, z={z})")
min_nghiệm = tập_nghiệm [0]
min_tổng = sum(min_nghiệm)
for nghiệm in tập_nghiệm:
    tổng = sum(nghiệm)
if tổng < min_tổng:
    min_tổng = tổng
    min_nghiệm = nghiệm
print("Nghiệm nhỏ nhất của phương trình là",min_nghiệm,", với tổng là",min_tổng)