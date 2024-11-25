#python project
#project 2 : Word guessing game (geuss department's name in ITS)

print("Tebak Nama Departemen di Lingkungan Kampus ITS")
import random

name=input("Siapa nama anda? ") #komputer meminta nama user
print("Selamat bermain, semoga beruntung", name)

#data base nama-nama departemen di ITS
depart=['Fisika','Matematika','Statistika','Kimia','Biologi','Aktuaria','Teknik Mesin','Teknik Kimia',
        'Teknik Fisika','Teknik Sistem dan Industri','Teknik Material','Teknik Sipil','Arsitektur',
        'Teknik Lingkungan','Perencanaan Wilayah dan Kota','Teknik Geopmatika','Teknik Geofisika',
        'Teknik Infrasturktur Sipil','Teknik Mesin Industri','Teknik Elektro Otomasi','Teknik Kimia Industr',
        'Teknik Instrumentasi','Statistika Bisnis','Teknologi Kedokteran','Kedokteran','Pendidikan Profesi Dokter',
        'Teknik Perkapalan','Teknik Sistem Perkapalan','Teknik Kelautan','Teknik Transportasi Laut','Teknik Elektro',
        'Teknik Biomedik','Teknik Komputer','Teknik Informatika','Sistem Informasi','Teknologi Informasi',
        'Desain Produk Industri','Desain Interior','Desain Komunikasi Visual','Manajemen Bisnis','Studi Pembangunan',
        'Manajemen Teknologi']

#komputer akan memilih nama departemen secara random
depart=random.choice(depart)

print("Ayo tebak nama departemen di ITS")
print("Jumlah Karakter : ", len(depart))

tebakan=''
giliran=3

while giliran > 0:

    #perhitungan kegagalan user
    gagal=0

    #semua karakter dari kata yang dimasukan 
    for char in depart:

        if char in tebakan:
            print(char,end=" ")

        else:
            print("_")

        #untuk setiap kegagalan, jumlah kegagaln akan ditambah +1
            gagal +=1

    if gagal==0:
         print("Selamat,Anda Menang!")
        #user akan memenangkan pertandingan jika kegagalan 0
        #dan akan tampil output berikut
         

        #Jawaban benar
         print("Nama Departemen adalah : ", depart)
         break

        #jika user memasukan huruf yanga salah,maka komputer akan meminta user
            #untuk memasukan huruf lainnya
    print()
    tebak=input("tebak huruf : ")

      #setiap karakter yang dimasukan akan disimpan di "tebakan"
    tebakan +=tebak

      #periksa karakter yang dimasukan
    if tebak not in depart:
        giliran-=1

        #jika karakter tidak sesuai dengan depart, maka akan muncul pernyataan salah
        print("Salah")

        #perintah berikut akan menampilkan gilaran yang tersisa
        print("Anda memiliki",+ giliran,'tebakan lagi')

    if giliran==0:
        print("Maaf, Anda kalah")
        print("Nama Departemen adalah : ", depart)
                

