# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:49:32 2020

@author: andositopu
"""


kotak = ['1','2','3','4','5','6','7','8','9']
player1 = 'X'
player2 = 'O'
tengah = ()

print ("Selamat Datang di Game Tic-Tac-Tok")
print("Dilakukan dengan 3 cara, Horizontal, Vertikal, dan Diagonal")
print("First X and than O")

while tengah ==""  and player2 < 9:
    print("\n")
    print("%s|%s|%s" % (kotak[0], kotak[1], kotak[2]))
    print("-+-+-")
    print("%s|%s|%s" % (kotak[3], kotak[4], kotak[5]))
    print("-+-+-")
    print("%s|%s|%s" % (kotak[6], kotak[7], kotak[8]))
    
pos = -1
while (pos == -1):
    pos = int(input("\n%s's belok. kemana?: " % player1))
    if pos < 1 or pos > 9 :
        pos = -1
        print("Pilihan Salah! hanya angka 1-9")
        
pos = pos -1
if kotak[pos]== 'X' or kotak[pos]== 'O':
    pos = -1
print("Kotak telah dipilih by%s! coba lagi" % kotak[pos])

kotak[pos] = player1
player2 = player2 +1
baris1 = kotak[0] == player1 and kotak[1] == player1 and kotak[2] == player1
baris2 = kotak[3] == player1 and kotak[4] == player1 and kotak[5] == player1
baris3 = kotak[6] == player1 and kotak[7] == player1 and kotak[8] == player1 

kolom1 = kotak[0] == player1 and kotak[3] == player1 and kotak[6] == player1 
kolom2 = kotak[1] == player1 and kotak[4] == player1 and kotak[7] == player1
kolom3 = kotak[2] == player1 and kotak[5] == player1 and kotak[8] == player1

diagonal1 = kotak[0] == player1 and kotak[4] == player1 and kotak[8] == player1
diagonal2 = kotak[2] == player1 and kotak[4] == player1 and kotak[6] == player1

baris = baris1 or baris2 or baris3
kolom = kolom1 or kolom2 or kolom3
diagonal = diagonal1 or diagonal2

if (baris or kolom or diagonal):
    print("\n")
    print("%s|%s|%s" % (kotak[0], kotak[1], kotak[2]))
    print("-+-+-")
    print("%s|%s|%s" % (kotak[3], kotak[4], kotak[5]))
    print("-+-+-")
    print("%s|%s|%s" % (kotak[6], kotak[7], kotak[8]))
    
    print("Selamat Anda Menang tetapi tidak dapat apa-apa %s! You Won!!!" % player1)
    
    tengah = player1
    if player1 == 'X':
        player1 = 'O'
    else :
        player1 = 'X'
        
    if player2 == 9 and tengah =="" :
        print("Tidak ada yang menang! :( ") 