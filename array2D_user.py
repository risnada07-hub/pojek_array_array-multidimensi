
# ====== DEKLARASI & INISIALISASI array 2D (matriks 3x3) ======
BARIS = 3
KOLOM = 3
matriks = [[0] * KOLOM for _ in range(BARIS)]  # list 2D

# ====== INPUT dari user ======
print(f"Masukkan elemen matriks {BARIS}x{KOLOM}:")
for i in range(BARIS):
    for j in range(KOLOM):
        matriks[i][j] = int(input(f"  matriks[{i}][{j}]: "))

# ====== PROSES: jumlah per baris ======
print("\n-- Jumlah per Baris --")
for i in range(BARIS):
    jumlah = 0
    for j in range(KOLOM):
        jumlah += matriks[i][j]   # operator +=
    print(f"Baris {i}: {jumlah}")

# ====== OUTPUT ke console ======
print("\n-- Isi Matriks 2D --")
for i in range(BARIS):
    for j in range(KOLOM):
        print(f"{matriks[i][j]:4}", end="")
    print()   # pindah baris