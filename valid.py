#This folder will contain all of the validation functions in the program.

def valid_one(choice):
    if choice == 1 or choice == 2 or choice == 3:
        return True
    else:
        return False

def data_valid(choice):
    if choice < 1 or choice > 9:
        return False
    else:
        return True 
