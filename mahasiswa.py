class Mahasiswa:

    def __init__(self, nama):
        self.nama = nama
        self.nilai = []

    def tambah_nilai(self, n):
        self.nilai.append(n)

    def jumlah_nilai(self):
        hitung = 0
        for i in self.nilai:
            hitung += 1
        return hitung

    def rata_rata(self):
        if not self.nilai:
            return 0
        total = 0
        for n in self.nilai:
            total += n
        return total / self.jumlah_nilai()

    def tertinggi(self):
        if not self.nilai:
            return None
        tertinggi = self.nilai[0]
        for n in self.nilai:
            if n > tertinggi:
                tertinggi = n
        return tertinggi

    def lulus(self):
        return self.rata_rata() >= 60

    def __str__(self):
        return self.nama + " (" + str(self.jumlah_nilai()) + " nilai)"