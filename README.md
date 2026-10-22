# Pertemuan 10 - String dan Pengolahan Teks dalam Python

**Nama:** Indah Palupi Kusumaningrum

**NIM:** 2225250212

**Kelas:** 3F

## 1. Tujuan

Mempelajari penggunaan string dalam Python untuk menyimpan, mengakses, membersihkan, dan mengolah data teks. Pertemuan ini juga mempelajari normalisasi teks menggunakan berbagai method string dan fungsi.

## 2. Materi yang Dipelajari

- Pengenalan string dalam Python.
- Mengakses karakter menggunakan indeks positif dan negatif.
- Mengambil bagian string menggunakan slicing.
- Memahami sifat string yang immutable.
- Menggunakan method `lower()`, `upper()`, `title()`, `capitalize()`, dan `strip()`.
- Mengganti teks menggunakan `replace()`.
- Mencari dan menghitung teks menggunakan `find()` dan `count()`.
- Memecah teks menggunakan `split()`.
- Menggabungkan teks menggunakan `join()`.
- Mengolah string menggunakan fungsi.
- Melakukan normalisasi data nama mahasiswa dan kode kelas.

## 3. Struktur Folder

```text
pertemuan-10-string-NIM/
├── latihan/
│   ├── 01_dasar_string.py
│   ├── 02_indeks_slicing.py
│   ├── 03_method_string.py
│   ├── 04_membersihkan_teks.py
│   ├── 05_split_join.py
│   └── 06_pencarian_kata.py
├── tugas/
│   └── normalisasi_data_mahasiswa.py
├── .gitignore
└── README.md
```

*Catatan: Sesuaikan nama folder dan file di atas dengan struktur proyek yang sebenarnya.*

## 4. Penjelasan Latihan

### A. Dasar String
Mempelajari cara membuat string, menampilkan teks, menghitung panjang string, serta mengubah huruf menjadi huruf besar dan kecil.

### B. Indeks dan Slicing
Mempelajari cara mengakses karakter berdasarkan indeks dan mengambil sebagian teks menggunakan slicing.

### C. Method String
Menggunakan method seperti `strip()`, `title()`, dan `upper()` untuk mengolah teks.

### D. Membersihkan Teks
Mempelajari cara membersihkan spasi berlebih dan membuat format teks lebih konsisten.

### E. Split dan Join
Menggunakan `split()` untuk memisahkan teks menjadi beberapa kata dan `join()` untuk menggabungkannya kembali.

### F. Pencarian Kata
Menggunakan operator `in`, method `find()`, dan `count()` untuk mencari serta menghitung kemunculan kata dalam teks.

## 5. Tugas Normalisasi Data Mahasiswa

File program:

`tugas/normalisasi_data_mahasiswa.py`

Program ini digunakan untuk membersihkan dan menormalisasi nama mahasiswa serta kode kelas yang memiliki format penulisan tidak konsisten.

### Fitur Program

1. Menerima input nama lengkap mahasiswa.
2. Menghapus spasi berlebih di awal dan akhir nama.
3. Mengubah nama menjadi format title case.
4. Menerima input kode kelas dan mengubahnya menjadi huruf kapital.
5. Mengganti spasi pada kode kelas dengan tanda hubung.
6. Menghitung jumlah kata dalam nama mahasiswa.
7. Membuat inisial dari huruf pertama setiap kata.
8. Menampilkan hasil normalisasi secara rapi.

### Fungsi yang Digunakan

- `normalisasi_nama(nama)` untuk membersihkan dan menormalkan nama.
- `buat_inisial(nama)` untuk membuat inisial mahasiswa.
- `normalisasi_kode(kode)` untuk menormalkan format kode kelas.

## 6. Contoh Input dan Output

### Input

```text
Nama:   Indah
Kode kelas: pmat a 2026
```

### Output

```text
Nama bersih : Indah
Kode kelas  : PMAT-A-2026
Jumlah kata : 1
Inisial     : I
```

## 7. Cara Menjalankan Program

Pastikan Python sudah terpasang dan proyek telah dibuka di Visual Studio Code.

Jalankan program dengan perintah berikut dari folder utama proyek:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

Jika perintah `python` tidak berfungsi, coba:

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

## 8. Pengujian Program

Program diuji menggunakan beberapa variasi input untuk memastikan normalisasi nama, kode kelas, jumlah kata, dan inisial berjalan dengan benar.

| Nama Input | Kode Kelas Input | Nama Bersih | Kode Kelas Bersih | Inisial |
|---|---|---|---|---|
| `aan hendrayana` | `pmat a 2026` | Aan Hendrayana | PMAT-A-2026 | AH |
| `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah | KELAS-B | FM |
| `BUDI` | `pmtk 01` | Budi | PMTK-01 | B |
| `siti nur aisyah` | `kelas c` | Siti Nur Aisyah | KELAS-C | SNA |

## 9. Kesimpulan

Melalui Pertemuan 10, saya mempelajari cara menggunakan string untuk mengolah data teks dalam Python. Saya memahami penggunaan indeks, slicing, method string, `split()`, `join()`, serta fungsi untuk melakukan normalisasi teks.

Materi ini diterapkan dalam program normalisasi data mahasiswa untuk menghasilkan nama, kode kelas, jumlah kata, dan inisial dengan format yang konsisten.

## 10. Dokumentasi Git dan GitHub

Proyek dikelola menggunakan Git dan diunggah ke GitHub sebagai dokumentasi hasil latihan dan tugas.