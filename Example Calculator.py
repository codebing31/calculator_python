print("=" * 50)
print(" Kalkulator ")
print("=" * 12)
print(" 1. Tambah \t [+]")
print(" 2. Kurang \t [-]")
print(" 3. Kali \t [*]")
print(" 4. Bagi \t [/]")
print(" 5. Pangkat \t [^]")
print("=" * 50)

Operasi = input("Pilih Operasi(1/2/3/4/5):")
if(Operasi == "1"):
    print("User Memilih Penjumlahan")
elif(Operasi == "2"):
    print("User Memilih Pengurangan")
elif(Operasi == "3"):
    print("User Memilih Perkalian")
elif(Operasi == "4"):
    print("User Memilih Pembagian")
elif(Operasi == "5"):
    print("User Memilih Pangkat")
else:
    print("Invalid")
    
Bilangan_1 = eval(input("Masukan Bilangan Pertama : "))
Bilangan_2 = eval(input("Masukan Bilangan Kedua : "))

if(Operasi == "1"):
    hasil = Bilangan_1 + Bilangan_2
    print("Hasil dari operasi",Bilangan_1,"+",Bilangan_2,"=",hasil)
elif(Operasi == "2"):
    hasil = Bilangan_1 - Bilangan_2
    print("Hasil dari operasi",Bilangan_1,"-",Bilangan_2,"=",hasil)
elif(Operasi == "3"):
    hasil = Bilangan_1 * Bilangan_2
    print("Hasil dari operasi",Bilangan_1,"*",Bilangan_2,"=",hasil)
elif(Operasi == "4"):
    hasil = Bilangan_1 / Bilangan_2
    print("Hasil dari operasi",Bilangan_1,"/",Bilangan_2,"=",hasil)
elif(Operasi == "5"):
    hasil = Bilangan_1 ** Bilangan_2
    print("Hasil dari operasi",Bilangan_1,"^",Bilangan_2,"=",hasil)
else:
    print("Invalid")

print("Good Jobs!")
print("=" * 50)

    
