from model.auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utasok_szama = utasok_szama

    def get_auto_info(self):
        return f"{self.tipus} (Rendszám: {self.rendszam}, Utasok: {self.utasok_szama}) - {self.berleti_dij} Ft/nap"