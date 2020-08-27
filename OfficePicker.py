import random; import os

if __name__ == "__main__":

    reRoll = True

    os.system("@echo off")

    while (reRoll is True):

        os.system("cls")

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
