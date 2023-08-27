import os
import colorama
from colorama import Fore
from banner import __banner__

colorama.init(autoreset=True) 

__banner__()

def __note__():

        print(f"{Fore.YELLOW}\t NOTE!!! Enter number Only")
        try:
                count = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Number of Notepad : {Fore.GREEN}"))

                for i in range(count):
                        os.system("start notepad")
                        print(f"{Fore.GREEN}{i} Openning..") 
                print(f"{Fore.GREEN}\nDone...\n")
        except:
                print(f"{Fore.RED}\nError : Give Correct Value!!!")

__note__()