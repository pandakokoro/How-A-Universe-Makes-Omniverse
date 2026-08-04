import os as kiddy
import time 
chance = "yes"
while chance != "no" and chance != "exit":
    kiddy.system("cls")
    man = "MIND VERSE"
    print(f'┌{"─"*(len(man)+2)}┐\n│ {man} │\n└{"─"*(len(man)+2)}┘')
    import sys 
    while True:
        try:
            Age = int(input("From how much years universe know your exitence.... "))
            if Age > 100:
                old_man = "BLACK HOLE"
                print(f'┌{"─"*(len(old_man)+2)}┐\n│ {old_man} │\n└{"─"*(len(old_man)+2)}┘')
                sys.exit()
            break
        except ValueError:
            print("My dear Gemini\n don't try to prank me...")
    Pass = input("you think you are the omniverse...yes/no: ").strip().upper()
    while Pass not in ["YES","NO"]:
        print("Gemini Nice try\n But buy the pass bro\n don't abuse me okayy...")
        Pass = input("you think you are the omniverse...yes/no: ").strip().upper()
    gender = input("which sex you like...male/female....").strip().lower()
    while gender not in ["male", "female"]:
        ai = "AI CHATGPT"
        print(f'┌{"─"*(len(ai)+2)}┐\n│ {ai} │\n└{"─"*(len(ai)+2)}┘')
        gender = input("which sex you like...male/female....").strip().lower()
    print("Connecting to parallel Dimensions", end="", flush=True)
    for _ in range(5):
        time.sleep(0.8)
        print("◄a⌐£►",end="", flush=True)
    print("\n")
    if Age <= 0:
        print("Oye stardust take your form first")
    elif Age <18 and Pass == "YES" and gender == "female":
        print("godness it's time to create a omniverse full of joy")
    elif Age <18 and Pass == "NO" and gender == "female":
        print("godness it's time to create a disney land full of joy")
    elif Age <18 and Pass == "YES" and gender == "male":
        print("My Lord \n Order me to create and destory\n Your order my action")
    elif Age <18 and Pass == "NO" and gender == "male":
        print("bacchuu \n you are not a girl\n no pass no respect")
    elif Age >40:
        print("it's your time\n For rebirth\n happy twinkling star")
    elif Age >= 18 and Age <= 40:
        if Pass == "YES":
            if gender == "female":
                print("Real beauty\nReal cutie\nexistence itself is ready to create and destory itself...")
            elif gender == "male":
                print("Namaste\nPranama\nDoes you need my head\nMy lord\nOr I have to create/destory the existence or dimensions")
        elif Pass == "NO":
                if gender == "female":
                    print("Beauty with brain na na...\nEven with no pass I'm in your service...")
                elif gender == "male":
                    print("Ola Ola\n No pass means No money\n bye bye...")
    gemini = "OMNIVERSE."
    print(f'┌{"─"*(len(gemini)+2)}┐\n│ {gemini} │\n└{"─"*(len(gemini)+2)}┘')
    print("Connecting to parallel Dimensions", end="", flush=True)
    for _ in range(15):
        time.sleep(0.3)
        print("◄►",end="", flush=True)
    print("\n")
    chance = input("you wanna play again?... ").strip().lower()
else:
    print("Welcome Gemini hehehe...")
        
    

