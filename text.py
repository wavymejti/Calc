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
    result = x + y
    return result

def odejmowanie(x, y):
    result = x - y
    return result

#if operator == "+":
#    print(dodawanie(x, y))
#elif operator == "-":
#    print(odejmowanie(x, y))
#else:
#    print("nieznany operator")


result = dodawanie(x, y)
result = odejmowanie(x, y)


#chech if the result is even or not
if result % 2 == 0:
        print("liczba jest parzysta")
else:
        print("liczba nie jest parzysta")