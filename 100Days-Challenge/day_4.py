import numpy as np 
import random as rd 
arr = np.random.choice(100,size=(9,9),replace=False)+20
for a in zip(arr):
    print(f"\n{a}")