#Dodawanie
def add (a,b):
    return(a + b)
#Odejmowanie
def subtract (a,b):
    return(a - b)
#Mnożenie
def multiply(a,b):
    return(a * b)
#Dzielenie
def divide(a,b):
    return(a / b)

#Zwrot do użytkownika
print("Wybierz operację:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
#Wybór użytkownika
choice = input("Wybierz opcję (1,2,3,4)  ")
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Podaj pierwszą wartość: "))
    num2 = float(input("Podaj drugą wartość: "))

    if choice == '1':
        print("Dodaję", num1, "i", num2)
        print("Wynik to: ", add(num1,num2))

    elif choice== '2':
        print("Odejmuję", num1, "od", num2)
        print("Wynik to: ", subtract(num1,num2))

    elif choice == '3':
        print("Mnożę", num1, "przez", num2)
        print("Wynik to: ", multiply(num1,num2))

    elif choice == '4':
        print("Dzielę", num1, "przez", num2)
        print("Wynik to: ", divide(num1,num2))
#Jeśli nie wybierze liczb 1-4
else:
    print("Zły wybór")