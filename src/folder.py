import os
import colorama
from colorama import Fore
from src.banner import _folder_

colorama.init(autoreset=True)

_folder_()

def __folder__():

    while True:
        try:
            cwd = os.getcwd()
            cd = os.chdir("C:\Windows\Temp")
            print(f"{Fore.RED}\t NOTE!!! {Fore.YELLOW}Enter number Only")
            print(f"{Fore.BLUE}[+]\t{Fore.GREEN} 0.Exit")
            count = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Number of Folder : {Fore.GREEN}"))
            for i in range(count):
                os.mkdir("{}.temp".format(i))
                print(f"{Fore.GREEN}{i}.temp")
            print(f"{Fore.GREEN}\nDone...\n")
            if count == 0:
                print(f"{Fore.GREEN}\nExit...\n")
                exit()
        except FileExistsError:
            print(Fore.BLUE + "\n[+]\t", Fore.RED + "oops!!! This File is Already Exits, Restart Once\n")
        except ValueError:
            print(f"{Fore.RED}\nError : Give Correct Value!!!")
        except KeyboardInterrupt:
            print(f"{Fore.RED}\nExit...")
            exit()
        except EOFError:
            print(f"{Fore.RED}\nExit...")
            exit()

# __folder__()