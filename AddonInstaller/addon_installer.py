import dload, shutil, os

addonList = []
pickedAddon = ""

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

def installer():
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
        installer()
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Unknown addon")

def main(prompt):
    downloadRepo()
    fetchAddons()
    menu()