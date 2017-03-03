#This file will contain the support class.

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
        ''')
        input('Press enter to return to main menu ')

    def quit(self):
        print('\033c')
        print('\t************************************************')
        print('\tProgram is now quitting, thank you for using it!')
        print('\tHope you come back real soon!!!')
        print('\t************************************************')
        print()
        input('\tPress enter to quit ')
