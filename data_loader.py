from model.autokolcsonzo import AutoKolcsonzo
from model.szemelyauto import Szemelyauto
from model.teherauto import Teherauto
from model.berles import Berles


def betoltes():
    # A példaprojekt inicializálása három autóval és négy bérléssel
    autok = [
        Szemelyauto("ABC-123", "Toyota Corolla", 10000, 5),
        Szemelyauto("DEF-456", "Ford Focus", 12000, 5),
        Teherauto("GHI-789", "Mercedes Sprinter", 15000, 1000)
    ]

    berlesek = [
        Berles(autok[0], "2024-11-10"),
        Berles(autok[1], "2024-11-11"),
        Berles(autok[2], "2024-11-12"),
        Berles(autok[0], "2024-11-13")
    ]

    return AutoKolcsonzo("My Auto Kolcsonzo", autok, berlesek)