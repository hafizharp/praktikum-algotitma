# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:31:44 2022

@author: LENOVO
"""

import calendar
print("Program dapat menentukan jumlah hari di salah satu bulan")
ulang = "y"
while ulang == "y" or ulang == "x": 
    year = int(input("Masukan Tahun yang anda inginkan: ")) 
    month = int(input("Masukan Bulan yang anda inginkan: "))
    print("Ada", (calendar.monthrange(year, month)[1]), "Hari di bulan ke",month, "pada tahun",year)
    ulang = input("ketik'y' jika ingin lanjut, ketik 'x' jika stop: ")
    if ulang == "x":
        print("Terimakasih sudah Menggunakan program ini")
        print("programmer : Maulana Hafizh A 064002200034")
        break