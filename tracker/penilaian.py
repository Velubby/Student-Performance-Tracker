class Penilaian:
    """
    Objek Penilaian.
    Atribut skor (0-100): quiz, tugas, uts, uas.
    Metode: nilai_akhir() dengan bobot 15%, 25%, 25%, 35%.
    """

    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        self._quiz = 0.0
        self._tugas = 0.0
        self._uts = 0.0
        self._uas = 0.0
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def _bound(self, v):
        try:
            v = float(v)
        except Exception:
            v = 0.0
        if v < 0:
            v = 0.0
        if v > 100:
            v = 100.0
        return v

    @property
    def quiz(self):
        return self._quiz

    @quiz.setter
    def quiz(self, v):
        self._quiz = self._bound(v)

    @property
    def tugas(self):
        return self._tugas

    @tugas.setter
    def tugas(self, v):
        self._tugas = self._bound(v)

    @property
    def uts(self):
        return self._uts

    @uts.setter
    def uts(self, v):
        self._uts = self._bound(v)

    @property
    def uas(self):
        return self._uas

    @uas.setter
    def uas(self, v):
        self._uas = self._bound(v)

    def nilai_akhir(self):
        return (0.15 * self.quiz) + (0.25 * self.tugas) + (0.25 * self.uts) + (0.35 * self.uas)