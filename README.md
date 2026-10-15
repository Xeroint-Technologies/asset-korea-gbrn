# Belajar Korean — Android + GitHub auto-update

Aplikasi Android Kotlin + Jetpack Compose untuk belajar kosakata Korea. Setelah kosakata diunduh satu kali, data tersimpan di HP dan aplikasi bisa dipakai **offline**.

## Fitur

- Instalasi baru dimulai dengan kosakata kosong.
- Tombol **Cek Update** hanya mengecek versi manifest di GitHub; tidak langsung mengunduh atau mengganti data.
- Jika ada versi baru, aplikasi meminta persetujuan sebelum mengunduh.
- Data yang berhasil diunduh tersimpan lokal untuk penggunaan offline.
- Jika internet mati atau unduhan gagal, data lama tetap aman.
- Progres hafalan dan pilihan kata dipertahankan untuk kosakata yang masih tersedia.
- Pencarian, penandaan hafal, pilihan kata latihan, dan kuis pilihan ganda.

## Cara paling mudah mengganti / menambah kosakata

Edit file **`github-data/vocabulary.csv`**. Kolomnya:

| id | sourceNumber | korean | meaning |
|---:|---:|---|---|
| 1 | 1 | 안녕하세요 | Halo |
| 2 | 2 | 감사합니다 | Terima kasih |

- **Menambah kata:** tambahkan satu baris baru dengan `id` baru.
- **Mengganti kata/arti:** edit kolom `korean` atau `meaning` pada baris tersebut.
- Jangan hapus header kolom paling atas.
- Jika arti berisi koma, editor CSV biasanya akan memberi tanda kutip otomatis.

### Upload perubahan ke GitHub

1. Buka folder `github-data` di repository `asset-korea-gbrn`.
2. Edit `vocabulary.csv` langsung lewat GitHub (ikon pensil), atau upload file CSV yang sudah diedit.
3. Klik **Commit changes** ke branch `main`.
4. Buka tab **Actions** dan tunggu workflow **Buat JSON kosakata dari CSV** selesai.
5. Workflow otomatis membuat `vocabulary.json` dan menaikkan versi di `manifest.json`.
6. Di aplikasi, tekan **Cek Update**. Jika versi baru ditemukan, tekan **Unduh pembaruan**.

File `vocabulary.json` tetap disediakan untuk aplikasi. Sebaiknya jangan mengedit JSON secara manual karena akan dibuat otomatis dari CSV.

## URL yang dipakai aplikasi

Manifest: `https://raw.githubusercontent.com/Xeroint-Technologies/asset-korea-gbrn/main/github-data/manifest.json`

Kosakata: `https://raw.githubusercontent.com/Xeroint-Technologies/asset-korea-gbrn/main/github-data/vocabulary.json`

## Struktur file

- `github-data/vocabulary.csv` — sumber utama yang diedit manusia.
- `github-data/vocabulary.json` — data yang dibaca aplikasi; dibuat otomatis dari CSV.
- `github-data/manifest.json` — versi data dan URL JSON.
- `tools/csv_to_json.py` — skrip pembuat JSON.
- `.github/workflows/update-vocabulary.yml` — otomatisasi GitHub Actions.
- `app/src/main/assets/vocabulary.json` — sengaja berisi `[]`, agar instalasi baru kosong.

## Menjalankan aplikasi

1. Buka folder `BljrKorean` di Android Studio.
2. Tunggu Gradle Sync.
3. Jalankan konfigurasi `app` di emulator atau HP Android.
4. Untuk membuat APK, pilih **Build > Build Bundle(s) / APK(s) > Build APK(s)**.

Catatan: APK baru pertama kali diinstal memang kosong. Pengguna memerlukan internet satu kali untuk mengunduh kosakata awal; sesudah itu kosakata tersimpan dan dapat digunakan offline.
