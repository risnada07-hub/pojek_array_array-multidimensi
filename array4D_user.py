# ====== DEKLARASI & INISIALISASI array 4D (2x2x3x3) ======
D1 = 2   # dimensi ke-1 (blok)
D2 = 2   # dimensi ke-2 (lapisan)
D3 = 3   # dimensi ke-3 (baris)
D4 = 3   # dimensi ke-4 (kolom)

arr4d = [[[[0] * D4 for _ in range(D3)]
          for _ in range(D2)]
         for _ in range(D1)]   # list 4D, semua 0

# ====== INPUT dari user ======
print(f"Masukkan elemen array 4D ({D1}x{D2}x{D3}x{D4}):")
for a in range(D1):
    for b in range(D2):
        for c in range(D3):
            for d in range(D4):
                arr4d[a][b][c][d] = int(input(
                    f"  arr4d[{a}][{b}][{c}][{d}]: "))

# ====== PROSES: tambah 10 ke tiap elemen ======
for a in range(D1):
    for b in range(D2):
        for c in range(D3):
            for d in range(D4):
                arr4d[a][b][c][d] += 10   # operator +=

# ====== PROSES: cari nilai maksimum ======
maks = arr4d[0][0][0][0]
for a in range(D1):
    for b in range(D2):
        for c in range(D3):
            for d in range(D4):
                if arr4d[a][b][c][d] > maks:
                    maks = arr4d[a][b][c][d]

# ====== OUTPUT ke console ======
print("\n-- Isi Array 4D (setelah +10) --")
for a in range(D1):
    print(f"Blok [{a}]:")
    for b in range(D2):
        print(f"  Lapisan [{b}]:")
        for c in range(D3):
            row = ""
            for d in range(D4):
                row += f"{arr4d[a][b][c][d]:5}"
            print(f"    {row}")
print(f"\nNilai maksimum: {maks}")