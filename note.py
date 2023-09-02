import os
import colorama
from colorama import Fore
from banner import __note__

colorama.init(autoreset=True) 

__note__()

def __note__():

        while True:
                try:
                        print(f"{Fore.RED}\t NOTE!!! {Fore.YELLOW}Enter number Only")
                        print(f"{Fore.BLUE}[+]\t{Fore.GREEN} 0.Exit")
                        count = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Number of Notepad : {Fore.GREEN}"))
                        for i in range(count):
                                os.system("start notepad")
                                print(f"{Fore.GREEN}{i} Opening...") 
                        print(f"{Fore.GREEN}\nDone...\n")
                        if count == 0:
                                print(f"{Fore.GREEN}\nExit...\n")
                                exit()
                except ValueError:
                        print(f"{Fore.RED}\nError : Give Correct Value!!!")
                except KeyboardInterrupt:
                        print(f"{Fore.RED}\nExit...")
                        exit()
                except EOFError:
                        print(f"{Fore.RED}\nExit...")
                        exit()

__note__()