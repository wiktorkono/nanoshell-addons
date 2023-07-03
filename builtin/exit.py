from bin.coloramasetup import *

def exit(prompt):
    if "-s" in prompt: quit()
    else:
        answer = input(f"{c.RED}Are you sure you want to exit?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
        answers = ["y", "Y", "yes", "t"]
        if answer in answers: quit()