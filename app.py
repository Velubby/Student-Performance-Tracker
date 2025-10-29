from tracker.mahasiswa import Mahasiswa
from tracker.penilaian import Penilaian
from tracker.rekap_kelas import RekapKelas

if __name__ == "__main__":
    rk = RekapKelas()
    rk.tambah_mahasiswa(Mahasiswa("230110001", "Ana", 92))
    rk.set_penilaian("230110001", quiz=80, tugas=90, uts=85, uas=95)
    print(rk.rekap())