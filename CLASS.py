class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        print(f"Hai! Nama saya {self.nama}, NIM saya {self.nim}")

m1 = Mahasiswa("fajri", "121055520121150")
m2 = Mahasiswa("firman", "121055520121048")

m1.perkenalan()
m2.perkenalan()

print("NIM fajri:", m1.nim)
