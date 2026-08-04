import os 
msg = "LOVE METER"
play = "yes"
while play != "no" and play != "exit":
    os.system('cls')
    print(f'┌{"─"*(len(msg)+2)}┐\n│ {msg} │\n└{"─"*(len(msg)+2)}┘')
    num1 = int(input("How many crush you have: "))
    num2 = int(input("How many proposal you get: "))
    score = " KALANKI DIL "
    dil = " MY MAJESTY "
    angel = "DEAR ANGEL"
    sigma = input("which mathematical formula you want to apply on yours.... ").strip()
    Really = num1 - num2
    if sigma == "-":
        if num1 < Really:
            print("Really you think you have more proposal then your crush")
        elif num1 > Really:
            print("Salute to you \n my lord \n can you give me some tips...")
        else:
            print("impossible\n God detected")
    elif sigma == "+":
        if num1 > num2:
            print("Really you think you have more proposal then your crush")
        elif num1 < num2:
            print("Salute to you \n my lord \n can you give me some tips...")
        else:
            print("impossible\n God detected")
    elif sigma == "*":
        if num1 > num2:
            print("Really you think you have more proposal then your crush")
        elif num1 < num2:
            print("Salute to you \n my lord \n can you give me some tips...")
        else:
            print("impossible\n God detected")
    elif sigma == "/":
        if num1 < num2:
            print("Really you think you have more proposal then your crush")
        elif num1 > num2:
            print("Salute to you \n my lord \n can you give me some tips...")
        else:
            print("impossible\n God detected")
    if num1 > num2:
        print(f'┌{"─"*(len(score)+2)}┐\n│ {score} │\n└{"─"*(len(score)+2)}┘')
    elif num1 < num2:
        print(f'┌{"─"*(len(angel)+2)}┐\n│ {angel} │\n└{"─"*(len(angel)+2)}┘')
    else:
        print(f'┌{"─"*(len(dil)+2)}┐\n│ {dil} │\n└{"─"*(len(dil)+2)}┘')
    try:
        if num2 == 0:
            print("Creator has detected")
    except:
        print("everything is find bro")
    play = input('\nyou wanna play again?... ').strip().lower()
print("Dumpass\n hey lady that your potential")

