import dload, shutil, os
from bin.coloramasetup import *

addonList = []

def checkForRequest(prompt):
    if prompt != "install" or prompt != "install ": return prompt.replace("install ", "")
    else: return ""

def downloadRepo():
    print("Clone addons repo")
    dload.git_clone("https://github.com/Kwadratz/nanoshell-addons.git")
    print("Organize folders...")
    shutil.move("./addons/AddonInstaller/nanoshell-addons/nanoshell-addons-main", "./addons/AddonInstaller/")
    shutil.rmtree("./addons/AddonInstaller/nanoshell-addons")
    os.rename("./addons/AddonInstaller/nanoshell-addons-main", "./addons/AddonInstaller/addonsRepo")
    print("Remove unecessary files")
    os.remove("./addons/AddonInstaller/addonsRepo/.gitignore")
    os.remove("./addons/AddonInstaller/addonsRepo/LICENSE")
    os.remove("./addons/AddonInstaller/addonsRepo/README.md")

def fetchAddons():
    global addonList
    print("Retrieve addon list")
    addonList = os.listdir("./addons/AddonInstaller/addonsRepo")
    print(addonList)

def cleanUp():
    print("Delete cloned addons repo")
    shutil.rmtree("./addons/AddonInstaller/addonsRepo")
    print("Installation complete. Please exit Nanoshell and run 'run.py'.")

def installer(pickedAddon):
    addonRelativePath = os.path.abspath(os.path.join("./addons/AddonInstaller/addonsRepo", pickedAddon))
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
        print({dim}addon{r})
    pickedAddon = input(f"\nEnter the name of the addon you'd like to install {dim}>{r} ")
    if pickedAddon != "":
        if pickedAddon in addonList:
            installAddon(pickedAddon)
        else:
            os.system('cls' if os.name=='nt' else 'clear')
            shutil.rmtree("./addons/AddonInstaller/addonsRepo")
            input(f"{c.RED}Unknown addon{r}{dim}, press [ENTER] to continue...{r}")
            menu()

def installAddon(request):
    if request in addonList:
        addonRelativePath = os.path.abspath(os.path.join("./addons/AddonInstaller/addonsRepo", request)) # pick addon relative path
        destinationPath = os.path.abspath(os.path.join("./addons", request)) # move picked addon to addons/
        if os.path.exists(destinationPath):
            print(f"{c.RED}Destination path already exists. Deleting existing directory.{r}")
            shutil.rmtree(destinationPath)
        shutil.copytree(addonRelativePath, destinationPath)
        cleanUp()
        shutil.rmtree("./addons/AddonInstaller/addonsRepo") # remove tree addonsrepo
        print(f"{r}{c.GREEN}Successfully installed {request}")
        print(f"{r}{dim}To apply changes, restart or reload your Nanoshell instance ('reload' command){r}")

def main(prompt):
    addonRequest = checkForRequest(prompt)
    downloadRepo()
    fetchAddons()
    if addonRequest == "": menu()
    else: installAddon(addonRequest)