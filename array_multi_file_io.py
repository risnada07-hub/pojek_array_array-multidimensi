# ====== DEKLARASI & INISIALISASI array 3D ======
L, B, K = 2, 3, 3
arr3d = [[[0]*K for _ in range(B)] for _ in range(L)]

# ====== INPUT dari file ======
with open("input_multi.txt", "r") as f:
    angka = [int(x) for x in f.read().split()]

idx = 0
for l in range(L):
    for i in range(B):
        for j in range(K):
            arr3d[l][i][j] = angka[idx]
            idx += 1

# ====== PROSES: kurangi rata-rata global ======
total = sum(arr3d[l][i][j]
            for l in range(L)
            for i in range(B)
            for j in range(K))
rata  = total / (L * B * K)   # operator /

for l in range(L):
    for i in range(B):
        for j in range(K):
            arr3d[l][i][j] -= rata   # operator -=

# ====== OUTPUT ke console ======
print("-- Array 3D setelah normalisasi --")
for l in range(L):
    print(f"Lapisan [{l}]:")
    for i in range(B):
        print("  ", [f"{arr3d[l][i][j]:.2f}" for j in range(K)])

# ====== OUTPUT ke file ======
with open("output_multi.txt", "w") as f:
    f.write(f"Rata-rata global: {rata:.2f}\n\n")
    for l in range(L):
        f.write(f"=== Lapisan {l} ===\n")
        for i in range(B):
            baris = " ".join(f"{arr3d[l][i][j]:.2f}"
                             for j in range(K))
            f.write(baris + "\n")
        f.write("\n")
print("Output tersimpan di output_multi.txt")
