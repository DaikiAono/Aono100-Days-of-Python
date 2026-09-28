import random 
from data import *
from art import logo


def password_gen(nl, ns, nn):  
    raw_password = []
    password = ""

    for item in range(1, nl + 1):
        pcode = random.choice(letters)
        raw_password.append(pcode)

    for item in range(1, ns + 1):
        pcode = random.choice(symbols)
        raw_password.append(pcode)

    for item in range(1, nn + 1):
        pcode = random.choice(numbers)
        raw_password.append(pcode)

    print(raw_password)

    for item in range(len(raw_password)):
        password += random.choice(raw_password)
       

    raw_password.clear()
    print("Your new password is: " + password)


def main():
    print(logo)
    print("Welcome to the PyPassword Generator!")

    
    no_letters = int(input("How many letters would you like" \
    " in your password?\n"))

    no_symbols = int(input("How many symbols would you like?\n"))

    no_numbers = int(input("How many numbers would you like?\n"))


    password_gen(no_letters, no_symbols, no_numbers)


main()
    
