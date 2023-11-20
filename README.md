# Aplikasi Kasir Sederhana

Aplikasi ini adalah sistem kasir sederhana yang dirancang menggunakan bahasa pemrograman Python. Aplikasi ini memiliki tiga modul utama: Admin, Kasir, dan Pembeli. Modul Admin bertanggung jawab untuk manajemen data kasir, sedangkan modul Kasir digunakan untuk manajemen data barang. Modul Pembeli menyajikan daftar barang untuk pembeli.

## Struktur Kode

- `Node`: Kelas ini digunakan untuk membuat simpul dalam linked list.
  
- `Data_Kasir`: Kelas ini digunakan untuk menyimpan data kasir, termasuk ID, nama, dan password.

- `LL_Admin`: Kelas ini merupakan linked list yang menyimpan data kasir untuk modul Admin. Berisi fungsi-fungsi untuk menambah, menghapus, dan mengupdate data kasir.

- `Barang`: Kelas ini digunakan untuk menyimpan data barang, termasuk ID, nama, jumlah, dan harga.

- `LL_kasir`: Kelas ini merupakan linked list yang menyimpan data barang untuk modul Kasir. Berisi fungsi-fungsi untuk menambah, menghapus, dan mengupdate data barang.

- `menu_admin()`: Fungsi ini menampilkan menu dan fitur yang dapat diakses oleh Admin, seperti menambah, menampilkan, mengupdate, dan menghapus data kasir.

- `menu_kasir()`: Fungsi ini menampilkan menu dan fitur yang dapat diakses oleh Kasir, seperti menambah, menampilkan, mengupdate, dan menghapus data barang.

- `menu_pembeli()`: Fungsi ini menampilkan daftar barang untuk Pembeli dan meminta input untuk memilih barang.

- Program utama: Terdapat loop utama yang menampilkan menu utama dan memanggil fungsi-fungsi yang sesuai berdasarkan pilihan pengguna.

## Cara Menjalankan Aplikasi

1. Pastikan Anda memiliki Python terinstal di komputer Anda. Jika belum, Anda dapat mengunduhnya dari [situs resmi Python](https://www.python.org/).

2. Salin kode aplikasi dari file `KasirLinkedList.py` ke editor teks atau lingkungan pengembangan Python.

3. Jalankan program dengan membuka terminal atau command prompt, lalu masuk ke direktori tempat Anda menyimpan file `KasirLinkedList.py`. Ketik perintah berikut:

    ```bash
    python KasirLinkedList.py
    ```

4. Ikuti instruksi yang muncul di layar untuk menggunakan aplikasi.

## Fitur

- **Admin**: Menambah, menampilkan, mengupdate, dan menghapus data kasir.
  
- **Kasir**: Menambah, menampilkan, mengupdate, dan menghapus data barang.

- **Pembeli**: Melihat daftar barang dan memilih barang untuk pembelian.

## Catatan

- Pastikan untuk memasukkan input yang sesuai dengan instruksi yang diberikan oleh aplikasi.

- Aplikasi ini bersifat sederhana dan dapat diperluas sesuai kebutuhan pengguna.

Selamat menggunakan Aplikasi Kasir Sederhana!
