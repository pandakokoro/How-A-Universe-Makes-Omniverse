import numpy as np
import random as rd

arr = np.random.randint(1,55,size=(5,5))

def marriage_matrix(arr):
    print(f'\n┌{"─"*(len("MARRIAGE MATRIX")+2)}┐\n│ {"MARRIAGE MATRIX"} │\n└{"─"*(len("MARRIAGE MATRIX")+2)}┘\n')
    gender = rd.choice(["boy","girl"])
    boy = int(rd.choice(arr.flatten()))
    girl = int(rd.choice(arr.flatten()))
    if gender == "boy":
        if boy >= 21 :
            if boy <= 30 :
                print(f"Man ,\n age = {boy}, \n"
                        f"If you have talent and money together,\n"
                            f"At this point you are unbeatable,\n"
                                f"It's the Time to chase Your Empress,\n"
                                    f"you are qualified\n")
            elif boy <= 40 :
                print(f"Man ,\n age = {boy}, \n"
                        f"It's god era,\n"
                            f"For your family,\n"
                                f"Because a tycoon acting as a boy,\n"
                                    f"It's the Time to chase Your Empress,\n"
                                        f"you are qualified\n")
            else:
                print(f"Man ,\n age = {boy},\n "
                        f"Only cheat code;\n"
                            f"You have left,\n"
                                f"MONEY,\n"
                                    f"you are unqualified\n")
    else:
        if girl >= 18 :
            if girl <= 21 :
                print(f"lady ,\n age = {girl}\n"
                        f"beauty at her prime.\n"
                            f"you are qualified\n")
            elif girl <= 30 :
                print(f"lady ,\n age = {girl},\n"
                        f"When the prime of beauty,\n"
                            f"Meets the prime itself,\n"
                                f"you are qualified\n")
            else:
                print(f"lady ,\n age = {girl},\n"
                        f"Only cheat code;\n"
                            f"You have left,\n"
                                f"MONEY,\n"
                                    f"you are unqualified\n")

if __name__ == "__main__" :
    marriage_matrix(arr)
    
