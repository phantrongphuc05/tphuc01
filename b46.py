# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:59:39 2024

@author: Admin
"""
print("Cho phương trình: 2x + 7y +9z = 979 với(x,y,z > 0 )")
tập_nghiệm = []
print("Bộ nghiệm của phương trình là: ")
for x in range(1, (int(979 // 2) + 1)):
    for y in range(1, (int((979 - (2 * x)) // 7)) + 1):
        for z in range(1, (int((979 - (2 * x) - (7 * y)) // 9)) + 1):
            if (2 * x) + (7 * y) + (9 * z) == 979:
                tập_nghiệm += [x, y, z]
                print(f"(x={x}, y={y}, z={z})")
if not tập_nghiệm:
    print("Không có bộ nghiệm nguyên nào thỏa mãn.")