#definiowanie liczb
a = float(input("podaj liczbe a\n")) #definiowanie liczby a
b = float(input("podaj liczbe b\n")) #definiowanie liczby b

#dodawanie liczb całkowitych
def dodawanie(a, b):
    wynikdodawania = a + b
    return wynikdodawania



def odejmowanie(a, b):
    wynikodejmowania = a - b
    return wynikodejmowania

def mnozenie(a, b):
    wynikmnozenia = a * b
    return wynikmnozenia

def dzielenie(a, b):

    if b != 0:
        wynikdzielenia = a / b
        return wynikdzielenia
    elif b == 0:
        return "nie dziel przez 0"

wynikdodawania = dodawanie(a, b)
print(wynikdodawania)

wynikodejmowania = odejmowanie(a, b)
print(wynikodejmowania)

wynikmnozenia = mnozenie(a, b)
print(wynikmnozenia)

wynikdzielenia = dzielenie(a, b)
print(wynikdzielenia)
