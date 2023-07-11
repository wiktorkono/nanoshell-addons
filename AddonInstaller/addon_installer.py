import dload, shutil, os

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
    print(f"Picked addon relative path: {addonRelativePath}")
    destinationPath = os.path.abspath(os.path.join("./addons", pickedAddon))
    print("Move picked addon to addons/")

    if os.path.exists(destinationPath):
        print("Destination path already exists. Deleting existing directory.")
        shutil.rmtree(destinationPath)

    shutil.copytree(addonRelativePath, destinationPath)
    cleanUp()

def menu():
    global pickedAddon
    os.system('cls' if os.name=='nt' else 'clear')
    print("\tAddon installer")
    print("\nListing all addons:\n")
    for addon in addonList:
        print(addon)
    pickedAddon = input("\nEnter the name of the addon you'd like to install (case-sensitive!) > ")
    if pickedAddon in addonList:
        installer(pickedAddon)
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        shutil.rmtree("./addons/AddonInstaller/addonsRepo")
        print("Unknown addon")

def installAddon(request):
    if request != "":
        if pickedAddon in addonList:
            addonRelativePath = os.path.abspath(os.path.join("./addons/AddonInstaller/addonsRepo", pickedAddon)) # pick addon relative path
            destinationPath = os.path.abspath(os.path.join("./addons", pickedAddon)) # move picked addon to addons/
            if os.path.exists(destinationPath):
                print("Destination path already exists. Deleting existing directory.")
                shutil.rmtree(destinationPath)
            shutil.copytree(addonRelativePath, destinationPath)
            cleanUp()
            print("Delete cloned addons repo")
            shutil.rmtree("./addons/AddonInstaller/addonsRepo")
            print("Installation complete")
            userInput = input("Do you want to reload Nanoshell now? Y N")

def main(prompt):
    addonRequest = checkForRequest(prompt)
    downloadRepo()
    fetchAddons()
    if addonRequest == "": menu()
    else: installAddon(addonRequest)