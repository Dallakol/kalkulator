#Dodawanie
def add (a,b,):
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
        print(num1, '+', num2, '=', add(num1, num2))

    elif choice== '2':
        print(num1, '-', num2, '=', subtract(num1,num2))

    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1,num2))

    elif choice == '4':
        print(num1, '/' , num2, '=', divide(num1,num2))
#Jeśli nie wybierze liczb 1-4
else:
    print("Zły wybór")
    
