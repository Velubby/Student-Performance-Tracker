# Student Performance Tracker

Aplikasi sederhana untuk mengelola data mahasiswa, penilaian, dan membuat laporan rekap dalam format Markdown.

## Struktur
- app.py
- tracker/
  - __init__.py
  - mahasiswa.py
  - penilaian.py
  - rekap_kelas.py
  - report.py
- data/
  - attendance.csv
  - grades.csv
- out/  (otomatis berisi report.md setelah disimpan)

## Cara Menjalankan
1) Pastikan berada di folder proyek.
2) (Opsional) Edit `data/attendance.csv` dan `data/grades.csv`.
3) Jalankan:
4) Di menu:
- 1: Muat data dari CSV
- 2: Tambah mahasiswa
- 3: Ubah presensi
- 4: Ubah nilai
- 5: Lihat rekap
- 6: Simpan Laporan Markdown (ke `out/report.md`)

## Format CSV
- attendance.csv: `nim,nama,hadir`
- grades.csv: `nim,quiz,tugas,uts,uas`

## Catatan
- Nilai divalidasi 0–100 menggunakan property.
- Bobot nilai akhir: quiz 15%, tugas 25%, UTS 25%, UAS 35%.
- Predikat: A>=80, B>=70, C>=60, D>=50, selainnya E.