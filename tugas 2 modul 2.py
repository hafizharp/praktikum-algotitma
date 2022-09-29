# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 22:29:43 2022

@author: LENOVO
"""

import math

x1 = float(input("masukkan titik kordinat x garis pertama= "))
y1 = float(input("masukkan titik kordinat y garis pertama= "))

x2 = float(input("masukkan titik kordinat x garis ke dua = "))
y2 = float(input("masukkan titik kordinat y garis ke dua = "))

dlat = x2 - x1
dlon = y2 - y1

a = math.sin(math.radians(dlat/2)) **2 - math.cos(math.radians(x1)) 
math.cos(math.radians(x2)) * math.sin(math.radians(dlon/2)) **2

c = 2 * math.asin(math.sqrt(a))
r = 6371.01

print("jarak antara dua titik adalah" ,c*r , "km")