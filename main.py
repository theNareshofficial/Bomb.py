import colorama
from colorama import Fore
from src.banner import _banner_ 
from src.chrome import chrome
from src.cms import __cmd__
from src.explorer import __explorer__
from src.note import __note__
from src.file import __file__
from src.folder import __folder__

_banner_()

colorama.init(autoreset=True)

def __main__():
    print(f"""
 {Fore.BLUE}[+]\t{Fore.GREEN}1.CMD Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}2.Notepad Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}3.Folder Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}4.File Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}5.Explorer Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}6.Chrome Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}0.Exit

    """)
    print(f"{Fore.RED}\t NOTE!!! {Fore.YELLOW}Enter number Only")

    while True:
        try:
            attack = int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Your Attack : {Fore.GREEN}"))

            if attack == 1:
                __cmd__()
            elif attack == 2:
                __note__()
            elif attack == 3:
                __folder__()
            elif attack == 4:
                __file__()
            elif attack == 5:
                __explorer__()
            elif attack == 7:
                chrome()
            elif attack == 0:
                print(f"{Fore.GREEN}Exit...\n")
                exit()
            else:
                print(f"{Fore.RED}\nError : Enter Correct Value!!!")
        except ValueError:
            print(f"{Fore.RED}\nError : Enter Correct Value!!!")
        except KeyboardInterrupt:
            print(f"{Fore.GREEN}\n\nExit...\n")
            exit()
        except EOFError:
            print(f"{Fore.GREEN}\nExit...\n")
            exit()
    
__main__()
