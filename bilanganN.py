# Inisialisasi max dengan nilai sangat kecil
max_value = float('-inf')

while True:
    # Input bilangan dari pengguna
    N = int(input("Masukkan bilangan (ketik 0 untuk selesai): "))
    
    # Jika bilangan adalah 0, keluar dari loop
    if N == 0:
        break
    
    # Jika bilangan lebih besar dari max_value, perbarui max_value
    if N > max_value:
        max_value = N

# Cetak bilangan terbesar yang ditemukan
print("Bilangan terbesar adalah:", max_value)