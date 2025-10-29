from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """
    Manajer rekap: menyimpan banyak Mahasiswa dan Penilaian.
    Struktur:
      - self.mhs   : dict[nim] -> Mahasiswa
      - self.nilai : dict[nim] -> Penilaian
    """

    def __init__(self):
        self.mhs = {}
        self.nilai = {}

    def tambah_mahasiswa(self, mahasiswa):
        """Tambahkan satu objek Mahasiswa ke rekap."""
        if isinstance(mahasiswa, Mahasiswa):
            self.mhs[mahasiswa.nim] = mahasiswa
            if mahasiswa.nim not in self.nilai:
                self.nilai[mahasiswa.nim] = Penilaian()
            return True
        return False

    def set_hadir(self, nim, persen):
        """Atur persentase hadir mahasiswa tertentu."""
        if nim in self.mhs:
            self.mhs[nim].hadir_persen = persen
            return True
        return False

    def set_penilaian(self, nim, quiz=None, tugas=None, uts=None, uas=None):
        """Perbarui skor penilaian untuk nim tertentu (optional field)."""
        if nim not in self.mhs:
            return False
        if nim not in self.nilai:
            self.nilai[nim] = Penilaian()
        p = self.nilai[nim]
        if quiz is not None: p.quiz = quiz
        if tugas is not None: p.tugas = tugas
        if uts is not None: p.uts = uts
        if uas is not None: p.uas = uas
        return True

    def predikat(self, skor):
        """Konversi skor ke huruf A-E."""
        if skor >= 85: return "A"
        if skor >= 75: return "B"
        if skor >= 65: return "C"
        if skor >= 55: return "D"
        return "E"

    def rekap(self):
        """Kembalikan list of dict berisi ringkasan tiap mahasiswa."""
        rows = []
        for nim in sorted(self.mhs):
            m = self.mhs[nim]
            p = self.nilai.get(nim, Penilaian())
            na = p.nilai_akhir()
            rows.append({
                "nim": m.nim,
                "nama": m.nama,
                "hadir": m.hadir_persen,
                "nilai_akhir": na,
                "predikat": self.predikat(na),
            })
        return rows