import os
import csv
from . import (
    Mahasiswa,
    RekapKelas,
    build_markdown_report,
    build_html_report,
    save_text,
)

DATA_DIR = "data"
OUT_MD = os.path.join("out", "report.md")
OUT_HTML = os.path.join("out", "report.html")

rk = RekapKelas()

def muat_dari_csv():
    attend_path = os.path.join(DATA_DIR, "attendance.csv")
    grades_path = os.path.join(DATA_DIR, "grades.csv")

    if os.path.exists(attend_path):
        with open(attend_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                nim = (row.get("nim") or "").strip()
                nama = (row.get("nama") or "").strip()
                hadir = row.get("hadir", 0)
                if not nim:
                    continue
                rk.tambah_mahasiswa(Mahasiswa(nim, nama, hadir))
        print("Attendance dimuat.")
    else:
        print("attendance.csv tidak ditemukan (lewati).")

    if os.path.exists(grades_path):
        with open(grades_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                nim = (row.get("nim") or "").strip()
                if not nim:
                    continue
                rk.set_penilaian(
                    nim,
                    quiz=row.get("quiz", 0),
                    tugas=row.get("tugas", 0),
                    uts=row.get("uts", 0),
                    uas=row.get("uas", 0),
                )
        print("Grades dimuat.")
    else:
        print("grades.csv tidak ditemukan (lewati).")

def tambah_mahasiswa():
    nim = input("NIM: ").strip()
    nama = input("Nama: ").strip()
    hadir = input("Hadir (%): ").strip() or "0"
    rk.tambah_mahasiswa(Mahasiswa(nim, nama, hadir))
    print("Mahasiswa ditambahkan.\n")

def ubah_presensi():
    nim = input("NIM: ").strip()
    persen = input("Hadir baru (%): ").strip() or "0"
    if rk.set_hadir(nim, persen):
        print("Presensi diperbarui.\n")
    else:
        print("NIM tidak ditemukan.\n")

def ubah_nilai():
    nim = input("NIM: ").strip()
    if nim not in rk.mhs:
        print("NIM tidak ditemukan.\n")
        return
    quiz = input("Quiz: ").strip() or None
    tugas = input("Tugas: ").strip() or None
    uts = input("UTS: ").strip() or None
    uas = input("UAS: ").strip() or None
    rk.set_penilaian(nim, quiz, tugas, uts, uas)
    print("Nilai diperbarui.\n")

def lihat_rekap():
    rows = rk.rekap()
    if not rows:
        print("(Belum ada data)\n")
        return
    print("== Rekap Nilai ==")
    for r in rows:
        print(f"{r['nim']:>10} | {r['nama']:<20} | Hadir {r['hadir']:5.1f}% | NA {r['nilai_akhir']:6.2f} | {r['predikat']}")
    print("")

def lihat_rekap_below_70():
    rows = rk.rekap_below(70.0)
    if not rows:
        print("(Tidak ada mahasiswa dengan NA < 70)\n")
        return
    print("== Rekap Nilai (< 70) ==")
    for r in rows:
        print(f"{r['nim']:>10} | {r['nama']:<20} | Hadir {r['hadir']:5.1f}% | NA {r['nilai_akhir']:6.2f} | {r['predikat']}")
    print("")

def simpan_markdown():
    content = build_markdown_report(rk.rekap())
    save_text(OUT_MD, content)
    print(f"Laporan Markdown disimpan ke {OUT_MD}\n")

def simpan_html():
    content = build_html_report(rk.rekap())
    save_text(OUT_HTML, content)
    print(f"Laporan HTML disimpan ke {OUT_HTML}\n")

def menu():
    while True:
        print("""
=== Student Performance Tracker (python -m tracker) ===
1) Muat data dari CSV
2) Tambah mahasiswa
3) Ubah presensi
4) Ubah nilai
5) Lihat rekap
6) Lihat rekap (nilai < 70)
7) Simpan Laporan Markdown
8) Simpan Laporan HTML
9) Keluar
""")
        p = input("Pilih [1-9]: ").strip()
        if p == "1":
            muat_dari_csv()
        elif p == "2":
            tambah_mahasiswa()
        elif p == "3":
            ubah_presensi()
        elif p == "4":
            ubah_nilai()
        elif p == "5":
            lihat_rekap()
        elif p == "6":
            lihat_rekap_below_70()
        elif p == "7":
            simpan_markdown()
        elif p == "8":
            simpan_html()
        elif p == "9":
            break
        else:
            print("Pilihan tidak dikenal.\n")

if __name__ == "__main__":
    menu()