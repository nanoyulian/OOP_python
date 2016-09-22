# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 03:59:36 2016

@author: nano

Membuat simulasi data random berdasarkan probability pada masing2x data
ref:http://stackoverflow.com/questions/19871608/generating-weighted-random-numbers
"""

import random

def sample(totals):
    n = random.uniform(0, totals[-1])
    for i, total in enumerate(totals):
        #print i,":",n,":",total        
        if n <= total:
            return i
"""
membuat samples berdasarkan peluang sebanyak n
@arr_probabilites = Nilai Peluang pada setiap Nilai
@n_simulation = jumlah simulasi yang diinginkan
"""
def create_samples (arr_probabilites,n_simulation):
    totals =  [sum(arr_probabilites[:i+1]) for i in range(len(arr_probabilites))]
    return  [sample(totals) for _ in range(n_simulation)]

"""
Cara Penggunaan : 
Tujuannya generate samples dalam bentuk kumulatif per Nilai (Xi) dgn Peluang tertentu
1. Siapkan distribusi Peluangnya misal : 
   misal X adalah Kejadian munculnya Usia Produktif (27-29)
-----------------------
Indeks   Xi     P(Xi) = 1
-----------------------
0        25      0,10
1        26      0,30
2        27      0,35
3        28      0,15
4        29      0,10

2. Gunakan fungsi create_samples (array_P(Xi), jumlahSimulasi)
3. Hasil dari fungsi create_samples bisa anda gunakan untuk membuat distribusi frekuensi P(Xi)
   untuk melihat bentuk distribusinya.. CMIIW
4. yang digenerate adalah indexnya misal indeks 0=25 , 3=28, 4=29 
"""           
samples = create_samples ([0.1, 0.3, 0.35, 0.15,0.1],1000)
print "Frekuensi Xi: "
print "Jumlah Indeks X=0", ":", samples.count(0)
print "Jumlah Indeks X=1", ":",samples.count(1)
print "Jumlah Indeks X=2", ":",samples.count(2)
print "Jumlah Indeks X=3", ":",samples.count(3)
print "Jumlah Indeks X=3", ":",samples.count(4)
#print samples 
for x in samples:
    print x
    


