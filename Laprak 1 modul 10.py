# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:05:57 2022

@author: LENOVO
"""

data_list = [4, 13, 17, 28, 37, 45, 59, 66, 73, 155, 200]
print(data_list)
cari = int(input("Masukkan Angka Yang Anda ingin Cari : "))

def bubble_sort(List,search):
    counter = 0
    while counter != len(data_list):
        if data_list[counter] == search:j
            result = counter
            return result
        counter += 1

hasil = bubble_sort(data_list,cari)
if cari not in data_list:
    print(data_list)
    print("Element tidak ditemukan pada list")
else:
    print(data_list)
    print("Element ditemukan pada posisi ke",hasil+1)