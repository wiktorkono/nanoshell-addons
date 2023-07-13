import os
import shutil

def getInstalledAddons():
    global installed_addons
    global addons_path
    addons_path = os.path.abspath("./addons")
    print(f"Addons folder absolute path: {addons_path}")
    installed_addons = [name for name in os.listdir(addons_path) if os.path.isdir(os.path.join(addons_path, name))]
    print(f"Get installed addons: {installed_addons}")
    os.system("cls")

def uninstallAddon(pickedAddon):
    uninstallPath = os.path.join(addons_path, pickedAddon)
    print("Create uninstall path")
    shutil.rmtree(uninstallPath)
    print("Remove path")
    os.system("cls")
    print("Uninstall complete.\nPlease reload Nanoshell to avoid any unexpected issues.")

def uninstallMenu():
    global pickedAddon
    os.system("cls")
    print("Addon Uninstaller\n\nInstalled addons:\n")
    for addon in installed_addons:
        print(addon)
    pickedAddon = input("\nEnter the name of the addon you'd like to uninstall: ")
    if pickedAddon == "builtin":
        os.system("cls")
        print("This addon cannot be uninstalled.")
        input()
        os.system("cls")
        uninstallMenu()
    else:
        if pickedAddon in installed_addons:
            uninstallAddon(pickedAddon)
        else:
            os.system("cls")
            print(f"Couldn't find {pickedAddon}.")

def uninstallerMain(prompt):
    getInstalledAddons()
    if prompt.startswith('uninstall '):
        pickedAddon = prompt.split(' ', 1)[1]
        if pickedAddon == "builtin":
            print("This addon cannot be uninstalled.")
        else:
            if pickedAddon in installed_addons:
                uninstallAddon(pickedAddon)
            else:
                os.system("cls")
                print(f"Couldn't find {pickedAddon}.")
    else:
        uninstallMenu()
