# rawrcat v1.0
# 'iomgr.py' -> command line iostream manager -> v1.1
# shell text formatting and iostream handling
# python version 3.13.5
# dependencies: 'colorama' 'os' 'platform'
# [!] undefined exception handling rules

# import dependencies
import os, platform
from colorama import init, Fore, Style
init(autoreset=True)

# object 'textcolor' { (takes no parameters) -> null }
class textcolor:

    # method 'format' - format string text color
    def format(color, ctext):
        if color == 0:
            return (Style.RESET_ALL + str(ctext,))
        elif color == 1:
            return (Style.NORMAL + Fore.RED + str(ctext,) + Style.RESET_ALL)
        elif color == 2:
            return (Style.NORMAL + Fore.GREEN + str(ctext,) + Style.RESET_ALL)
        elif color == 3:
            return (Style.NORMAL + Fore.BLUE + str(ctext,) + Style.RESET_ALL)
        elif color == 4:
            return (Style.NORMAL + Fore.YELLOW + str(ctext,) + Style.RESET_ALL)
        elif color == 5:
            return (Style.NORMAL + Fore.MAGENTA + str(ctext,) + Style.RESET_ALL)
        elif color == 6:
            return (Style.NORMAL + Fore.LIGHTBLACK_EX + str(ctext,) + Style.RESET_ALL)
        else:
            return False
        
    # method 'concatenate_colortext_text' - concatenate formatted heading and standard body
    def concatenate_colortext_text(color, heading, body):
        if heading == '':
            return str(str(textcolor.format(color, heading)) + str(body))
        else:
            return str(str(textcolor.format(color, heading)) + " " + str(body))

# object 'iostream' { (takes no parameters) -> null }
class iostream:

    # method 'log' - display optionally formatted string on standard output
    def log(text, color=0, header=''):
        if color <= 6:
            print(textcolor.concatenate_colortext_text(color, header, text))
        else:
            print(str(text))
        return

    # method 'confirm' - return boolean from yes/no confirmation prompt
    def confirm(prompt, color=0, header=''):
        msg = str(prompt + " (y/N) >>> ")
        if color <= 6:
            next = input(textcolor.concatenate_colortext_text(color, header, msg))
        else:
            next = input(str(msg))
        if next.lower() == 'y':
            return True
        return False

    # method 'input' - return string from standard input
    def input(prompt, color=0, header=''):
        msg = str(prompt + " >>> ")
        if color <= 6:
            return input(textcolor.concatenate_colortext_text(color, header, msg))
        else:
            return input(str(msg))

# object 'shell' { (takes no parameters) -> null }
class shell:

    # method 'clear' - clear the command line
    def clear():
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'unix':
            os.system('clear')
        return
