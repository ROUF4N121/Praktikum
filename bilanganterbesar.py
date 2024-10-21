# Inisialisasi dan membaca input dari pengguna
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
bil3 = int(input("Masukkan bilangan ketiga: "))

# Perbandingan untuk menentukan bilangan terbesar
if bil1 > bil2 and bil1 > bil3:
    print("Bilangan terbesar adalah bilangan pertama:", bil1)
elif bil2 > bil3 and bil2 > bil1:
    print("Bilangan terbesar adalah bilangan kedua:", bil2)
else:
    print("Bilangan terbesar adalah bilangan ketiga:", bil3)