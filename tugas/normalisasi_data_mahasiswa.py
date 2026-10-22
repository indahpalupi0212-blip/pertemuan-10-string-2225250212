def normalisasi_nama(nama):
    nama_bersih = " ".join(nama.strip().split())
    return nama_bersih.title()


def buat_inisial(nama):
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    inisial = "".join(k[0] for k in kata)
    return inisial


def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    kode_bersih = "-".join(kata)
    return kode_bersih


# Meminta input dari pengguna
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Memproses data
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama)

# Menampilkan hasil
print("\n=== HASIL NORMALISASI DATA MAHASISWA ===")
print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)