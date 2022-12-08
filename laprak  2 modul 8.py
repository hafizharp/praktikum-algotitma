# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:28:14 2022

@author: LENOVO
"""

def latihan2():
    print()
    print("Ini merupakan program pemangkatan negatif dan positif, Tekan enter untuk berhenti")
    data1 = input("Masukkan Angka: ")
    if data1 == '':
        print("Terima Kasih telah menggunakan Program ini. Program selesai")
        print()
        return 0
    data2 = input("Masukkan Pangkatnya: ")
    eksekusi = int(data1)**int(data2)
    print("Hasilnya adalah: ",eksekusi)
    latihan2()

latihan2()
