import os
import colorama
from colorama import Fore
from banner import __banner__

colorama.init(autoreset=True)

__banner__()

def __file__():

    cwd = os.getcwd()
    ch = os.chdir("C:/Windows/Temp")

    try:
        print(f"{Fore.YELLOW}\t NOTE!!! Enter number Only")
        count = int(input(f"\n{Fore.BLUE}[+]\t{Fore.MAGENTA}Enter number of File : {Fore.GREEN}"))
        for i in range(count):
            open("{}.temp".format(i),"+w")
            print(f"{Fore.GREEN}{i}.tmp")

        print(f"{Fore.GREEN}\nDone...\n")
    except:
        print(f"{Fore.RED}\nError : Give Correct Value!!!")

__file__()

