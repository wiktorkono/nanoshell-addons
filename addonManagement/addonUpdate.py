import shutil, os, dload, json
from bin.coloramasetup import a as accentColor, r as resetColor, dim, red

localAddonList = os.listdir("./addons")
addonDictionary = {}

def downloadRepo():
    print(f"{dim}Cloning addons repository...")
    dload.git_clone("https://github.com/Kwadratz/nanoshell-addons.git")
    print(f"{dim}Organizing folders...")
    shutil.move("./addons/addonManagement/nanoshell-addons/nanoshell-addons-main", "./addons/addonManagement/")
    shutil.rmtree("./addons/addonManagement/nanoshell-addons")
    os.rename("./addons/addonManagement/nanoshell-addons-main", "./addons/addonManagement/addonsRepo")
    print(f"{dim}Removing unnecessary files... {resetColor}")
    os.remove("./addons/addonManagement/addonsRepo/.gitignore")
    os.remove("./addons/addonManagement/addonsRepo/LICENSE")
    os.remove("./addons/addonManagement/addonsRepo/README.md")

def fetchAddons():
    global repoAddonList
    print(f"{dim}Retrieving repo addon list...")
    repoAddonList = os.listdir("./addons/addonManagement/addonsRepo")
    print(f"{repoAddonList} {resetColor}")

def cleanUp():
    print(f"{dim}Deleting cloned addons repo... {resetColor}")
    shutil.rmtree("./addons/addonManagement/addonsRepo")

def compare_versions(v1: str, v2: str) -> int:  # v1 - repo version, v2 - local version
    """Compares two version strings in the format 'x.y.z'.
    
    Returns:
    -1 if v1 (repo) is older than v2 (local),
     0 if they are equal,
     1 if v1 (repo) is newer than v2 (local).
    """
    parts1 = list(map(int, v1.split('.')))
    parts2 = list(map(int, v2.split('.')))

    # Compare each part
    for p1, p2 in zip(parts1, parts2):
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1

    # If all compared parts are equal but lengths differ
    if len(parts1) < len(parts2):
        return -1
    elif len(parts1) > len(parts2):
        return 1
    
    return 0  # They're equal

def createUneccessaryAddonList(localAddonList, repoAddonList):
    # returns a new list with addons in the repo but not on the local machine (these don't need to be checked for updates)
    set1 = set(localAddonList)
    return [addon for addon in repoAddonList if addon not in set1]

def removeUneccessaryAddons(uneccessaryAddonList):
    for addon in uneccessaryAddonList:
        uninstallPath = os.path.join("./addons/addonManagement/addonsRepo", addon)
        print(f"{dim}(temp) Removed uneccessary addon:", uninstallPath)
        shutil.rmtree(uninstallPath)
    print(f"{dim}All uneccessary addons from temporary addonsRepo removed.{resetColor}")
    if os.path.exists("./addons/addonManagement/addonsRepo/addonManagement"):
        shutil.rmtree("./addons/addonManagement/addonsRepo/addonManagement")
        print(f"{dim}ADDON addonManagement cannot be auto-updated - update checks for it ARE SKIPPED!{resetColor}")
        localAddonList.remove("addonManagement")

def checkIfAddonIsExternal(localAddonList, repoAddonList):
    # checks for addons that exist on the local machine but not in the repo
    matchingAddonCount = 0
    externalAddonCount = 0
    global addonsToCheck
    addonsToCheck = []
    for addon in localAddonList:
        if addon in repoAddonList:
            print(f"{dim}Found matching addon {addon} in nanoshell-addons repo")
            matchingAddonCount += 1
            addonDictionary[addon] = {"type": "repo"}
            addonsToCheck.append(addon)
        else:
            print(f"{dim}Could not find {addon} in nanoshell-addons repo: will be treated as an external addon!")
            externalAddonCount += 1
            addonDictionary[addon] = {"type": "external"}
    print(f"{dim}Updated addonDictionary")
    print(f"{dim}Found {matchingAddonCount} matching addon(s), {externalAddonCount} external addon(s){resetColor}")

def addonVersionChecker(addon, addonLocation):
    # gets and stores versions of addons
    if addonLocation == "local":
        addon_path = os.path.join("./addons", addon)
    elif addonLocation == "repo":
        addon_path = os.path.join("./addons/addonManagement/addonsRepo", addon)
    print(f"{dim}Set addon_path to {addon_path}")

    if not os.path.exists(addon_path):
        print(f"{dim}Addon '{addon}' not found.")
        return
    
    json_files = [f for f in os.listdir(addon_path) if f.endswith(".json")]

    if len(json_files) == 1:
        # Only one JSON file: Treat it as a direct addon
        json_file_path = os.path.join(addon_path, json_files[0])
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
                if "addonVersion" in data:
                    print(f"[{addonLocation}] {addon} -", data['addonVersion'])

                    # Ensure both versions are set without overwriting
                    if addonLocation == "local":
                        if addon not in addonDictionary:
                            addonDictionary[addon] = {"addons": {}}
                        addonDictionary[addon]["localVersion"] = data['addonVersion']
                    elif addonLocation == "repo":
                        if addon not in addonDictionary:
                            addonDictionary[addon] = {"addons": {}}
                        addonDictionary[addon]["repoVersion"] = data['addonVersion']

                else:
                    print(f"addonVersion not found in {json_files[0]} - JSON is borked.")
        except json.JSONDecodeError:
            print(f"Error loading JSON from {json_file_path}. The file might be empty or contain invalid JSON.")

    elif len(json_files) > 1:
        # Multiple JSON files: Treat them as sub-addons
        for filename in json_files:
            json_file_path = os.path.join(addon_path, filename)
            try:
                with open(json_file_path, "r") as file:
                    data = json.load(file)
                    if "addonVersion" in data:
                        addon_name = filename[:-5]  # remove ".json" extension
                        print(f"[{addonLocation}] {addon}/{addon_name} -", data['addonVersion'])

                        # Initialize sub-addon entry if not present
                        if addon not in addonDictionary:
                            addonDictionary[addon] = {"addons": {}}
                        if "addons" not in addonDictionary[addon]:
                            addonDictionary[addon]["addons"] = {}
                        if addon_name not in addonDictionary[addon]["addons"]:
                            addonDictionary[addon]["addons"][addon_name] = {}

                        if addonLocation == "local":
                            # Set the local version for the sub-addon
                            addonDictionary[addon]["addons"][addon_name]["localVersion"] = data["addonVersion"]
                        elif addonLocation == "repo":
                            # Set the repo version for the sub-addon
                            addonDictionary[addon]["addons"][addon_name]["repoVersion"] = data["addonVersion"]

                    else:
                        print(f"addonVersion not found in {filename} - JSON is borked.")
            except json.JSONDecodeError:
                print(f"Error loading JSON from {json_file_path}. The file might be empty or contain invalid JSON.")

def getAddonVersions(addon):
    # gets local and repo versions for one addon
    if addon not in addonDictionary:
        print(f"Addon '{addon}' not found in addonDictionary.")
        return None
    
    addon_data = addonDictionary[addon]
    addon_versions = {}

    # Check main addon versions
    if "localVersion" in addon_data:
        addon_versions["localVersion"] = addon_data["localVersion"]
    if "repoVersion" in addon_data:
        addon_versions["repoVersion"] = addon_data["repoVersion"]

    # Check sub-addons (if any)
    if "addons" in addon_data:
        addon_versions["subaddons"] = {}
        for subaddon, subaddon_data in addon_data["addons"].items():
            subaddon_versions = {}
            if "localVersion" in subaddon_data:
                subaddon_versions["localVersion"] = subaddon_data["localVersion"]
            if "repoVersion" in subaddon_data:
                subaddon_versions["repoVersion"] = subaddon_data["repoVersion"]
            addon_versions["subaddons"][subaddon] = subaddon_versions

    return addon_versions

def createAddonListNoExternal():
    # creates addonlist without external addons
    localAddonListNoExternal = []
    for addon in localAddonList:
        addon_data = addonDictionary[addon]
        if "type" in addon_data:
            if addon_data["type"] == "repo":
                localAddonListNoExternal.append(addon)
        else:
            print(f"{dim}[WARNING] No value for 'type' was found for {addon} in addonDictionary. It is very likely that something has failed or will fail miserably soon.{resetColor}")
    return localAddonListNoExternal

def createAddonListExternalOnly(localAddonListNoExternal):
    # creates addonlist with only external addons
    localAddonListExternalOnly = []
    for addon in localAddonList:
        if addon not in localAddonListNoExternal:
            localAddonListExternalOnly.append(addon)
    return localAddonListExternalOnly

def checkIfUpdateRequired(addon_versions, addon):

    # Check if the main addon has versions
    if "repoVersion" in addon_versions and "localVersion" in addon_versions:
        repo_version = addon_versions["repoVersion"]
        local_version = addon_versions["localVersion"]
        updateStatus = compare_versions(repo_version, local_version)
        print(f"update status for addon: {updateStatus}")

        # Ensure the main addon entry exists
        if addon not in addonDictionary:
            addonDictionary[addon] = {}

        if "updateStatus" not in addonDictionary[addon]:
            addonDictionary[addon]["updateStatus"] = ""

        if updateStatus == -1:
            addonDictionary[addon]["updateStatus"] = "dev"
        elif updateStatus == 0:
            addonDictionary[addon]["updateStatus"] = "no"
        elif updateStatus == 1:
            addonDictionary[addon]["updateStatus"] = "yes"

        print("updated addonDictionary entry")

    # Check if there are subaddons
    if "subaddons" in addon_versions:
        for subaddon, subaddon_versions in addon_versions["subaddons"].items():
            repo_version = subaddon_versions.get("repoVersion")
            local_version = subaddon_versions.get("localVersion")
            updateStatus = compare_versions(repo_version, local_version)
            print(f"update status for subaddon '{subaddon}': {updateStatus}")

            # Ensure the addon and subaddon structure exists
            if addon not in addonDictionary:
                addonDictionary[addon] = {}  # Initialize addon entry if missing
            if "addons" not in addonDictionary[addon]:
                addonDictionary[addon]["addons"] = {}  # Initialize subaddons dict
            if subaddon not in addonDictionary[addon]["addons"]:
                addonDictionary[addon]["addons"][subaddon] = {}  # Initialize specific subaddon

            if "updateStatus" not in addonDictionary[addon]["addons"][subaddon]:
                addonDictionary[addon]["addons"][subaddon]["updateStatus"] = ""

            if updateStatus == -1:
                addonDictionary[addon]["addons"][subaddon]["updateStatus"] = "dev"
            elif updateStatus == 0:
                addonDictionary[addon]["addons"][subaddon]["updateStatus"] = "no"
            elif updateStatus == 1:
                addonDictionary[addon]["addons"][subaddon]["updateStatus"] = "yes"

            print("updated addonDictionary entry")

def updateAddons(toCopyOver):
    # copies over folders of addons that need updating
    print(f"{dim}Addons will now update:{resetColor}")
    for addonFolder in toCopyOver:
        localAddonPath = os.path.join("./addons", addonFolder)
        repoAddonPath = os.path.join("./addons/addonManagement/addonsRepo", addonFolder)
        shutil.rmtree(localAddonPath)
        shutil.copytree(repoAddonPath, localAddonPath)
        print(f"Updated {accentColor}{addonFolder}{resetColor}")
    print(f"\n{accentColor}All addons updated.{resetColor}")

def showUpdateStatusScreen(addon_dict):
    toCopyOver = []
    toUpdateCount = 0
    print(f"{resetColor}{accentColor}\nAddon update{resetColor}\n")
    for addon, details in addon_dict.items():
        if details.get("type") == "external":
            print(f"{dim}[EXTERNAL] {addon} - Cannot check for updates.{resetColor}")
            continue

        # Main addon update status
        update_status = details.get("updateStatus", "unknown")
        if update_status == "yes":
            repo_ver = details.get("repoVersion")
            local_ver = details.get("localVersion")
            toCopyOver.append(addon)
            toUpdateCount += 1
            print(f"[UPDATE AVAILABLE] {accentColor}{addon}{resetColor} [{local_ver} ---> {repo_ver}]")
        elif update_status == "no":
            print(f"[UP-TO-DATE] {accentColor}{addon}{resetColor}")
        elif update_status == "dev":
            repo_ver = details.get("repoVersion")
            local_ver = details.get("localVersion")
            print(f"[PRERELEASE] {accentColor}{addon}{resetColor} [local: {local_ver} | repo: {repo_ver}]")
        else:
            print(f"{accentColor}{addon}{resetColor}")

        subAddonsToUpdate = 0
        devSubAddons = 0

        # Check for subaddons
        if "addons" in details:
            for subaddon, subdetails in details["addons"].items():
                sub_update_status = subdetails.get("updateStatus", "unknown")
                if sub_update_status == "yes":
                    sub_local_ver = subdetails.get("localVersion")
                    sub_repo_ver = subdetails.get("repoVersion")
                    subAddonsToUpdate += 1
                    toUpdateCount += 1
                    toCopyOver.append(addon)
                    print(f"  └── [UPDATE AVAILABLE] {accentColor}{subaddon}{resetColor} [{sub_local_ver} ---> {sub_repo_ver}]")
                elif sub_update_status == "no":
                    print(f"  └── [UP-TO-DATE] {accentColor}{subaddon}{resetColor}")
                elif sub_update_status == "dev":
                    sub_local_ver = subdetails.get("localVersion")
                    sub_repo_ver = subdetails.get("repoVersion")
                    devSubAddons += 1
                    print(f"  └── [PRERELEASE] {accentColor}{subaddon}{resetColor} [local: {sub_local_ver} | repo: {sub_repo_ver}]")
                else:
                    print(f"  └── [UNKNOWN] {accentColor}{subaddon}{resetColor}")
        if subAddonsToUpdate >= 1 and devSubAddons >= 1:
            print(f"\n{red}[WARNING] {resetColor} One or more subaddons need an update, but you also have a prerelease addon. Updating will overwrite your prerelease addon with the latest repo version!")
    if toUpdateCount >= 1:
        updateConfirmation = input(f"\nWould you like to install all available updates? (y/N) > ")
        if updateConfirmation == "y" or updateConfirmation == "Y":
            updateAddons(toCopyOver)
        else:
            pass
    else:
        print(f"\n{accentColor}All addons are up to date.{resetColor}")
        pass

def addonUpdateBegin():
    downloadRepo()
    fetchAddons()
    removeUneccessaryAddons(createUneccessaryAddonList(localAddonList, repoAddonList))
    fetchAddons()
    checkIfAddonIsExternal(localAddonList, repoAddonList)

    for addon in localAddonList:
        addonVersionChecker(addon, "repo")
        addonVersionChecker(addon, "local")

    localAddonListNoExternal = createAddonListNoExternal()
    print(f"{dim}Created localAddonListNoExternal: {localAddonListNoExternal}")

    localAddonListExternalOnly = createAddonListExternalOnly(localAddonListNoExternal)
    print(f"{dim}Created localAddonListExternalOnly: {localAddonListExternalOnly}")

    for addon in localAddonListNoExternal:
        addon_versions = getAddonVersions(addon)
        print(f"{dim}Addon versions for {addon}: {addon_versions}")
        checkIfUpdateRequired(addon_versions, addon)

    showUpdateStatusScreen(addonDictionary)
    cleanUp()