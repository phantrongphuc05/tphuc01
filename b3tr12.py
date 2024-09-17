# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:17:14 2024

@author: Admin
"""

import random
danh_sách = ""
for i in range(random.randrange(1, 12)):
    số = random.randrange(20, 31)
    chuỗi = str(số)
    danh_sách = danh_sách + chuỗi + " "
print(danh_sách)
danh_sách = danh_sách[:-1]
x = danh_sách.split(" ")
print(len(x))
bình_phương = ""
bình_phương = [pow(float(i), 2) \
                  for i in range(99) if 18 <= pow(float(i), 2) <= 99]
print("Danh sách các giá trị bình phương:", bình_phương)
if bình_phương:
    giá_trị_ngẫu_nhiên= random.choice(bình_phương)
    print("Giá trị ngẫu nhiên từ danh sách bình phương:", giá_trị_ngẫu_nhiên)