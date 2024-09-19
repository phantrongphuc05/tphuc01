# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:04:27 2024

@author: Admin
"""
tổng_chẵn = 0
tổng_lẻ = 0
for i in range(0, 101):
    if i % 2 == 0:
        tổng_chẵn += i
    else:
        tổng_lẻ += i
        print("Tổng các số chẵn là:",tổng_chẵn)
        print("Tổng các số lẻ là:",tổng_lẻ)
        