class Mahasiswa:
    """
    Objek Mahasiswa.
    Atribut: nim (str), nama (str), hadir_persen (0-100).
    """

    def __init__(self, nim, nama, hadir_persen=0.0):
        self._nim = str(nim).strip()
        self._nama = str(nama).strip()
        self._hadir_persen = 0.0
        self.hadir_persen = hadir_persen  # gunakan setter untuk validasi

    @property
    def nim(self):
        return self._nim

    @property
    def nama(self):
        return self._nama

    @property
    def hadir_persen(self):
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        try:
            v = float(value)
        except Exception:
            v = 0.0
        if v < 0:
            v = 0.0
        if v > 100:
            v = 100.0
        self._hadir_persen = v

    def info(self):
        """Profil singkat."""
        return f"{self.nim} - {self.nama} | Hadir {self.hadir_persen:.1f}%"