from model.auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def get_auto_info(self):
        return f"{self.tipus} (Rendszám: {self.rendszam}, Teherbírás: {self.teherbiras} kg) - {self.berleti_dij} Ft/nap"