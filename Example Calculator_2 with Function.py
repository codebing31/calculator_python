print("=" * 50)
print("Kalkulator")
print("=" * 12)

print("Silakan Masukan Bilangan yang ingin di Operasikan")
bilangan_1 = int(input("Masukan Angka Pertama :"))
bilangan_2 = int(input("Masukan Angka Kedua :"))

def tambah(bilangan_1,bilangan_2):
    return bilangan_1 + bilangan_2

def kurang(bilangan_1,bilangan_2):
    return bilangan_1 - bilangan_2

def kali(bilangan_1,bilangan_2):
    return bilangan_1 * bilangan_2

def bagi(bilangan_1,bilangan_2):
    return bilangan_1 / bilangan_2

print("Hasil Tambah : %d" %tambah(bilangan_1,bilangan_2))
print("Hasil Kurang : %d" %kurang(bilangan_1,bilangan_2))
print("Hasil Kali : %d" %kali(bilangan_1,bilangan_2))
print("Hasil Bagi : %d" %bagi(bilangan_1,bilangan_2))
