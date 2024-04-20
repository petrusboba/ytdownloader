# PLAYME

## Deskripsi
PLAYME adalah program sederhana untuk memainkan lagu dari YouTube menggunakan Python dan pygame.

## Instalasi

### Persyaratan Sistem
- Python 3.12.3 atau versi lebih baru
- pip

### Instalasi Modul
1. Buka terminal atau command prompt.
2. Perbarui pip (opsional):
python -m pip install --upgrade pip

Copy code
atau
python3 -m pip install --upgrade pip

markdown
Copy code
3. Instal modul yang diperlukan:
python -m pip install youtube-search-python pygame youtube_dl

Copy code
atau
python3 -m pip install youtube-search-python pygame youtube_dl

markdown
Copy code

## Penggunaan

1. Jalankan program `playme.py` dengan Python:
python playme.py

Copy code
atau
python3 playme.py

markdown
Copy code
2. Program akan meminta Anda memasukkan judul lagu atau nama artis.
3. Masukkan judul lagu atau nama artis yang ingin Anda dengarkan.
4. Program akan mencari lagu tersebut di YouTube dan memainkannya menggunakan pygame.

## Catatan

- Pastikan Anda terhubung ke internet saat menjalankan program ini.
- Jika Anda mengalami masalah saat mencari atau memainkan lagu, coba perbarui modul `youtube-search-python` dan `youtube_dl` dengan menjalankan perintah:
python -m pip install --upgrade youtube-search-python youtube_dl

Copy code
atau
python3 -m pip install --upgrade youtube-search-python youtube_dl

shell
Copy code

## Lisensi
MIT License
