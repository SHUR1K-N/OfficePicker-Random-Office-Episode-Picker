import random; import os

os.system("@echo off")
loopFlag = 0

while (loopFlag == 0):

    os.system("cls")

    randmS = random.randint(1, 9)
    if (randmS == 1):
        randmE = random.randint(1, 6)
    elif (randmS) == 2:
        randmE = random.randint(1, 22)
    elif (randmS) == 3:
        randmE = random.randint(1, 25)
    elif (randmS) == 4:
        randmE = random.randint(1, 19)
    elif (randmS) == 5:
        randmE = random.randint(1, 28)
    elif (randmS) == 6:
        randmE = random.randint(1, 26)
    elif (randmS) == 7 or 9:
        randmE = random.randint(1, 27)
    elif (randmS) == 8:
        randmE = random.randint(1, 24)

    print("Season %d, Episode %d\n" % (randmS, randmE))
    cont = input(str("Press Enter to reroll.\n"))

    if cont == "":
        loopFlag = 0
    else:
        loopFlag = 1
