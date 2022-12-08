# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:40:20 2022

@author: LENOVO
"""

def data(nama,Umur,alamat,email,dosenwali):

    file = open('Biodata.txt','w')
    file.write(f'Nama : {nama} \nUmur : {Umur} \nAlamat : {alamat} \nEmail : {email} \nDosen wali : {dosenwali}')
    file.close()
    
def baca():
    file = open('Biodata.txt','r')
    text = file.read()
    print(text)
    file.close()

nama = input('Masukkan Nama: ')
Umur = input('Masukkan Umur: ')
alamat = input('Masukkan alamat: ')
email = input('Masukkan email: ')
dosenwali = input('Masukkan dosen wali: ')
print('\nBerikut biodatamu')
data(nama,Umur,alamat,email,dosenwali)
baca()