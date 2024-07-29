#definiowanie liczb
a = float(input("podaj liczbe a\n")) #definiowanie liczby a
b = float(input("podaj liczbe b\n")) #definiowanie liczby b

#dodawanie liczb całkowitych
def dodawanie(a, b):
    wynikdodawania = a + b
    return wynikdodawania

#dodawaniecal = int(a + b) #operacja arytmetyczna na liczbach całkowitych
#print(dodawaniecal)
#
##dodawanie liczb rzeczywistych
#dodawaniezmien = float(a+b)
#print(dodawaniezmien)

def odejmowanie(a, b):
    wynikodejmowania = a - b
    return wynikodejmowania
##odejmowanie liczb całkowitch
#odejmowaniecal = int(a - b)
#print(odejmowaniecal)
#
##odejmowanie liczb rzeczywistch 
#odejmowanierzeczywistych = float(a - b)
#print(odejmowanierzeczywistych)

def mnozenie(a, b):
    wynikmnozenia = a * b
    return wynikmnozenia
##mnozenie liczb naturalnych
#mnozenienat = int(a * b)
#print(mnozenienat)
#
##mnozenie liczb rzeczywistych 
#mnozenierzeczywistych = float(a * b)
#print(mnozenierzeczywistych)

def dzielenie(a, b):
    wynikdzielenia = a / b
    return wynikdzielenia
##dzielenie naturlanych
#dzielenienat = int(a / b)
#print(dzielenienat)
#
##dzielenie rzeczywistch
#dzielenierzeczywistych = float(a / b)
#print(dzielenierzeczywistych)

wynikdodawania = dodawanie(a, b)
print(wynikdodawania)

wynikodejmowania = odejmowanie(a, b)
print(wynikodejmowania)

wynikmnozenia = mnozenie(a, b)
print(wynikmnozenia)

wynikdzielenia = dzielenie(a, b)
print(wynikdzielenia)
