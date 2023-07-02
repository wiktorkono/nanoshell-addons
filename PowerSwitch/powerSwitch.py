from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem, CommandItem
import os

def powerOff():
    os.system("shutdown /s /t 0")
    exit()

def restart():
    os.system("shutdown /f /t 0")
    exit()

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    exit()

def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    exit()

def hibernate():
    os.system("shutdown /h")
    exit()

def showPowerMenu(prompt):
    menu = ConsoleMenu("PowerSwitch", "Control your PC's power status.")
    power_item = FunctionItem("Shutdown", powerOff)
    restart_item = FunctionItem("Restart", restart)
    sleep_item = FunctionItem("Sleep", sleep)
    lock_item = FunctionItem("Lock", lock)
    hibernate_item = FunctionItem("Hibernate", hibernate)

    menu.append_item(power_item)
    menu.append_item(restart_item)
    menu.append_item(sleep_item)
    menu.append_item(lock_item)
    menu.append_item(hibernate_item)
    menu.show()