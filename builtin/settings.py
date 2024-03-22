import os
from bin.coloramasetup import *

def settings(prompt):
    prompt = prompt.replace("settings ", "")
    if prompt == "accentcolor" or prompt == "accent":
        changeAccent()
    else:
        print(f"{a}{bright}Nanoshell Settings{r}")
        print(f"""
            1. Change accent color
        """)
        match input(f"{a}{bright}Type number or leave blank to return to Nanoshell > "):
            case "1": changeAccent()
            case other: pass
            
def changeAccent():
    print(f"Settings > Change accent color")
    print(f"""
        1. Green {dim}(default){r}
        2. Red
        3. Yellow
        4. Blue
        5. Magenta
        6. Cyan
        7. White
    """)
    match input(f"{a}{bright}Type number or leave blank to return to the main menu > "):
        case "1": setAccent("c.GREEN")
        case "2": setAccent("c.RED")
        case "3": setAccent("c.YELLOW")
        case "4": setAccent("c.BLUE")
        case "5": setAccent("c.MAGENTA")
        case "6": setAccent("c.CYAN")
        case "7": setAccent("c.WHITE")
        case other: settings("")

def setAccent(color):
    with open("bin/coloramasetup.py", "w") as f:
        f.write(f"""from colorama import Fore as c
from colorama import Back as bg
from colorama import Style as s

white = c.WHITE
dim = s.DIM
bright = s.BRIGHT
green = c.GREEN
light_green = c.LIGHTGREEN_EX
red = c.RED
a = {color}
r = s.RESET_ALL""")
        f.close()
    print(f"{red}You'll have to reload Nanoshell to apply changes. {r}{dim}Type 'reload'{r}")