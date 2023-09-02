import os
import colorama
from colorama import Fore
from banner import __file__

colorama.init(autoreset=True)

__file__()

def __file__():

    while True:
            cwd = os.getcwd()
            ch = os.chdir("C:/Windows/Temp")
            try:
                print(f"{Fore.RED}\t NOTE!!! {Fore.YELLOW}Enter number Only")
                print(f"{Fore.BLUE}[+]\t{Fore.GREEN} 0.Exit")
                count = int(input(f"\n{Fore.BLUE}[+]\t{Fore.MAGENTA}Enter Number of File : {Fore.GREEN}"))
                for i in range(count):
                    open("{}.temp".format(i),"+w")
                    print(f"{Fore.GREEN}{i}.tmp")
                print(f"{Fore.GREEN}\nDone...\n")
                if count == 0:
                    print(f"{Fore.GREEN}\nExit...\n")
                    exit()
            except ValueError:
                print(f"{Fore.RED}\nError : Enter Correct Value!!!")
            except KeyboardInterrupt:
                print(f"{Fore.RED}\nExit...")
                exit()
            except EOFError:
                print(f"{Fore.RED}\nExit...")
                exit()

__file__()

