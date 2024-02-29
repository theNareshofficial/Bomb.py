import os
import colorama
from colorama import Fore
from src.banner import _explorer_

colorama.init(autoreset=True)

_explorer_()

def __explorer__():

     while True:
          try:
               print(f"{Fore.RED}\t NOTE!!! {Fore.YELLOW}Enter number Only")
               print(f"{Fore.BLUE}[+]\t{Fore.GREEN} 0.Exit")
               count = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Number of Explorer : {Fore.GREEN}"))
               for i in range(count):
                    os.system("start explorer")
                    print(f"{Fore.GREEN}{i} Opening...")
               print(f"{Fore.GREEN}\nDone...")
               if count == 0:
                    print(f"{Fore.GREEN}\nExit...\n")
                    exit()
          except ValueError:
               print(f"{Fore.RED}\nError : Give Correct Value!!!")
          except KeyboardInterrupt:
               print(f"{Fore.GREEN}\n\nExit...\n")
               exit()
          except EOFError:
               print(f"{Fore.GREEN}\nExit...\n")
               exit()

# explorer()