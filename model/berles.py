from datetime import datetime

class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        # A datumot datetime típusúvá alakítjuk, ha még nem az
        self.datum = datum if isinstance(datum, datetime) else datetime.strptime(datum, "%Y-%m-%d")

    def ar_szamolas(self):
        return f"Bérlés ára: {self.auto.berleti_dij} Ft/nap"

    def __str__(self):
        return f"{self.datum.date()} - {self.auto.tipus}, rendszám: {self.auto.rendszam}, bérleti díj: {self.auto.berleti_dij} Ft"