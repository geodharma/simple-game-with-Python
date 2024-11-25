#Python project
#Project 1 : Number guessing game

import random
import math

#masukan input (batas atas & bawah)
bawah=int(input("masukan batas bawah ="))
atas=int(input("masukan batas atas ="))

#membangkitkan bilangan random antara batas bawah dan atas
x=random.randint(bawah,atas)
max_percobaan=math.ceil(math.log(atas-bawah+1,2))
print("\n\tAnda hanya punya",max_percobaan,
      "kesempatan menebak bilanagn bulat!\n")

#Inisialisasi jumlah tebakan
count=0
flag=False

#Jumlah minimum tebakan
while count<max_percobaan:
                  count +=1

                  #angka tebakan
                  tebakan=int(input("Tebak sebuah angka ="))

                  if x==tebakan:
                      print("Selamat anda berhasil menabak dalam",count,"percobaan")
                      flag=True
                      break
                    
                  elif x>tebakan:
                     print("Nilai tebakan anda terlalu kecil!")
                     print("\n\tKesempatan anda tersisa",max_percobaan-count,
                           "percobaan\n")
                  elif x<tebakan:
                     print("Nilai tebakan anda terlalu besar!")
                     ("\n\tKesempatan anda tersisa",max_percobaan-count,
                           "percobaan\n")

#Jika jumlah tebakan melampaui, akan tampil
if not flag:
    print("\nJawabannya adalah %d" % x)
    print("\tSemoga lebih beruntung di kesempatan selanjutnya!")

                     
            

