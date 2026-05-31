# ====== DEKLARASI & INISIALISASI array 3D (2x3x4) ======
LAPISAN = 2   # dimensi ke-1
BARIS   = 3   # dimensi ke-2
KOLOM   = 4   # dimensi ke-3

arr3d = [[[0] * KOLOM for _ in range(BARIS)]
         for _ in range(LAPISAN)]   # list 3D, semua 0

# ====== INPUT dari user ======
print(f"Masukkan elemen array 3D ({LAPISAN}x{BARIS}x{KOLOM}):")
for l in range(LAPISAN):
    for i in range(BARIS):
        for j in range(KOLOM):
            arr3d[l][i][j] = int(input(
                f"  arr3d[{l}][{i}][{j}]: "))

# ====== PROSES: kalikan elemen * 2 ======
for l in range(LAPISAN):
    for i in range(BARIS):
        for j in range(KOLOM):
            arr3d[l][i][j] *= 2     # operator *=

# ====== PROSES: hitung total semua elemen ======
total = 0
for l in range(LAPISAN):
    for i in range(BARIS):
        for j in range(KOLOM):
            total += arr3d[l][i][j] # operator +=

# ====== OUTPUT ke console ======
print("\n-- Isi Array 3D (setelah x2) --")
for l in range(LAPISAN):
    print(f"  Lapisan [{l}]:")
    for i in range(BARIS):
        row = ""
        for j in range(KOLOM):
            row += f"{arr3d[l][i][j]:6}"
        print(f"    {row}")
print(f"\nTotal semua elemen: {total}")