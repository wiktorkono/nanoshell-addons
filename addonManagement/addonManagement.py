import os, shutil, dload
import json
from colorama import Fore, Style
from bin.coloramasetup import *

addonList = []


def mainAddonMng(prompt):
    if "install" in prompt and "uninstall" not in prompt:
        prompt = prompt.replace("install", "")
        prompt = prompt.replace("addons", "")
        prompt = prompt.replace(" ", "")
        downloadRepo()
        fetchAddons()
        if prompt == "":
            installMenu()
        else:
            installAddon(prompt)
    elif "uninstall" in prompt:
        prompt = prompt.replace("uninstall", "")
        prompt = prompt.replace("addons", "")
        prompt = prompt.replace(" ", "")
        if prompt == "":
            uninstallMenu()
        else:
            uninstallAddon(prompt)
    elif "list" in prompt or prompt == "addons":
        listAddons()
    elif "ver" in prompt:
        prompt = prompt.replace("ver", "")
        prompt = prompt.replace("addons", "")
        prompt = prompt.replace(" ", "")
        if prompt == "":
            listAddonVersions()
        else:
            getAddonVersion(prompt)


def getInstalledAddons(total=False):
    addons_dir = os.path.join(os.path.dirname(__file__), "..")
    if total:
        return len(os.listdir(addons_dir))
    else:
        return os.listdir(addons_dir)


# INSTALL

def downloadRepo():
    print(f"{dim}Cloning addons repository...")
    dload.git_clone("https://github.com/Kwadratz/nanoshell-addons.git")
    print(f"{dim}Organizing folders...")
    shutil.move("./addons/addonManagement/nanoshell-addons/nanoshell-addons-main", "./addons/addonManagement/")
    shutil.rmtree("./addons/addonManagement/nanoshell-addons")
    os.rename("./addons/addonManagement/nanoshell-addons-main", "./addons/addonManagement/addonsRepo")
    print(f"{dim}Removing unnecessary files...")
    os.remove("./addons/addonManagement/addonsRepo/.gitignore")
    os.remove("./addons/addonManagement/addonsRepo/LICENSE")
    os.remove("./addons/addonManagement/addonsRepo/README.md")


def fetchAddons():
    global addonList
    print(f"{dim}Retrieving addon list...")
    addonList = os.listdir("./addons/addonManagement/addonsRepo")
    print(addonList)


def cleanUp():
    print("Deleting cloned addons repo...")
    shutil.rmtree("./addons/addonManagement/addonsRepo")
    print("Installation complete. Please exit Nanoshell and run 'run.py'.")


def installer(pickedAddon):
    addonRelativePath = os.path.abspath(os.path.join("./addons/addonManagement/addonsRepo", pickedAddon))
    destinationPath = os.path.abspath(os.path.join("./addons", pickedAddon))
    if os.path.exists(destinationPath):
        print("Destination path already exists. Deleting existing directory.")
        shutil.rmtree(destinationPath)
    shutil.copytree(addonRelativePath, destinationPath)
    cleanUp()


def installMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{r}{a}Addon Installer")
    print(f"{r}Listing all addons:\n")
    for addon in addonList:
        print(dim + addon + r)
    pickedAddon = input(f"\nEnter the name of the addon you'd like to install {dim}>{r} ")
    if pickedAddon != "":
        if pickedAddon in addonList:
            installAddon(pickedAddon)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            shutil.rmtree("./addons/addonManagement/addonsRepo")
            input(f"{red}Unknown addon{r}{dim}, press [ENTER] to continue...{r}")
            installMenu()


def installAddon(request):
    if request in addonList:
        addonRelativePath = os.path.abspath(os.path.join("./addons/addonManagement/addonsRepo", request))
        destinationPath = os.path.abspath(os.path.join("./addons", request))
        if os.path.exists(destinationPath):
            print(f"{red}Destination path already exists. Deleting existing directory.{r}")
            shutil.rmtree(destinationPath)
        shutil.copytree(addonRelativePath, destinationPath)
        cleanUp()
        print(f"{r}{a}Successfully installed {request}")
        print(f"{r}{dim}To apply changes, restart or reload your Nanoshell instance ('reload' command){r}")


# UNINSTALL

def uninstallAddon(pickedAddon):
    installed_addons = getInstalledAddons()
    addons_path = os.path.join(os.path.dirname(__file__), "..")
    uninstallPath = os.path.join(addons_path, pickedAddon)
    if pickedAddon in installed_addons:
        shutil.rmtree(uninstallPath)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Uninstall complete.\nPlease reload Nanoshell to avoid any unexpected issues.")
    else:
        print(f"Couldn't find {pickedAddon}")


def uninstallMenu():
    installed_addons = getInstalledAddons()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{r}{a}Addon Uninstaller")
    print(f"{r}Listing all addons:\n")
    for addon in installed_addons:
        print(dim + addon + r)
    pickedAddon = input(f"\nEnter the name of the addon you'd like to uninstall {dim}>{r} ")
    if pickedAddon in installed_addons:
        uninstallAddon(pickedAddon)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Couldn't find {pickedAddon}.")


# LIST

def listAddons():
    addons_list = getInstalledAddons()
    total = getInstalledAddons(True)
    print(f"{a}Installed addons{r}{dim} ({total} total)")
    for addon in addons_list:
        print(f"{dim}\t{addon}{r}")
    print(f"{dim}You can update your addons by typing{r}{a} addons update{r}")
    print(f"{dim}Not needing any of these? Type {r}{a}addons uninstall {white}[name]{r}")
    print(f"{dim}Check the version of an addon: type {r}{a}addons ver {white}[name]")


# VER


def getAddonVersion(addon):
    addons_path = os.path.join(os.path.dirname(__file__), "..")
    addon_path = os.path.join(addons_path, addon)
    
    if not os.path.exists(addon_path):
        print(f"Addon '{addon}' not found.")
        return
    
    max_name_length = 0
    max_version_length = 0
    
    for filename in os.listdir(addon_path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(addon_path, filename)
            try:
                with open(json_file_path, 'r') as file:
                    data = json.load(file)
                    if "name" in data:
                        addonFriendlyName = data['name']
                        max_name_length = max(max_name_length, len(addonFriendlyName))
                    if "addonVersion" in data:
                        max_version_length = max(max_version_length, len(data['addonVersion']))
                        print(f"{addon:<{max_name_length}} / {addonFriendlyName:<{max_name_length}} || {data['addonVersion']:<{max_version_length}}")
            except json.JSONDecodeError:
                print(f"Error loading JSON from {json_file_path}. The file might be empty or contain invalid JSON.")



def listAddonVersions():
    addons_path = os.path.join(os.path.dirname(__file__), "..")
    max_name_length = 0
    max_version_length = 0
    
    # find maximum lengths
    for addon in os.listdir(addons_path):
        addon_path = os.path.join(addons_path, addon)
        if os.path.isdir(addon_path):
            json_files = []
            
            for filename in os.listdir(addon_path):
                if filename.endswith(".json"):
                    json_files.append(filename)
            
            for json_file in json_files:
                json_file_path = os.path.join(addon_path, json_file)
                try:
                    with open(json_file_path, 'r') as file:
                        data = json.load(file)
                        if "name" in data:
                            addonFriendlyName = data['name']
                            max_name_length = max(max_name_length, len(addonFriendlyName))
                        if "addonVersion" in data:
                            max_version_length = max(max_version_length, len(data['addonVersion']))
                except json.JSONDecodeError:
                    print(f"Error loading JSON from {json_file_path}. The file might be empty or contain invalid JSON.")
    
    # print the addon versions with aligned "||"
    for addon in os.listdir(addons_path):
        addon_path = os.path.join(addons_path, addon)
        if os.path.isdir(addon_path):
            json_files = []
            
            for filename in os.listdir(addon_path):
                if filename.endswith(".json"):
                    json_files.append(filename)
            
            for json_file in json_files:
                json_file_path = os.path.join(addon_path, json_file)
                try:
                    with open(json_file_path, 'r') as file:
                        data = json.load(file)
                        if "name" in data:
                            addonFriendlyName = data['name']
                        else:
                            print(f"{addon} / {json_file} ({json_file_path}) does not contain a 'name' key. (addon might be broken?)")
                            continue # Skip to the next file if 'name' is missing
                        if "addonVersion" in data:
                            # Use the calculated maximum lengths for formatting
                            print(f"{addon:<{max_name_length}} / {addonFriendlyName:<{max_name_length}} || {data['addonVersion']:<{max_version_length}}")
                        else:
                            print(f"{addon} / {json_file} ({json_file_path}) does not contain an 'addonVersion' key. (addon might be broken?)")
                except json.JSONDecodeError:
                    print(f"Error loading JSON from {json_file_path}. The file might be empty or contain invalid JSON.")