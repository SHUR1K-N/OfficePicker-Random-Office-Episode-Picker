import random; import os


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


if __name__ == "__main__":

    while (True):

        try:

            clrscr()

            randSeason = random.randint(1, 9)
            if (randSeason == 1):
                randEpisode = random.randint(1, 6)
            elif (randSeason) == 2:
                randEpisode = random.randint(1, 22)
            elif (randSeason) == 3:
                randEpisode = random.randint(1, 25)
            elif (randSeason) == 4:
                randEpisode = random.randint(1, 19)
            elif (randSeason) == 5:
                randEpisode = random.randint(1, 28)
            elif (randSeason) == 6:
                randEpisode = random.randint(1, 26)
            elif (randSeason) == 7 or 9:
                randEpisode = random.randint(1, 27)
            elif (randSeason) == 8:
                randEpisode = random.randint(1, 24)

            print(f"Season {randSeason}, Episode {randEpisode}\n")
            input("Press Enter to reroll.\n")
        except KeyboardInterrupt:
            clrscr()
            print("\nCTRL ^C\n\nWhy are you the way that you are?")
            print("Honestly, every time I try to do something fun or exciting, you make it... NOT that way.")
            print("I hate so much about the things that you choose to be.")
            print("\nPress Enter to exit.")
            input()
