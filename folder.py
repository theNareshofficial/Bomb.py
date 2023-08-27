import os
import colorama
from colorama import Fore
from banner import __banner__

colorama.init(autoreset=True)

__banner__()

def __folder__():

    cwd = os.getcwd()
    cd = os.chdir("C:\Windows\Temp")

    try:
        print(f"{Fore.YELLOW}\t NOTE!!! Enter number Only")
        count = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Number of Folder : {Fore.GREEN}"))
        for i in range(count):
            os.mkdir("{}.temp".format(i))
            print(f"{Fore.GREEN}{i}.temp")

    except FileExistsError:
        print(Fore.BLUE + "\n[+]\t", Fore.RED + "oops!!! This File is already exits, Resart Once\n")
    
    except ValueError:
        print(f"{Fore.RED}\nError : Give Correct Value!!!")


__folder__()