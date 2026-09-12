import random as message

msg = message.choice(["dare","truth"])

def sovereign_msg(msg):
    pycom = input(f'what you can give this universe, \n write your ultimate message: {msg =} : ')
    print(pycom)
    soverignty = ["save","help","we","india","heart","peace"]
    if "indian" in pycom:
        if any(word in pycom for word in soverignty):
            print("soverignty has been called")
        else:
            pass
    else:
        return

if __name__ == "__main__" :
    sovereign_msg(msg)

        
