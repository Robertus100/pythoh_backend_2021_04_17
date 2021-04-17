from random import randint

DEBUG = True

gracz_x = randint(1, 10)
gracz_y = randint(1, 10)

skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

def odleglosc():
    return abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

def debug_polozenie():
    if DEBUG is True:
        print(f"Gracz: {gracz_x} {gracz_y}")
        print(f"Skarb: {skarb_x} {skarb_y}")
        print(f"Min l kr: {min_l_k}")

min_l_k = odleglosc()
# debug_polozenie()

liczba_krokow = 0

while True:
    min_l_k_przed = odleglosc()

    debug_polozenie()
    kierunek = input("Podaj kierunek (g,d,l,p)")

    if kierunek == 'g':
        gracz_y += 1
    elif kierunek == 'd':
        gracz_y -= 1
    elif kierunek == "p":
        gracz_x += 1
    elif kierunek == "l":
        gracz_x -= 1

    min_l_k_po = odleglosc()
    liczba_krokow += 1

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print("Wygrałeś/aś!!")
        break

    if min_l_k_przed > min_l_k_po:
        print("Ciepło")
    else:
        print("Zimno")

    if liczba_krokow > 2 * min_l_k:
        print("Zmiana położenia skarbu")
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        min_l_k = odleglosc()
        liczba_krokow = 0

print(min_l_k)

