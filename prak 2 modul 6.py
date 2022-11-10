# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:57:57 2022

@author: LENOVO
"""

def kabisat(tahun):
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def hari(tahun, bulan):
    if bulan > 12 or bulan < 1:
        return "Bulan tidak valid!"
    if bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    if bulan in (4, 6, 9, 11):
        return 30
    else:
        return 31
i=1
while i==1:
    tahun = (input("Masukkan tahun: "))
    bulan = (input("Masukkan bulan: "))
    if tahun=='' or bulan=='':
        i=0
    else:
        tahun=int(tahun)
        bulan=int(bulan)
        days = hari(tahun, bulan)
        print("Jumlah hari:",days)
