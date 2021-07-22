import sys
import logging
logging.basicConfig(level=logging.DEBUG)


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
logging.info("Wybierz operację:")
logging.info("1.Dodawanie")
logging.info("2.Odejmowanie")
logging.info("3.Mnożenie")
logging.info("4.Dzielenie")
#Wybór użytkownika
choice = input("Wybierz opcję (1,2,3,4)  ")
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Podaj pierwszą wartość: "))
    num2 = float(input("Podaj drugą wartość: "))


    if choice == '1':
        logging.info(f"Dodaję {num1} i {num2}")
        logging.info(f"Wynik to:  {add(num1,num2)}")

    elif choice== '2':
        logging.info(f"Odejmuję {num1} od {num2}")
        logging.info(f"Wynik to:  {subtract(num1,num2)}")

    elif choice == '3':
        logging.info(f"Mnożę {num1} przez {num2}")
        logging.info(f"Wynik to:  {multiply(num1,num2)}")

    elif choice == '4':
        logging.info(f"Dzielę {num1} przez {num2}")
        logging.info(f"Wynik to:  {divide(num1,num2)}")
#Jeśli nie wybierze liczb 1-4
else:
    logging.debug("Zły wybór")



    