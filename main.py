#This is the main file for the project. All of functions to run the program
#will be located in this file.

#Files which will be imported.
from valid import *

#This is the main function of the program which will launch it once the program
#is executed.
def main():
    print('\033c')
    print('\t---------------------')
    print('\tWelcome to World Info')
    print('\t---------------------')
    print()
    input('\tHit Enter to continue! ')
    main_menu()

#This function will present the user with the main menu.
def main_menu():
    print('\033c')
    print('1. Use Program')
    print('2. Learn about this program')
    print('3. Quit')
    choice = int(input('What is your choice? '))
    while not valid_one(choice):
        print('That is not a valid choice!')
        choice = int(input('What is your choice? '))
    if choice == 1:
        pass

main()
