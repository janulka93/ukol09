import pytest
import ai, piskvorky


def test_vyhodnot_vyhra_x():
    """
    Křížky vyhrály.
    """
    assert piskvorky.vyhodnot("xxx-----------------") == "x"
    assert piskvorky.vyhodnot("--------xxx---------") == "x"
    assert piskvorky.vyhodnot("-----------------xxx") == "x"
    assert piskvorky.vyhodnot("-xoxoxxxoxoxoxoxoxox") == "x"
    assert piskvorky.vyhodnot("-xooxxooxxooxxoxxxoo") == "x"
    assert piskvorky.vyhodnot("xxxoxoxoxoxoxoxoxox-") == "x"
    assert piskvorky.vyhodnot("oxxxoxoxxooxxooxxoo-") == "x"
    assert piskvorky.vyhodnot("oxoxoxoxo-oxoxoxoxxx") == "x"
    assert piskvorky.vyhodnot("xxooxxoox-ooxxooxxxo") == "x"
    assert piskvorky.vyhodnot("o-oxoxxoxxxoxxooxxoo") == "x"
    assert piskvorky.vyhodnot("ooxoxxoox-xoxxxoxxoo") == "x"


def test_vyhodnot_vyhra_o():
    """
    Kolečka vyhrála.
    """
    assert piskvorky.vyhodnot("ooo-----------------") == "o"
    assert piskvorky.vyhodnot("--------ooo---------") == "o"
    assert piskvorky.vyhodnot("-----------------ooo") == "o"
    assert piskvorky.vyhodnot("-xoxoxoxoooxoxoxoxox") == "o"
    assert piskvorky.vyhodnot("-xoooxooxxooxxooxxoo") == "o"
    assert piskvorky.vyhodnot("xoooxoxoxoxoxoxoxox-") == "o"
    assert piskvorky.vyhodnot("oooxxooxxooxxooxxoo-") == "o"
    assert piskvorky.vyhodnot("oxoxoxoxo-oxoxoxooox") == "o"
    assert piskvorky.vyhodnot("xxooxxoox-ooxxooxooo") == "o"
    assert piskvorky.vyhodnot("x-xoxooxoooxooxxooxx") == "o"
    assert piskvorky.vyhodnot("xxoxooxxo-oxoooxooxx") == "o"


def test_vyhodnot_remiza():
    """
    Nastala remíza.
    """
    assert piskvorky.vyhodnot("oxoxoxoxoxoxoxoxoxox") == "!"
    assert piskvorky.vyhodnot("xxooxxooxxooxxooxxoo") == "!"
    assert piskvorky.vyhodnot("xoxoxoxoxoxoxoxoxoxo") == "!"
    assert piskvorky.vyhodnot("ooxxooxxooxxooxxooxx") == "!"


def test_vyhodnot_hra():
    """
    Hra neskončila.
    """
    assert piskvorky.vyhodnot("--------------------") == "-"
    assert piskvorky.vyhodnot("xx----------------oo") == "-"
    assert piskvorky.vyhodnot("-xoxoxoxoxoxoxoxoxox") == "-"
    assert piskvorky.vyhodnot("-xooxxooxxooxxooxxoo") == "-"
    assert piskvorky.vyhodnot("xoxoxoxoxoxoxoxoxox-") == "-"
    assert piskvorky.vyhodnot("xooxxooxxooxxooxxoo-") == "-"
    assert piskvorky.vyhodnot("oxoxoxoxo-oxoxoxoxox") == "-"
    assert piskvorky.vyhodnot("xxooxxoox-ooxxooxxoo") == "-"
    assert piskvorky.vyhodnot("xxoo------------xxoo") == "-"
    assert piskvorky.vyhodnot("oo----------------xx") == "-"


def test_tah_x():
    """
    Pozitivní testy se symbolem "x".
    """
    assert piskvorky.tah("--------------------", 0, "x") == "x-------------------"
    assert piskvorky.tah("--------------------", 5, "x") == "-----x--------------"
    assert piskvorky.tah("--------------------", 10, "x") == "----------x---------"
    assert piskvorky.tah("--------------------", 15, "x") == "---------------x----"
    assert piskvorky.tah("--------------------", 19, "x") == "-------------------x"


def test_tah_o():
    """
    Pozitivní testy se symbolem "o".
    """
    assert piskvorky.tah("--------------------", 0, "o") == "o-------------------"
    assert piskvorky.tah("--------------------", 5, "o") == "-----o--------------"
    assert piskvorky.tah("--------------------", 10, "o") == "----------o---------"
    assert piskvorky.tah("--------------------", 15, "o") == "---------------o----"
    assert piskvorky.tah("--------------------", 19, "o") == "-------------------o"


def test_tah_pocitace_prazdne():
    """
    Hra na prázdné pole.
    """
    pole = "--------------------"
    result = ai.tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("-") == 19
    assert result.count("o") == 1


def test_tah_pocitace_skoro_plne():
    """
    Hra na skoro plné pole (volno uprostřed).
    """
    pole = "xoxoxoxoxo-xoxoxoxox"
    result = ai.tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_zacatek():
    """
    Hra na skoro plné pole (volno na začátku).
    """
    pole = "-xoxoxoxoxoxoxoxoxox"
    result = ai.tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec():
    """
    Hra na skoro plné pole (volno na konci).
    """
    pole = "xoxoxoxoxoxoxoxoxox-"
    result = ai.tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec_2():
    """
    Hra na skoro plné pole (2× volno na konci).
    """
    pole = "xooxxooxoxoxoxooxx--"
    result = ai.tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 9
    assert result.count("o") == 10
    assert result.count("-") == 1


def test_tah_pocitace_delka_pole_25_prazdne():
    """
    Hra na prázdné pole s délkou 25.
    """
    pole = "-------------------------"
    result = ai.tah_pocitace(pole)
    assert len(result) == 25
    assert result.count("-") == 24
    assert result.count("o") == 1

#
# def test_tah_pocitace_plne_pole():
#     """
#     Hra na plné pole.
#     """
#     pole = 'xoxoxoxoxoxoxoxoxoxo'
#     with pytest.raises(ValueError):
#         ai.tah_pocitace(pole)

# def test_tah_pocitace_delka_pole_0():
#     """
#     Hra na pole s délkou 0.
#     """
#     pole = ''
#     result = ai.tah_pocitace(pole)
#     assert len(result) == 0
#     with pytest.raises(ValueError):
#         ai.tah_pocitace(pole)

if __name__ == "__main__":
    pytest.main()
