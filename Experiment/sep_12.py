import numpy as np
import random as rd

index = np.arange(25).reshape(5,5)

arr = np.random.randint(1,100,size=(5,5))

choice = rd.choice(["red","eye"])

"""

this code is all about;
random and numpy libraries;




"""

print(f"\nThe index of the Array \n {index}\n")
print(f"\nOriginal Array \n{arr}\n")
if choice == "red":
    print(f"\nAfter adding two to it \n {arr+2}\n")

else:
    print(f"\nAfter subtracting two from it \n {arr-2}\n")
