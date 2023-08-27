import os
import colorama
from colorama import Fore
from banner import __banner__

colorama.init(autoreset=True)

__banner__()

def __cmd__():

        try:
                print(f"{Fore.YELLOW}\t NOTE!!! Enter number Only")

                count = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Number of CMD : {Fore.GREEN}"))
                for i in range(count):
                        os.system("start CMD")
                        print(f"{Fore.GREEN}{i} Opening...")
                print(f"{Fore.GREEN}\nDone...\n")
                
        except ValueError:
                print(f"{Fore.RED}\nError : Give Correct Value!!!")


__cmd__()