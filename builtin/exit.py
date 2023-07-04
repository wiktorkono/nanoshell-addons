from bin.coloramasetup import *
import os

def clearFiles():
    with open(os.path.join("bin", "nanoshell-base.py"), "r") as f: nanoshellBase = f.read()
    with open(os.path.join("nanoshell.py"), "w") as f: f.write(nanoshellBase)
    with open(os.path.join("imports.py"), "w") as f: f.write("")

def exit(prompt):
    if "-kf" in prompt: clear = False # kp means keepFiles
    else: clear = True
    if "-s" in prompt:
        if clear: clearFiles()
        quit()
    else:
        answer = input(f"{c.RED}Are you sure you want to exit?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
        answers = ["y", "Y", "yes", "t"]
        if answer in answers: 
            if clear: clearFiles()
            quit()