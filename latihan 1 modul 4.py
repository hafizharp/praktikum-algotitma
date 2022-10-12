# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:00:41 2022

@author: LENOVO
"""

n = int(input("masukan nilai:"))
for x in range(n, 0, -1):
    for y in range(x):
        print(x, end ='')
    print('')
