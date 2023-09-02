import os
import colorama
from colorama import Fore
from banner import __chrome__

colorama.init(autoreset=True)

__chrome__()

def chrome():

     while True:
          try:
               print(f"{Fore.RED}\t NOTE!!! {Fore.YELLOW}Enter number Only")
               print(f"{Fore.BLUE}[+]\t{Fore.GREEN} 0.Exit")
               count = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Number of Chrome : {Fore.GREEN}"))
               for i in range(count):
                    os.system("start chrome")
                    print(f"{Fore.GREEN}{i} Opening...")
               print(f"{Fore.GREEN}\nDone...")
               if count == 0:
                    print(f"{Fore.GREEN}\nExit...\n")
                    exit()
          except FileNotFoundError:
               print(f"{Fore.RED}\nError : Chrome is Not Available in your system!!1")
          except ValueError:
               print(f"{Fore.RED}\nError : Give Correct Value!!!")
          except KeyboardInterrupt:
               print(f"{Fore.GREEN}\n\nExit...\n")
               exit()
          except EOFError:
               print(f"{Fore.GREEN}\nExit...\n")
               exit()

chrome()