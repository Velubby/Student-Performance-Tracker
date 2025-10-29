from tracker.mahasiswa import Mahasiswa
from tracker.penilaian import Penilaian
from tracker.rekap_kelas import RekapKelas
from tracker.report import build_markdown_report, save_text

if __name__ == "__main__":
    rk = RekapKelas()
    rk.tambah_mahasiswa(Mahasiswa("230110001", "Ana", 92))
    rk.tambah_mahasiswa(Mahasiswa("230110002", "Bimo", 60))
    rk.set_penilaian("230110001", quiz=88, tugas=90, uts=85, uas=95)
    rk.set_penilaian("230110002", quiz=70, tugas=65, uts=60, uas=62)

    records = rk.rekap()
    md = build_markdown_report(records)
    save_text("out/report.md", md)
    print("Laporan tersimpan di out/report.md")