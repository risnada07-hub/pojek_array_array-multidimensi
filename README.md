# pojek_array_array-multidimensi
# =============================================================
#  main.py  —  Project Array Python Multidimensi
#  Mencakup: Array 1D, 2D, 3D, 4D
#  Input : dari user (keyboard) dan dari file
#  Proses: operator aritmatika (+=, -=, *=, /)
#  Output: ke console dan ke file
# =============================================================


# ==============================================================
# BAGIAN 1 — ARRAY 1 DIMENSI
# ==============================================================

def array_1d_dari_user():
    """Array 1D: input dari user, proses penjumlahan, output console + file."""

    # ====== DEKLARASI variabel array 1 dimensi ======
    UKURAN = 5
    nilai  = [0] * UKURAN          # inisialisasi semua elemen = 0

    # ====== INPUT dari user ======
    print(f"\nMasukkan {UKURAN} nilai untuk Array 1D:")
    for i in range(UKURAN):
        nilai[i] = int(input(f"  nilai[{i}]: "))

    # ====== PROSES: hitung total dan rata-rata ======
    total = 0
    for i in range(UKURAN):
        total += nilai[i]              # operator +=
    rata = total / UKURAN             # operator /

    # ====== OUTPUT ke console ======
    print("\n-- Isi Array 1D --")
    for i in range(UKURAN):
        print(f"  nilai[{i}] = {nilai[i]}")
    print(f"  Total  : {total}")
    print(f"  Rata2  : {rata:.2f}")

    # ====== OUTPUT ke file ======
    with open("data_output.txt", "a") as f:
        f.write("=== Array 1D ===\n")
        for i in range(UKURAN):
            f.write(f"nilai[{i}] = {nilai[i]}\n")
        f.write(f"Total  : {total}\n")
        f.write(f"Rata2  : {rata:.2f}\n\n")
    print("  [Tersimpan di data_output.txt]")


# ==============================================================
# BAGIAN 2 — ARRAY 2 DIMENSI
# ==============================================================

def array_2d_dari_user():
    """Array 2D: input dari user, proses jumlah per baris, output console + file."""

    # ====== DEKLARASI & INISIALISASI array 2 dimensi (matriks 3x3) ======
    BARIS  = 3
    KOLOM  = 3
    matriks = [[0] * KOLOM for _ in range(BARIS)]  # list 2D, semua 0

    # ====== INPUT dari user ======
    print(f"\nMasukkan elemen matriks {BARIS}x{KOLOM} untuk Array 2D:")
    for i in range(BARIS):
        for j in range(KOLOM):
            matriks[i][j] = int(input(f"  matriks[{i}][{j}]: "))

    # ====== PROSES: hitung jumlah per baris ======
    jumlah_baris = []
    for i in range(BARIS):
        s = 0
        for j in range(KOLOM):
            s += matriks[i][j]         # operator +=
        jumlah_baris.append(s)

    # ====== OUTPUT ke console ======
    print("\n-- Isi Matriks 2D --")
    for i in range(BARIS):
        row = "  ".join(f"{matriks[i][j]:4}" for j in range(KOLOM))
        print(f"  [{row}]  jumlah = {jumlah_baris[i]}")

    # ====== OUTPUT ke file ======
    with open("data_output.txt", "a") as f:
        f.write("=== Array 2D ===\n")
        for i in range(BARIS):
            row = " ".join(str(matriks[i][j]) for j in range(KOLOM))
            f.write(f"Baris {i}: {row}  (jumlah={jumlah_baris[i]})\n")
        f.write("\n")
    print("  [Tersimpan di data_output.txt]")


# ==============================================================
# BAGIAN 3 — ARRAY 3 DIMENSI (Input User)
# ==============================================================

def array_3d_dari_user():
    """Array 3D: input dari user, proses kalikan x2, hitung total, output console + file."""

    # ====== DEKLARASI & INISIALISASI array 3 dimensi (2x3x4) ======
    LAPISAN = 2
    BARIS   = 3
    KOLOM   = 4
    arr3d   = [[[0] * KOLOM for _ in range(BARIS)]
               for _ in range(LAPISAN)]     # list 3D, semua 0

    # ====== INPUT dari user ======
    print(f"\nMasukkan elemen Array 3D ({LAPISAN}x{BARIS}x{KOLOM}):")
    for l in range(LAPISAN):
        for i in range(BARIS):
            for j in range(KOLOM):
                arr3d[l][i][j] = int(input(
                    f"  arr3d[{l}][{i}][{j}]: "))

    # ====== PROSES: kalikan setiap elemen x2 ======
    for l in range(LAPISAN):
        for i in range(BARIS):
            for j in range(KOLOM):
                arr3d[l][i][j] *= 2        # operator *=

    # ====== PROSES: hitung total semua elemen ======
    total = 0
    for l in range(LAPISAN):
        for i in range(BARIS):
            for j in range(KOLOM):
                total += arr3d[l][i][j]    # operator +=

    # ====== OUTPUT ke console ======
    print("\n-- Isi Array 3D (setelah x2) --")
    for l in range(LAPISAN):
        print(f"  Lapisan [{l}]:")
        for i in range(BARIS):
            row = "".join(f"{arr3d[l][i][j]:6}" for j in range(KOLOM))
            print(f"    [{row}]")
    print(f"  Total semua elemen: {total}")

    # ====== OUTPUT ke file ======
    with open("data_output.txt", "a") as f:
        f.write("=== Array 3D (setelah x2) ===\n")
        for l in range(LAPISAN):
            f.write(f"Lapisan {l}:\n")
            for i in range(BARIS):
                row = " ".join(str(arr3d[l][i][j]) for j in range(KOLOM))
                f.write(f"  {row}\n")
        f.write(f"Total: {total}\n\n")
    print("  [Tersimpan di data_output.txt]")


# ==============================================================
# BAGIAN 4 — ARRAY 4 DIMENSI (Input User)
# ==============================================================

def array_4d_dari_user():
    """Array 4D: input dari user, proses tambah 10, cari maksimum, output console + file."""

    # ====== DEKLARASI & INISIALISASI array 4 dimensi (2x2x3x3) ======
    D1   = 2
    D2   = 2
    D3   = 3
    D4   = 3
    arr4d = [[[[0] * D4 for _ in range(D3)]
              for _ in range(D2)]
             for _ in range(D1)]           # list 4D, semua 0

    # ====== INPUT dari user ======
    print(f"\nMasukkan elemen Array 4D ({D1}x{D2}x{D3}x{D4}):")
    for a in range(D1):
        for b in range(D2):
            for c in range(D3):
                for d in range(D4):
                    arr4d[a][b][c][d] = int(input(
                        f"  arr4d[{a}][{b}][{c}][{d}]: "))

    # ====== PROSES: tambah 10 ke setiap elemen ======
    for a in range(D1):
        for b in range(D2):
            for c in range(D3):
                for d in range(D4):
                    arr4d[a][b][c][d] += 10    # operator +=

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
        print(f"  Blok [{a}]:")
        for b in range(D2):
            print(f"    Lapisan [{b}]:")
            for c in range(D3):
                row = "".join(f"{arr4d[a][b][c][d]:5}" for d in range(D4))
                print(f"      [{row}]")
    print(f"  Nilai maksimum: {maks}")

    # ====== OUTPUT ke file ======
    with open("data_output.txt", "a") as f:
        f.write("=== Array 4D (setelah +10) ===\n")
        for a in range(D1):
            f.write(f"Blok {a}:\n")
            for b in range(D2):
                f.write(f"  Lapisan {b}:\n")
                for c in range(D3):
                    row = " ".join(str(arr4d[a][b][c][d]) for d in range(D4))
                    f.write(f"    {row}\n")
        f.write(f"Nilai maksimum: {maks}\n\n")
    print("  [Tersimpan di data_output.txt]")


# ==============================================================
# BAGIAN 5 — ARRAY 3D dari FILE (Input/Output File)
# ==============================================================

def array_3d_dari_file():
    """Array 3D: input dari file, proses normalisasi (-rata2), output console + file."""

    # ====== DEKLARASI & INISIALISASI array 3D ======
    L = 2
    B = 3
    K = 3
    arr3d = [[[0] * K for _ in range(B)] for _ in range(L)]   # list 3D, semua 0

    # ====== INPUT dari file ======
    try:
        with open("input_multi.txt", "r") as f:
            angka = [int(x) for x in f.read().split()]
    except FileNotFoundError:
        print("\n  [ERROR] File 'input_multi.txt' tidak ditemukan.")
        print("  Buat file dengan 18 angka, contoh:")
        print("  1 2 3 4 5 6 7 8 9")
        print("  10 11 12 13 14 15 16 17 18")
        return

    idx = 0
    for l in range(L):
        for i in range(B):
            for j in range(K):
                arr3d[l][i][j] = angka[idx]
                idx += 1

    # ====== PROSES: hitung rata-rata global, lalu kurangi tiap elemen ======
    total = 0
    for l in range(L):
        for i in range(B):
            for j in range(K):
                total += arr3d[l][i][j]    # operator +=
    rata = total / (L * B * K)             # operator /

    for l in range(L):
        for i in range(B):
            for j in range(K):
                arr3d[l][i][j] -= rata     # operator -=

    # ====== OUTPUT ke console ======
    print(f"\n-- Array 3D setelah normalisasi (rata-rata global = {rata:.2f}) --")
    for l in range(L):
        print(f"  Lapisan [{l}]:")
        for i in range(B):
            row = "  ".join(f"{arr3d[l][i][j]:7.2f}" for j in range(K))
            print(f"    [{row}]")

    # ====== OUTPUT ke file ======
    with open("output_multi.txt", "w") as f:
        f.write(f"Rata-rata global: {rata:.2f}\n\n")
        for l in range(L):
            f.write(f"=== Lapisan {l} ===\n")
            for i in range(B):
                row = " ".join(f"{arr3d[l][i][j]:.2f}" for j in range(K))
                f.write(row + "\n")
            f.write("\n")
    print("  [Tersimpan di output_multi.txt]")


# ==============================================================
# MAIN — MENU UTAMA
# ==============================================================

def main():
    # Bersihkan file output di awal
    with open("data_output.txt", "w") as f:
        f.write("=== OUTPUT PROGRAM ARRAY PYTHON ===\n\n")

    while True:
        print("\n" + "=" * 38)
        print("   MENU PROGRAM ARRAY MULTIDIMENSI")
        print("   Universitas Dinamika — Latihan 7")
        print("=" * 38)
        print("  1. Array 1D  — Input dari user")
        print("  2. Array 2D  — Input dari user")
        print("  3. Array 3D  — Input dari user")
        print("  4. Array 4D  — Input dari user")
        print("  5. Array 3D  — Input dari file")
        print("  0. Keluar")
        print("=" * 38)
        pilihan = input("Pilih menu: ").strip()

        if   pilihan == "1": array_1d_dari_user()
        elif pilihan == "2": array_2d_dari_user()
        elif pilihan == "3": array_3d_dari_user()
        elif pilihan == "4": array_4d_dari_user()
        elif pilihan == "5": array_3d_dari_file()
        elif pilihan == "0":
            print("\nProgram selesai. Terima kasih!\n")
            break
        else:
            print("  Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
