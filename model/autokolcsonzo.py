from .auto import Auto
from .berles import Berles
from datetime import datetime


class AutoKolcsonzo:
    def __init__(self, nev, autok=None, berlesek=None):
        self.nev = nev
        self.autok = autok if autok is not None else []
        self.berlesek = berlesek if berlesek is not None else []

    def auto_berlese(self, auto: Auto, datum):
        datum = datum if isinstance(datum, datetime) else datetime.strptime(datum, "%Y-%m-%d")

        for berles in self.berlesek:
            if berles.auto == auto and berles.datum.date() == datum.date():
                return f"Hiba: Az autó (rendszám: {auto.rendszam}) már ki van bérelve ezen a napon."

        uj_berles = Berles(auto, datum)
        self.berlesek.append(uj_berles)
        return uj_berles.ar_szamolas()

    def berles_lemondasa(self, auto: Auto):
        for berles in self.berlesek:
            if berles.auto == auto:
                self.berlesek.remove(berles)
                return f"Bérlés lemondva: {auto.tipus}, rendszám: {auto.rendszam}."
        return "Nincs ilyen rendszámú bérlés az adatbázisban."

    def aktualis_berlesek_listazasa(self):
        if not self.berlesek:
            print("Nincs aktuális bérlés.")
        else:
            for berles in self.berlesek:
                print(berles)