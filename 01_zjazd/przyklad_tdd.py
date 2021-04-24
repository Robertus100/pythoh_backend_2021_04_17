def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    return False

def test_czy_parzysta_dla_l_parzystej():
    assert czy_parzysta(2) is True

def test_czy_parzysta_dla_l_nieparzystej():
    assert czy_parzysta(3) is False
