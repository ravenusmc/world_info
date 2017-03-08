#This is the main file for the project. All of functions to run the program
#will be located in this file.

#import libraries for use in this project.
import pandas as pd
import numpy as np

#Files which will be imported.
from valid import *
from support import *
from data import *

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
    data = Data()
    print("1. Gini Index")
    print("2. Female Suicide Rate")
    print("3. Male Suicide Rate")
    print("4. Homicide Rate")
    print('5. Internet Usage')
    print('6. Mean years of schooling')
    print('7. Prison Population')
    print('8. Public expenditure on Education as percentage of GDP')
    print('9. TB infections')
    choice = int(input("What is your choice? "))
    while not data_valid(choice):
        print('That is not a valid selection!')
        choice = int(input("What is your choice? "))
    if choice == 1:
        user_selection = 'Gini_coefficient'
        data.map_data(user_selection)
        main_menu()
    elif choice == 2:
        user_selection = 'Female_Suicide_Rate'
        data.map_data(user_selection)
        main_menu()
    elif choice == 3:
        user_selection = 'Male_Suicide'
        data.map_data(user_selection)
        main_menu()
    elif choice == 4:
        user_selection = 'Homicide_rate'
        data.map_data(user_selection)
        main_menu()
    elif choice == 5:
        user_selection = 'Internet_users'
        data.map_data(user_selection)
        main_menu()
    elif choice == 6:
        user_selection = 'Mean_years'
        data.map_data(user_selection)
        main_menu()
    elif choice == 7:
        user_selection = 'Prison_population'
        data.map_data(user_selection)
        main_menu()
    elif choice == 8:
        user_selection = 'Public_expenditure_on_education'
        data.map_data(user_selection)
        main_menu()
    elif choice == 9:
        user_selection = 'Tuberculosis_rate'
        data.map_data(user_selection)
        main_menu()

#This is what will launch the main program.
main()
