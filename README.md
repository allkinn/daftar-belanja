# Program Daftar Belanja (Python)

Aplikasi console sederhana untuk mengelola daftar belanja.
User bisa menambah barang, menghapus barang, melihat daftar belanja, dan menyimpan daftar ke file `.txt`.

---

## Fitur

* **Tambah Barang** → masukkan nama barang dan harga.
* **Lihat Daftar Belanja** → tampilkan semua barang yang sudah ditambahkan.
* **Hapus Barang** → pilih nomor barang dari daftar untuk dihapus.
* **Simpan ke File** → daftar belanja disimpan ke file `list_belanja.txt`.
* **Keluar** → program berhenti dengan opsi simpan/hapus file.
* Validasi input → program tetap aman walaupun user salah input.

---

## 🚀 Cara Menjalankan

1. Pastikan Python sudah terinstall.

   ```bash
   python --version
   ```

   Minimal Python **3.6+**.

2. Clone repository atau download file `belanja.py`:

   ```bash
   git clone https://github.com/allkinn/daftar-belanja.git
   ```

3. Jalankan program:

   ```bash
   python belanja.py
   ```

---

## 🖥Contoh Output

```
========== Program Daftar Belanja ==========
--------------------------------------------
******************* Menu *******************
1. Tambah Barang
2. Tampilkan File Saved
3. Keluar
--------------------------------------------
Pilih menu (1-3): 1
ketik 'view' untuk melihat list belanja
--------------------------------------------
Masukkan nama barang ke-1: Indomie
Masukkan harga barang ke-1 (*masukkan tanpa simbol!): 3500
--------------------------------------------
Barang Indomie berhasil ditambahkan.
--------------------------------------------
ketik 'view' untuk melihat list belanja
--------------------------------------------
Masukkan nama barang ke-2: view
--------------------------------------------
------- Berikut daftar  belanja anda -------
1. Indomie - Rp. 3500.0
--------------------------------------------
Ingin menambahkan barang lagi? (y/n): n
--------------------------------------------
Hapus barang atau keluar?:
1. Hapus barang
2. Keluar
--------------------------------------------
```

---

## 🛠Teknologi

* Python (standard library: file handling, input/output, loop).

---

## Kontributor

* [allkinn] (https://github.com/username)

---

