# Student Performance Tracker

Aplikasi konsol untuk mengelola data mahasiswa dan penilaian (OOP + modular) serta membuat laporan rekap dalam format Markdown dan HTML.

## Fitur
- Mahasiswa: nim, nama, hadir_persen (validasi 0–100 via property).
- Penilaian: quiz, tugas, uts, uas (validasi 0–100).
- Bobot Nilai Akhir: quiz 15%, tugas 25%, UTS 25%, UAS 35%.
- RekapKelas: tambah mahasiswa, set presensi/nilai, rekap + predikat (A≥85, B≥75, C≥65, D≥55, E<55).
- Laporan: out/report.md (Markdown) dan out/report.html (HTML).
- Filter cepat: tampilkan rekap mahasiswa dengan nilai akhir < 70.
- Muat data dari CSV (opsional). Tanpa CSV tetap bisa input manual via menu.

## Struktur Proyek
```bash
├─ app.py
├─ tracker/
│  ├─ __init__.py
│  ├─ mahasiswa.py
│  ├─ penilaian.py
│  ├─ rekap_kelas.py
│  └─ report.py
├─ data/                 (opsional)
│  ├─ attendance.csv
│  └─ grades.csv
├─ out/                  (dibuat otomatis saat simpan laporan)
│  └─ report.md
└─ README.md
```

## Menjalankan
1) (Opsional) Siapkan CSV di folder data/.
2) Jalankan sebagai paket :
    ```python -m tracker```
3) Jalankan skrip CLI :
    ```python app.py```

### Menu
- 1 Muat data dari CSV
- 2 Tambah mahasiswa
- 3 Ubah presensi
- 4 Ubah nilai
- 5 Lihat rekap
- 6 Lihat rekap (nilai < 70)
- 7 Simpan Laporan Markdown
- 8 Simpan Laporan HTML
- 9 Keluar

## Format CSV (opsional)
attendance.csv
```bash
nim,nama,hadir
230110001,Ana,92
230110002,Bimo,60
230110003,Cici,100
230110004,Dio,70
```

grades.csv
```bash
nim,quiz,tugas,uts,uas
230110001,88,90,85,95
230110002,70,65,60,62
230110003,95,94,92,96
230110004,55,75,70,80
```

## Output yang Dihasilkan
Markdown (out/report.md) contoh:
    # Rekap Nilai Mahasiswa

    | NIM | Nama | Hadir (%) | Nilai Akhir | Predikat |
    |----|------|-----------:|------------:|:--------:|
    | 230110001 | Ana  | 92.0 | 89.75 | A |
    | 230110002 | Bimo | 60.0 | 63.25 | C |

HTML (out/report.html) berisi tabel dengan pewarnaan predikat.

## Catatan Implementasi
- Enkapsulasi memakai property getter/setter untuk validasi nilai/presensi.
- RekapKelas.rekap() mengembalikan list of dict: nim, nama, hadir, nilai_akhir, predikat.
- Modul report: build_markdown_report(records), build_html_report(records), save_text(path, content).

## Checklist Submit
- Struktur paket benar dan tracker/__init__.py mengekspor simbol.
- python app.py berjalan tanpa error.
- out/report.md terbentuk saat menyimpan.
- README.md disertakan.
- (Opsional) data/ berisi contoh CSV kecil untuk memudahkan penguji.
