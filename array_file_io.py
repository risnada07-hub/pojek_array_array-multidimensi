# ====== DEKLARASI & INISIALISASI ======
N = 4
B, K = 2, 3
arr1d = [0] * N
arr2d = [[0] * K for _ in range(B)]

# ====== INPUT dari file ======
with open("data_input.txt", "r") as f:
    baris = f.read().split()          # baca semua angka

angka = [int(x) for x in baris]      # konversi ke int

for i in range(N):
    arr1d[i] = angka[i]               # isi array 1D dari file

idx = N
for i in range(B):
    for j in range(K):
        arr2d[i][j] = angka[idx]      # isi array 2D dari file
        idx += 1

# ====== PROSES: kalikan setiap elemen x2 ======
for i in range(N):
    arr1d[i] *= 2                     # operator *=
for i in range(B):
    for j in range(K):
        arr2d[i][j] *= 2

# ====== OUTPUT ke console ======
print("Hasil 1D:", arr1d)
print("Hasil 2D:")
for baris in arr2d:
    print(" ", baris)

# ====== OUTPUT ke file ======
with open("data_output.txt", "w") as f:
    f.write("=== Array 1D ===\n")
    for i, v in enumerate(arr1d):
        f.write(f"arr1d[{i}] = {v}\n")
    f.write("=== Array 2D ===\n")
    for baris in arr2d:
        f.write(" ".join(str(x) for x in baris) + "\n")

print("Output tersimpan di data_output.txt")
