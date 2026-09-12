import numpy as np 
import random as rd

arr = np.arange(25).reshape(5,5)

def sovereign_name(arr):
    mission = """

MAKE THIS EARTH TO BECOME THE CIVILIZATION II, 
    DYSON SPHERE,
        THE ULTIMATE WEAPON,
            HYDRO-NUCLEAR BOMB,
                ONE OMNIVERSE = ONE PLANET = INDIA



               """
    name = input("Enter your name: ").strip().lower()
    print(name)
    great = ["panda","kirti","lisa","roses","jennie","jisoo"]
    name_words = name.split()
    if any(word in great for word in name_words):
        print(f"Sovereign pass for {name_words},\n"
                 f"The sovereign Members are {great},\n"
                    f"We are on a Mission,\n"
                        f"The Mission,\n"
                            f"{mission}")
    else:
        pass
    
if __name__ == "__main__" :
    sovereign_name(arr)
