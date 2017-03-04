#The file will hold the class that will work with all of the data in this
#project.

#import libraries for use in this project.
import pandas as pd
import numpy as np

#Files which will be imported.
from valid import *
from support import *

data = pd.read_csv('Kaggle.csv')
print(data)
