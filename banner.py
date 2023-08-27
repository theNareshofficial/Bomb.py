import os
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def __banner__():
    
    os.system('cls' or 'clear')
    
    print(f"""{Fore.GREEN}
\t _______                           __                               
\t/       \                         /  |                              
\t$$$$$$$  |  ______   _____  ____  $$ |____        ______   __    __ 
\t$$ |__$$ | /      \ /     \/    \ $$      \      /      \ /  |  /  |
\t$$    $$< /$$$$$$  |$$$$$$ $$$$  |$$$$$$$  |    /$$$$$$  |$$ |  $$ |
\t$$$$$$$  |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |    $$ |  $$ |$$ |  $$ |
\t$$ |__$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ | __ $$ |__$$ |$$ \__$$ |
\t$$    $$/ $$    $$/ $$ | $$ | $$ |$$    $$/ /  |$$    $$/ $$    $$ |
\t$$$$$$$/   $$$$$$/  $$/  $$/  $$/ $$$$$$$/  $$/ $$$$$$$/   $$$$$$$ |
\t                                                $$ |      /  \__$$ |
\t                                                $$ |      $$    $$/ 
\t                                                $$/        $$$$$$/  
\t {Fore.BLUE}[+]{Fore.GREEN}Instagram : {Fore.RED}thenareshoffcial  
\t {Fore.BLUE}[+]{Fore.GREEN}GitHub    : {Fore.RED}thenareshofficial  

--------------------------------------------------------------------------------------------------------------
""")
    
__banner__()