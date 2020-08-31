import random; import os


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


if __name__ == "__main__":

    while (True):

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
