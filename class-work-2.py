class Arac:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        print("Marka:", self.marka)
        print("Model:", self.model)
        print("Yıl:", self.yil)

class Araba(Arac):
    def __init__(self, marka, model, yil, motor_hacmi):
        super().__init__(marka, model, yil)
        self.motor_hacmi = motor_hacmi

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("Motor Hacmi:", self.motor_hacmi)

class Kamyon(Arac):
    def __init__(self, marka, model, yil, yuk_kapasitesi):
        super().__init__(marka, model, yil)
        self.yuk_kapasitesi = yuk_kapasitesi

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("Yük Kapasitesi:", self.yuk_kapasitesi)

araba = Araba("Toyota", "Corolla", 2022, "1.6L")
araba.bilgileri_goster()

print()

kamyon = Kamyon("Volvo", "FH16", 2021, "50 ton")
kamyon.bilgileri_goster()
