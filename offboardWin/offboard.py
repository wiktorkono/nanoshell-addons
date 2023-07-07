import os
from bin.coloramasetup import *

def launchOffboard(prompt):
    if "shutdown" in prompt or "sd" in prompt:
        if "-ls" in prompt: os.system("shutdown /s /t 0") # ls means legacy shutdown
        else: 
            try:
                os.system("slidetoshutdown")
            except:
                answer = input(f"{c.RED}Are you sure you want to shut down your PC?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
                answers = ["y", "Y", "yes", "t"]
                if answer in answers: 
                    os.system("shutdown /s /t 0")
    if "restart" in prompt or "rs" in prompt:
        if "-s" in prompt: os.system("shutdown /f /t 0")
        else:
            answer = input(f"{c.RED}Are you sure you want to restart your PC?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
            answers = ["y", "Y", "yes", "t"]
            if answer in answers: 
                os.system("shutdown /f /t 0")
    if "sleep" in prompt or "sl" in prompt:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    if "lock" in prompt or "lk" in prompt:
        os.system("rundll32.exe user32.dll,LockWorkStation")
    if "hibernate" in prompt or "hb" in prompt:
        if "-s" in prompt: os.system("shutdown /h")
        else:
            answer = input(f"{c.RED}Are you sure you want to restart your PC?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
            answers = ["y", "Y", "yes", "t"]
            if answer in answers: 
                os.system("shutdown /h")

def shutdown(prompt):
    if "-ls" in prompt: os.system("shutdown /s /t 0") # ls means legacy shutdown
    else: 
        try:
            os.system("slidetoshutdown")
        except:
            answer = input(f"{c.RED}Are you sure you want to shut down your PC?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
            answers = ["y", "Y", "yes", "t"]
            if answer in answers: 
                os.system("shutdown /s /t 0")

def restart(prompt):
    if "-s" in prompt: os.system("shutdown /f /t 0")
    else:
        answer = input(f"{c.RED}Are you sure you want to restart your PC?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
        answers = ["y", "Y", "yes", "t"]
        if answer in answers: 
            os.system("shutdown /f /t 0")

def sleep(prompt): os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def lock(prompt): os.system("rundll32.exe user32.dll,LockWorkStation")

def hibernate(prompt):
    if "-s" in prompt: os.system("shutdown /h")
    else:
        answer = input(f"{c.RED}Are you sure you want to restart your PC?{r} {bg.RED}{c.WHITE}Y{r} {bg.RED}{c.WHITE}N{r} {c.LIGHTWHITE_EX}> {r}")
        answers = ["y", "Y", "yes", "t"]
        if answer in answers: 
            os.system("shutdown /h")