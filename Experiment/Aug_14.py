import os


class HackerHasFoundError(Exception):
    pass


try:
    chance = "yes"
    while chance != "no" :
        os.system("cls")
        panda = input("Enter the password: ").strip().lower()
        if panda == "panda7790":
            print("Now you are a wanted criminal!")
            raise HackerHasFoundError
            
        else:
            print("it's have two sevens nine zero in it \n"
                        "and a cute animal name like 'panda' in it\n"
                            " \nTry again!")
        chance = input('\nyou wanna play again?... ').strip().lower()
        
except HackerHasFoundError:
    print("okay")