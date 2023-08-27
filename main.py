import colorama
from colorama import Fore, Back
from banner import __banner__

__banner__()

colorama.init(autoreset=True)

def __main__():
    print(f"""
 {Fore.BLUE}[+]\t{Fore.GREEN}1.CMD Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}2.Notepad Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}3.Folder Attack
 {Fore.BLUE}[+]\t{Fore.GREEN}4.File Attack
    """)

    print(f"{Fore.YELLOW}\t NOTE!!! Enter number Only")

    try:
        attack = (int(input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Your Attack : {Fore.GREEN}")))

        if attack == 1:
            import cmd
     
        elif attack == 2:
            import note

        elif attack == 3:
           import  folder

        elif attack == 4:
            import file

        else:
            print(f"{Fore.BLUE}[+]{Fore.RED}Enter Correct Value!!!")
    
    except ValueError:
        print(f"{Fore.RED}\nError : Give Correct Value!!!")
    
__main__()
