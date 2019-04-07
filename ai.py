from random import randrange
import piskvorky
#from piskvorky import DELKA_POLE, symbol
DELKA_POLE = 20

SYMBOL_HRACE = "x"
SYMBOL_POCITACE = "o"

def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    #print('Počítač je na řadě:')
    while True:
        cislo_policka = randrange(0,DELKA_POLE)
        if pole[cislo_policka] == '-':
            return piskvorky.tah(pole, cislo_policka, SYMBOL_POCITACE)
