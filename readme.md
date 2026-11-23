# EXAMLAB V31 — Full Project

## Struktur
- `index.html` — file utama untuk menjalankan EXAMLAB.
- `website/EXAMLAB_V31_STANDALONE.html` — salinan sumber standalone.
- `docs/PANDUAN.md` — petunjuk menjalankan dan pemeriksaan.
- `docs/STRUKTUR.md` — penjelasan struktur aplikasi.
- `tools/check-project.py` — audit sederhana file HTML dan JavaScript.

## Menjalankan di Windows
1. Ekstrak ZIP ke folder yang mudah ditemukan.
2. Buka `index.html` dengan Google Chrome atau Microsoft Edge.
3. Login sebagai siswa atau Owner melalui halaman akses.
4. Untuk pengembangan, buka folder hasil ekstrak di Visual Studio Code.

## Catatan arsitektur
Versi ini berasal dari aplikasi HTML standalone. CSS, JavaScript, tampilan, dan data yang tertanam tetap berada di dalam `index.html`, sehingga tidak memerlukan proses build atau server lokal untuk penggunaan dasar.
Jika aplikasi memakai layanan eksternal yang memang sudah tertanam pada kode, koneksi internet mungkin tetap diperlukan.

## Keamanan
Gerbang login pada aplikasi browser standalone merupakan pembatas akses antarmuka, bukan autentikasi server. Jangan gunakan penyimpanan lokal browser untuk menyimpan kata sandi atau data sensitif.
