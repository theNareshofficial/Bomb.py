import colorama
from colorama import Fore
from banner import __banner__


__banner__()

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
            attack = input(f"{Fore.BLUE}\n[+]\t{Fore.MAGENTA}Enter Your Attack : {Fore.GREEN}")

            if attack == '1':
                import cmd
            elif attack == '2':
                import note
            elif attack == '3':
                import  folder
            elif attack == '4':
                import file
            elif attack == '5':
                import explorer
            elif attack == '6':
                import chrome
            elif attack == "0":
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
