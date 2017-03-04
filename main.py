#This is the main file for the project. All of functions to run the program
#will be located in this file.

#import libraries for use in this project.
import pandas as pd
import numpy as np

#Files which will be imported.
from valid import *
from support import *

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
    support = Support()
    choice = int(input('What is your choice? '))
    while not valid_one(choice):
        print('That is not a valid choice!')
        choice = int(input('What is your choice? '))
    if choice == 1:
        data_options()
    elif choice == 2:
        support.help()
        main_menu()
    elif choice == 3:
        support.quit()

#This function will allow the user to select what data they want to look at
def data_options():
    print('\033c')
    print("1. Look at Gini index")
    choice = int(input("What is your choice? "))


main()
