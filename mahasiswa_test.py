# ===== PENGUJI OTOMATIS =====
# Letakkan file ini di folder yang sama dengan mahasiswa.py
# Jalankan: python test_mahasiswa.py

from mahasiswa import Mahasiswa

lolos = 0
gagal = 0


def periksa(keterangan, fungsi, harapan):
    global lolos, gagal
    try:
        hasil = fungsi()
    except Exception as e:
        print("  GAGAL  ", keterangan, "-> program error:",
              type(e).__name__, e)
        gagal = gagal + 1
        return

    if hasil == harapan:
        print("  LULUS  ", keterangan, "->", repr(hasil))
        lolos = lolos + 1
    else:
        print("  GAGAL  ", keterangan, "-> dapat", repr(hasil),
              ", harusnya", repr(harapan))
        gagal = gagal + 1


def baru(nama, daftar):
    m = Mahasiswa(nama)
    for n in daftar:
        m.tambah_nilai(n)
    return m


print("--- Pembuatan objek ---")
periksa('Mahasiswa("Budi").nama', lambda: Mahasiswa("Budi").nama, "Budi")
periksa('Mahasiswa("Budi").nilai', lambda: Mahasiswa("Budi").nilai, [])

print()
print("--- tambah_nilai ---")
periksa("tambah 3 nilai", lambda: baru("Budi", [80, 90, 70]).nilai, [80, 90, 70])
periksa("jumlah_nilai()", lambda: baru("Budi", [80, 90, 70]).jumlah_nilai(), 3)

print()
print("--- rata_rata ---")
periksa("rata [80, 90, 70]", lambda: baru("A", [80, 90, 70]).rata_rata(), 80.0)
periksa("rata [50]", lambda: baru("A", [50]).rata_rata(), 50.0)
periksa("rata kosong", lambda: baru("A", []).rata_rata(), 0)

print()
print("--- tertinggi ---")
periksa("tertinggi [80, 90, 70]", lambda: baru("A", [80, 90, 70]).tertinggi(), 90)
periksa("tertinggi [70, 60, 90]", lambda: baru("A", [70, 60, 90]).tertinggi(), 90)
periksa("tertinggi negatif", lambda: baru("A", [-5, -12, -3]).tertinggi(), -3)
periksa("tertinggi seri", lambda: baru("A", [40, 40]).tertinggi(), 40)
periksa("tertinggi kosong", lambda: baru("A", []).tertinggi(), None)

print()
print("--- lulus ---")
periksa("lulus [80, 90]", lambda: baru("A", [80, 90]).lulus(), True)
periksa("lulus [60]", lambda: baru("A", [60]).lulus(), True)
periksa("lulus [50, 40]", lambda: baru("A", [50, 40]).lulus(), False)
periksa("lulus kosong", lambda: baru("A", []).lulus(), False)

print()
print("--- __str__ ---")
periksa("str 3 nilai", lambda: str(baru("Budi", [80, 90, 70])), "Budi (3 nilai)")
periksa("str kosong", lambda: str(baru("Siti", [])), "Siti (0 nilai)")

print()
print("--- Objek harus terpisah ---")
def terpisah():
    a = Mahasiswa("A")
    b = Mahasiswa("B")
    a.tambah_nilai(100)
    return b.nilai
periksa("nilai tidak tercampur", terpisah, [])

print()
print("====================================")
print("  LULUS :", lolos)
print("  GAGAL :", gagal)
print("  NILAI :", round(lolos / (lolos + gagal) * 100), "/ 100")
print("====================================")