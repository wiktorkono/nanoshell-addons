import dload, shutil, os
from bin.coloramasetup import *

addonList = []

def checkForRequest(prompt):
    if prompt.startswith("install"):
        return prompt.replace("install", "").strip()
    else:
        return prompt


def downloadRepo():
    print("Clone addons repo")
    dload.git_clone("https://github.com/Kwadratz/nanoshell-addons.git")
    print("Organize folders...")
    shutil.move("./addons/builtin/nanoshell-addons/nanoshell-addons-main", "./addons/builtin/")
    shutil.rmtree("./addons/builtin/nanoshell-addons")
    os.rename("./addons/builtin/nanoshell-addons-main", "./addons/builtin/addonsRepo")
    print("Remove unecessary files")
    os.remove("./addons/builtin/addonsRepo/.gitignore")
    os.remove("./addons/builtin/addonsRepo/LICENSE")
    os.remove("./addons/builtin/addonsRepo/README.md")

def fetchAddons():
    global addonList
    print("Retrieve addon list")
    addonList = os.listdir("./addons/builtin/addonsRepo")
    print(addonList)

def cleanUp():
    print("Delete cloned addons repo")
    shutil.rmtree("./addons/builtin/addonsRepo")
    print("Installation complete. Please exit Nanoshell and run 'run.py'.")

def installer(pickedAddon):
    addonRelativePath = os.path.abspath(os.path.join("./addons/builtin/addonsRepo", pickedAddon))
    destinationPath = os.path.abspath(os.path.join("./addons", pickedAddon))
    if os.path.exists(destinationPath):
        print("Destination path already exists. Deleting existing directory.")
        shutil.rmtree(destinationPath)
    shutil.copytree(addonRelativePath, destinationPath)
    cleanUp()

def menu():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"{r}{c.GREEN}Addon Installer")
    print(f"{r}Listing all addons:\n")
    for addon in addonList:
        print(dim + addon + r)
    pickedAddon = input(f"\nEnter the name of the addon you'd like to install {dim}>{r} ")
    if pickedAddon != "":
        if pickedAddon in addonList:
            if pickedAddon == "builtin":
                print("AddonInstaller currently isn't able to install builtin. We're working on ways to fix this issue.")
            else:
                installAddon(pickedAddon)
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            shutil.rmtree("./addons/builtin/addonsRepo")
            input(f"{c.RED}Unknown addon{r}{dim}, press [ENTER] to continue...{r}")
            menu()

def installAddon(request):
    if request in addonList:
        addonRelativePath = os.path.abspath(os.path.join("./addons/builtin/addonsRepo", request))
        destinationPath = os.path.abspath(os.path.join("./addons", request))
        if os.path.exists(destinationPath):
            print(f"{c.RED}Destination path already exists. Deleting existing directory.{r}")
            shutil.rmtree(destinationPath)
        shutil.copytree(addonRelativePath, destinationPath)
        cleanUp()
        print(f"{r}{c.GREEN}Successfully installed {request}")
        print(f"{r}{dim}To apply changes, restart or reload your Nanoshell instance ('reload' command){r}")


def startInstaller(prompt):
    addonRequest = checkForRequest(prompt)
    downloadRepo()
    fetchAddons()
    if addonRequest == "":
        menu()
    else:
        if addonRequest in addonList:
            if addonRequest == "builtin":
                print("AddonInstaller currently isn't able to install builtin. We're working on ways to fix this issue.")
            else:
                installAddon(addonRequest)