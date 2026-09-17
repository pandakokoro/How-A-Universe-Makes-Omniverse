import pandas as pd 
import numpy as np
import random as rd

arr = np.random.choice(100,size=(7),replace=False)+10


s = pd.Series([2, 3, 4, 54, 3, 2, 2], index= [arr])
print(s)

