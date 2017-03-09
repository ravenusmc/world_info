#This file will contain the support class.

#Importing files that this class will need to run.
import pycountry

#The main purpose of this class is to have methods that I can call that will
#provide support to the running of the main program.
class Support():

    #This method will simply provide the user with information if they choose to
    #learn about this program.
    def help(self):
        print('\033c')
        print('''
        This program is meant to provide the user with a graphical
        representation of world data based on what the user selects. Thus, if
        the user wants to look at a states GDP they will see a world map that
        is color coded based on what they see. This is really not a complex
        program but provides more practice on showing data on a world map.
        Finally, I will say that the most interesting map was from the prison
        population data set....
        ''')
        input('Press enter to return to main menu ')

    #This method will provide the user with options to quit out of the program.
    def quit(self):
        print('\033c')
        print('\t************************************************')
        print('\tProgram is now quitting, thank you for using it!')
        print('\tHope you come back real soon!!!')
        print('\t************************************************')
        print()
        input('\tPress enter to quit ')

    ### This method will be used to convert the country names to their two letter code.
    def country_name_convert(self,country_list):
        countries = {}
        for country in pycountry.countries:
            countries[country.name] = country.alpha2
        country_codes = [countries.get(country, 'Unknown code') for country in country_list]
        return country_codes
