from data_loader import betoltes
from datetime import datetime


def main():
    kolcsonzo = betoltes()

    while True:
        print("\n--- Autókölcsönző Rendszer ---")
        print("Kérlek, válassz egy lehetőséget:")
        print("1. Autó bérlése - Adott típusú autót bérelhetsz egy napra")
        print("2. Bérlés lemondása - Lemondhatod egy már meglévő autóbérlésedet")
        print("3. Bérlések listázása - Megtekintheted az aktuális bérléseket")
        print("4. Kilépés - Kilépés a programból")

        valasztas = input("\nÍrd be a választott opció számát: ")

        if valasztas == "1":
            print("\nElérhető autók:")
            for auto in kolcsonzo.autok:
                print(auto.get_auto_info())
            tipus = input("\nMelyik típusú autót szeretnéd bérelni? (Írd be a típus nevét): ")
            datum = datetime.now()
            for auto in kolcsonzo.autok:
                if auto.tipus == tipus:
                    eredmeny = kolcsonzo.auto_berlese(auto, datum)
                    print(eredmeny)
                    break
            else:
                print("Sajnáljuk, ilyen típusú autó jelenleg nem elérhető.")

        elif valasztas == "2":
            rendszam = input("\nAdd meg a lemondani kívánt autó rendszámát: ")
            for auto in kolcsonzo.autok:
                if auto.rendszam == rendszam:
                    print(kolcsonzo.berles_lemondasa(auto))
                    break
            else:
                print("Nincs ilyen rendszámú bérlés az adatbázisban.")

        elif valasztas == "3":
            print("\nAktuális bérlések listája:")
            kolcsonzo.aktualis_berlesek_listazasa()

        elif valasztas == "4":
            print("Kilépés a programból. Viszlát!")
            break

        else:
            print("Érvénytelen választás, kérlek próbáld újra.")


if __name__ == "__main__":
    main()