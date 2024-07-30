user = input("wpisz działanie:\n")
print("wpisałeś: ")
print(user)

#string splitting
spliter = user.split()
print(spliter)

#getting variables
x = int(spliter[0])
y = int(spliter[2])
operator = spliter[1]

def dodawanie(x, y):
    wynikdodawania = x + y
    return wynikdodawania

def odejmowanie(x, y):
    wynikodejmowania = x - y
    return wynikodejmowania

if operator == "+":
    print(dodawanie(x, y))
elif operator == "-":
    print(odejmowanie(x, y))
else:
    print("nieznany operator")
