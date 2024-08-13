![Preview](https://github.com/dypras666/PrinterQueueCleaner/blob/main/preview.png)
# Pembersih Antrian Printer WINDOWS 7,8,10,11

## Deskripsi

Aplikasi berbasis GUI sederhana menggunakan Python dan Tkinter untuk menghapus antrian printer pada sistem Windows. Aplikasi ini akan menampilkan daftar printer yang terdeteksi, statusnya (online/offline), dan memungkinkan pengguna untuk menghapus semua antrian cetak dengan sekali klik.

## Fitur

* Menampilkan daftar printer beserta statusnya
* Menghapus semua antrian cetak pada sistem
* Refresh daftar printer
* Hak akses administrator (akan meminta elevasi jika diperlukan)
* Antarmuka pengguna grafis yang sederhana

## Prasyarat

* Python 3.x
* Modul `tkinter`, `subprocess`, `os`, `ctypes`, `sys`, `win32print`, `threading`, `time`
* Akses administrator pada sistem Windows

## Cara Menjalankan

1. Pastikan Terinstall Python 3.x terinstal.
2. Install modul yang diperlukan dengan menjalankan perintah berikut di terminal:

   ```bash
   pip install tkinter subprocess os ctypes sys win32print threading time
   ```
3. Clone atau download repositori ini.
4. RUN 
  ```bash 
  py main.py
  ```

**Notes**

Aplikasi ini memerlukan hak akses administrator untuk menjalankan fungsi penghapusan antrian cetak.
Pastikan Anda menutup semua aplikasi yang sedang menggunakan printer sebelum menjalankan proses penghapusan antrian.
Gunakan dengan hati-hati, karena menghapus antrian cetak dapat mengganggu proses pencetakan yang sedang berjalan.

**Jangan Lupa**

Fork dan Star repositori ini jika Anda merasa bermanfaat.
Follow instagram.com/sedotphp untuk update dan proyek menarik lainnya!
Lisensi

Proyek ini dilisensikan di bawah MIT License. Silakan lihat file LICENSE untuk detail lebih lanjut.

**Kontribusi**

Pull request dipersilakan. Untuk perubahan besar, silakan buka issue terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.

Developer : instagram.com/sedotphp | tiktok.com/@devepras
Developer tidak bertanggung jawab atas segala kerusakan atau kehilangan data yang mungkin terjadi akibat penggunaan aplikasi ini. Gunakan dengan risiko Anda sendiri.





