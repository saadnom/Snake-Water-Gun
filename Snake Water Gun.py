import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {'s':1,'g':0,'w':-1}
reverseDict = {1:"Snake",0:'Gun',-1:'Water'}

you = youDict[youstr]

print(f'You choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}')

if you == computer:
    print("It's draw")
else:
    if you == -1 and computer == 1:
        print("You Win!")
    elif you == 1 and computer ==-1:
        print("You Win!")
    elif you == 0 and computer == 1:
        print("You lost!")
    elif you == 0 and computer == -1:
        print("You Win!")
    elif you == -1 and computer == 0:
        print("You lost!")
    elif you == 1 and computer == 0:
        print("You Win!")
    else:
        print("Something Wrong")
