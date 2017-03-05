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

# data = pd.read_csv('Kaggle.csv')
# print(data)

class Data():

    ### This function will be used to convert the country names to their two letter code.


    def map_data(self):
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
        info = data['Gini_coefficient']
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
        data_1, data_2, data_3 = {},{},{}
        for state, information in country_dictionary.items():
            if information <= 33:
                data_1[state] = information
            elif information > 33 and information <= 66:
                data_2[state] = information
            else:
                data_3[state] = information

        wm_style = RotateStyle('#336699')
        wm = World(style=wm_style)
        wm.title = "Data "
        wm.add('0-33', data_1)
        wm.add('34-66', data_2)
        wm.add('67-100', data_3)
        wm.render_to_file('map.svg')
        svg_map_help()






data = Data()
data.map_data()
