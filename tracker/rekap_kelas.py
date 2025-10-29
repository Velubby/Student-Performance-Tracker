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
        if isinstance(mahasiswa, Mahasiswa):
            self.mhs[mahasiswa.nim] = mahasiswa
            if mahasiswa.nim not in self.nilai:
                self.nilai[mahasiswa.nim] = Penilaian()
            return True
        return False

    def set_hadir(self, nim, persen):
        if nim in self.mhs:
            self.mhs[nim].hadir_persen = persen
            return True
        return False

    def set_penilaian(self, nim, quiz=None, tugas=None, uts=None, uas=None):
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
        if skor >= 80: return "A"
        if skor >= 70: return "B"
        if skor >= 60: return "C"
        if skor >= 50: return "D"
        return "E"

    def _row(self, nim):
        m = self.mhs[nim]
        p = self.nilai.get(nim, Penilaian())
        na = p.nilai_akhir()
        return {
            "nim": m.nim,
            "nama": m.nama,
            "hadir": m.hadir_persen,
            "nilai_akhir": na,
            "predikat": self.predikat(na),
        }

    def rekap(self):
        return [self._row(nim) for nim in sorted(self.mhs)]

    def rekap_below(self, threshold):
        """
        Rekap hanya mahasiswa dengan nilai_akhir < threshold.
        """
        rows = []
        for nim in sorted(self.mhs):
            r = self._row(nim)
            if r["nilai_akhir"] < float(threshold):
                rows.append(r)
        return rows