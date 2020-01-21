# import only system from os
from os import system, name
import sys
import os, shutil, ctypes
from random import choice
import platform, random

# import sleep to show output for some time period
from time import sleep
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def center(string="", rp=""):
    """
    Automatically centers text based on console size. If no console size is available, it will resize to 80x25.

    :param string: the string to center
    :param rp: Accepts values "r" and "p", r will return the centered string,
               p will print the sting. leave it blank and it will just return the string.
               capitalization does not matter.
    :return:
    """
    cols, rows = shutil.get_terminal_size(fallback=(80, 25))
    cols = str(cols)
    rows = str(rows)

    rp = str(rp).lower()
    if rp == "r" or rp == "":
        return string.center(int(cols))
    elif rp == "p":
        print(string.center(int(cols)))


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

class QuietError(Exception):
    # All who inherit me shall not traceback, but be spoken of cleanly
    pass

class SupportError(QuietError):
    """
        raised manually when a function is not supported
    """
    __module__ = Exception.__module__

    def __init__(self, value):
        self.value = value

    def __str__(self):
        clear()
        if self.value.endswith(".") or self.value.endswith("!") or self.value.endswith("?") or self.value.endswith(">") or self.value.endswith("'") or self.value.endswith('"') or self.value.endswith(")"):
            return repr(self.value)
        else:
            return repr(self.value+".")

def getcolor():
    return str(choice([i for i in range(0, 255) if i not in [0,16,232,233,234,235,236,237,7]]))


def machine(sym1,sym2,sym3):
    color = str(choice([i for i in range(0, 255) if i not in [0, 16, 232, 233, 234, 235, 236, 237, 7]]))
    print("\u001b[0m")
    colorlen = " "*len(color)+ " "*17
    clear()
    center("   ____________________ ", "p")
    center("  /                   /|", "p")
    center(" /___________________/ |", "p")
    center(" |                  |  |", "p")
    center(" |   _____________  |  |", "p")
    center(colorlen + " |   | \u001b[38;5;"+color+"m"+sym1+"   "+sym2+"   "+sym3+"\u001b[38;5;7m |  |  |", "p")
    center(" |   ‾‾‾‾‾‾‾‾‾‾‾‾‾  |  |", "p")
    center(" |                  |  |", "p")
    center(" |                  |  |", "p")
    center(" /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/  |", "p")
    center("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   |", "p")
    center("                   |             \u001b[38;5;82m║║\u001b[38;5;7m   |   |", "p")
    center("                   |             \u001b[38;5;82m║║\u001b[38;5;7m   |   |", "p")
    center("|                  |   |", "p")
    center("|                  |   |", "p")
    center("|                  |  / ", "p")
    center("|                  | /  ", "p")
    center("|__________________|/   ", "p")


def linuxerror():
    clear()
    system('mode con: cols=' + str(len(platform.platform()) + 166))
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------" + "-" * len(platform.platform()))
    print("You are currently using the linux based OS: " + platform.platform() + ". Sadly linux is not currently supported. if you are interested in porting it, please create an issue on the Github page.")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------" + "-" * len(platform.platform()))

if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    linuxerror()

clear()
print(center('is this line of text center?'))
inp1 = input("[Yes/No] >>>").lower()
clear()
print('\u001b[38;5;9mi\u001b[38;5;10ms \u001b[38;5;11mt\u001b[38;5;12mh\u001b[38;5;13mi\u001b[38;5;14ms \u001b[38;5;15ml\u001b[38;5;14mi\u001b[38;5;13mn\u001b[38;5;12me \u001b[38;5;11mo\u001b[38;5;10mf \u001b[38;5;9mt\u001b[38;5;10me\u001b[38;5;11mx\u001b[38;5;12mt \u001b[38;5;13mC\u001b[38;5;14mo\u001b[38;5;15ml\u001b[38;5;14mo\u001b[38;5;13mr\u001b[38;5;12mf\u001b[38;5;11mu\u001b[38;5;10ml\u001b[38;5;9m?\u001b[38;5;7m')
inp2 = input("[Yes/No] >>>")

if inp1 and inp2 == "no":
    raise SupportError('Unable to center text and color is not available, please download the No Color, Uncentered version: <link here>')
elif inp1 == "no" and inp2 != "no":
    raise SupportError('Unable to center text, please download the Uncentered version: <link here>')
elif inp2 == "no" and inp1 != "no":
    raise SupportError(center('Color is not available, please download the No Color version: <link here>'))

def symbols():
    symbollist = ["!","@","#","$","%"]
    sym1 = random.choice(symbollist)
    sym2 = random.choice(symbollist)
    sym3 = random.choice(symbollist)
    return sym1, sym2, sym3

def spin():
    try:
        bet = int(input("How much do you bet (without dollar sign) >>> "))
    except:
        print("That was not a number, please input a number.")
        spin()
    for i in range(5):
        sleep((i + 1) / 10)
        sym1,sym2,sym3 = symbols()
        machine(sym1,sym2,sym3)
        sleep((i + 1) / 10)
        sym1, sym2, sym3 = symbols()
        machine(sym1, sym2, sym3)
        sleep((i + 1) / 10)
        sym1, sym2, sym3 = symbols()
        machine(sym1, sym2, sym3)

    return sym1,sym2,sym3
