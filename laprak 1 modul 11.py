# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:28:58 2022

@author: LENOVO
"""

class mahasiswa:
    'common base class for all mahasiswa'
    empcount = 0
    
    def __init__(self, Name, NIM, Angkatan):
        self.Name = Name
        self.NIM = NIM
        self.Angkatan = Angkatan
        mahasiswa.stdCount = +1
    
    def displaymahasiswa(self):
        print ("Nama", self.Name, "NIM", self.NIM, "Angkatan", self.Angkatan)
    
Name = input("Masukkan Nama:")
NIM = input("Masukkan NIM:")
Angkatan = input("Angkatan Tahun:")

std=mahasiswa(Name ,NIM , Angkatan)
std.displaymahasiswa()
print("Total mahasiswa %d" % mahasiswa.stdCount)
    
    
    