panda = input("Enter the password: ").strip().lower()


class HackerHasFoundError(Exception):
    pass


try:
    if panda == "panda7790":
        print("Now you are a wanted criminal!")
        raise HackerHasFoundError
    else:
        print("it's have two sevens nine zero in it \nTry again!")
        
except HackerHasFoundError:
    print("okay")