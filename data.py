#The file will hold the class that will work with all of the data in this
#project.

#import libraries for use in this project.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pycountry
from pygal.maps.world import World
from pygal.style import RotateStyle

#Files which will be imported.
from valid import *
from support import *

#This class will work with the data in this file. I admit that this is a fairly
#long way to deal with this data-I have one super long method that has another
#function essentially within it! Not what I like.
class Data():

    #This method is what will process the data and make the SVG map from it. The
    #country_name_convert function I do not like at all having it within this
    #method. However, I want to finish this project and just have it there
    #for the time being.
    def map_data(self, user_selection):
        ### This function will be used to convert the country names to their two letter code.
        def country_name_convert(country_list):
            countries = {}
            for country in pycountry.countries:
                countries[country.name] = country.alpha2
            country_codes = [countries.get(country, 'Unknown code') for country in country_list]
            return country_codes
        data = pd.read_csv('Kaggle.csv')
        #These two lists will hold all of my data for what the user wants to
        #look at.
        data_list = []
        state_list = []
        info = data[user_selection]
        state = data['State']
        #I am now looping through the data and then appending that information
        #into the list that I created above.
        for i in info:
            data_list.append(i)
        for s in state:
            state_list.append(s)
        #Function to convert country names to 2 letter abbreviations. See country_name_convert function at the top
        #to see how it works-the only piece of code that I got all from stack overflow.
        country_codes = country_name_convert(state_list)
        #Another list is created to hold all of the country abbreviations which have been converted to lowercase.
        new_countrylist = []
        #I have to convert all of the country codes to lowercase-only way the wm.add method seems to work.
        for country in country_codes:
            lowercase_country = country.lower()
            new_countrylist.append(lowercase_country)
        #The wm.add method needs a dictionary to work with. Here, I create a dictionary which holds the country abbrevation
        #and the data for what the user wants to look at.
        country_dictionary = {}
        count = 0
        while count < len(country_codes):
            country_dictionary[new_countrylist[count]] = data_list[count]
            count += 1
        data_1, data_2, data_3, data_4, data_5 = {},{},{},{},{}
        #I need to break up the data points into five different intervals.
        #To do this I need to find the max and min of the data_list
        max_value = max(data_list)
        min_value = min(data_list)
        #Once I have the max and min I can find the length
        length = max_value - min_value
        #I then divide the length by 5 for the number of dictionaries that I
        #have created above: data_1, data_2 etc.
        parts = length / 5
        #I use a for loop to place the data into the right intervals
        for state, information in country_dictionary.items():
            if information <= parts:
                data_1[state] = information
            elif information > parts and information <= parts * 2:
                data_2[state] = information
            elif information > parts * 2 and information <= parts * 3:
                data_3[state] = information
            elif information > parts * 3 and information <= parts * 4:
                data_4[state] = information
            else:
                data_5[state] = information
        print('''
        Please note to look at the data, you have to open up the SVG map in
        Chrome. The file should be entitled map.svg. The program will return to
        the main menu so you must open up the file manually. 
        ''')
        input('Press enter to continue ')
        #This code here is what will actually make the SVG maps for the data that
        #the user wants to look at.
        wm_style = RotateStyle('#336699')
        wm = World(style=wm_style)
        wm.title = "Map of " + user_selection + ' Data'
        wm.add(str(0) + '-' + str(parts), data_1)
        wm.add(str(parts) + '-' + str(parts * 2), data_2)
        wm.add(str(parts * 2) + '-' + str(parts * 3), data_3)
        wm.add(str(parts * 3) + '-' + str(parts * 4), data_4)
        wm.add(str(parts * 4) + '-' + str(parts * 5), data_5)
        wm.render_to_file('map.svg')
