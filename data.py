#The file will hold the class that will work with all of the data in this
#project.

#import libraries for use in this project.
import pandas as pd
import numpy as np

#Files which will be imported.
from valid import *
from support import *

# data = pd.read_csv('Kaggle.csv')
# print(data)

class Data():

    def map_data(self):
        data = pd.read_csv('Kaggle.csv')
        #print(data)
        country_list = []
        # data = data['Gini_coefficient']
        state = data['State'][0]
        print(data)

data = Data()
data.map_data()
