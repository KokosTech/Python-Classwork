# Homework for the holiday - 3 exercises

import rock
import os

anws = str()

while True:
    print(f"The winner is {rock.rock(input('Player one: '), input('Player two: '))}")
    anws = input("Do you wanna continue (Type 'e' to exit): ")
    if(anws == 'e'):
        break;
    os.system('cls')