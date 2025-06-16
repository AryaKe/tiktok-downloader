# TikTok HD Video Downloader

**Tools untuk mendownload video TikTok dengan resolusi HD maksimal dan kompatibel dengan semua perangkat**

## 📋 Fitur Utama
- ✅ Mendukung semua jenis URL TikTok (vt.tiktok.com, www.tiktok.com)
- 🎥 Kualitas HD (1080p) dengan fallback ke resolusi terbaik
- 📱 Kompatibel dengan semua perangkat (format MP4 standar)
- 🔄 Multi-API backup system
- 📊 Progress indicator saat download
- 🚀 Cepat dan mudah digunakan

## 🛠️ Tools yang Digunakan
1. **Python 3.8+** - Bahasa pemrograman utama
2. **Requests** - Untuk HTTP requests
3. **Regex** - Untuk ekstraksi video ID
4. **urllib** - Untuk download file
5. **Multi-API System** - 3 sumber API berbeda untuk reliability

## 📥 Instalasi

### Persyaratan:
- Python 3.8 atau versi lebih baru
- Pip (package installer for Python)

### Langkah-langkah:
1. Clone repository atau download script:
   ```bash
   git clone https://github.com/username/tiktok-hd-downloader.git
   cd tiktok-hd-downloader
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. (Opsional) Buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install requests
   ```

## 🚀 Cara Menggunakan

### Basic Usage:
```bash
python tiktok_hd_downloader.py
```

1. Jalankan script
2. Masukkan URL TikTok saat diminta
   ```
   Contoh URL yang didukung:
   - https://vt.tiktok.com/ZSk4o7gUE/
   - https://www.tiktok.com/@username/video/1234567890123456789
   ```
3. Tunggu proses download selesai

### Advanced Usage:
Anda bisa menjalankan langsung dengan URL sebagai argument:
```bash
python tiktok_hd_downloader.py "https://vt.tiktok.com/ZSk4o7gUE/"
```

## 🎯 Output
- Video akan tersimpan dengan format: `tiktok_hd_[VIDEO_ID].mp4`
- Ukuran file dan progress akan ditampilkan selama download
- File tersimpan di direktori yang sama dengan script

## ⚠️ Troubleshooting
Jika mengalami error:
1. Coba gunakan VPN (terutama jika di daerah yang memblokir TikTok)
2. Pastikan URL benar dan video tersedia untuk publik
3. Coba lagi beberapa saat kemudian (API mungkin down sementara)
4. Jika semua gagal, buka issue di GitHub repository

## 📜 Lisensi
Project ini dibawah lisensi MIT - bebas digunakan untuk keperluan pribadi maupun komersial.

---



💡 Tips: Untuk hasil terbaik, gunakan koneksi internet stabil dan pastikan video yang didownload bersifat publik.
