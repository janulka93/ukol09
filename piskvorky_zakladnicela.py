from random import randrange
DELKA_POLE = 20

SYMBOL_HRACE = "x"
SYMBOL_POCITACE = "o"


def vyhodnot(pole):
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """
#rozhodnutí zda se v poli vyskytují dané řetězce - dle toho vracení hodnot
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return '-'
    pass

def tah_hrace(pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """
    while True:
        print('Hráč je na řadě.')
        try:
            cislo_policka = int(input('Zadej pozici, na kterou chceš umístit symbol: '))
        except ValueError:
            print('Tohle není číslo. Zadej znova.')
        else:
            while cislo_policka in range(0,DELKA_POLE):
                if pole[cislo_policka] != '-':
                    print('Zadaná pozice je již obsazena.')
                    break
                else:
                    return tah(pole, cislo_policka, SYMBOL_HRACE)
            else:
                print('Zadáváš blbosti.')

def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    pass

#doplněna funkce vypis, která vypisuje dle výsledku funkce vyhodnot
def vypis(varianta):
    """
    Vypíše výsledek v závislosti na volané funkci vyhodnot.
    """
    if varianta == 'x':
        print('Vyhrál hráč!')
    elif varianta == 'o':
        print('Vyhrál počítač!')
    elif varianta == '!':
        print('Remíza!')
    pass


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """
#založení proměnné kolo a samotného hracího pole
    kolo = 0
    pole = '-'*DELKA_POLE
#dokud se ještě může hrát (není rozhodnuto o vítězi ani remíze)
    while vyhodnot(pole) == '-':
#zvyš kolo o jedno a do pole ulož výsledek tahu hráče, vypiš informaci
        kolo += 1
        pole = tah_hrace(pole)
        print(kolo, '. kolo: ', pole, sep='')
#pokud po tahu hráčem se stále může hrát, proveď to stejné, jen pro tah hráče
        if vyhodnot(pole) == '-':
            pole = tah_pocitace(pole)
            kolo += 1
            print(kolo, '. kolo: ', pole, sep='')
            #print(pole)
#když už se nemůže hrát, vypíše dle funkce vypis, zda se jedná o výhru či remízu
    else:
        vypis(vyhodnot(pole))

    pass


if __name__ == "__main__":
    piskvorky1d()
