import os, json

def main(prompt):
    addonList = [] #[0 name, 1 triggerCmd, 2 initFoo, 3 imports]

    addons = os.listdir("addons")
    howManyAddons = 0
    print(f"Now listing addons: {addons}")
    print("Loading addons...")
    for addon in addons:
        howManyAddons += 1
        addonScripts = os.listdir(os.path.join("addons", addon))
        print(f"Now listing addon scripts: {addonScripts}")
        for obj in addonScripts:
            if obj.endswith(".json"):
                addonData = json.load(open(os.path.abspath(os.path.join("addons", addon, obj))))
                addonList.append([addonData["name"], addonData["triggerCmd"], addonData["initFoo"], addonData["imports"]])
    print("Successfully loaded addons")

    print("Reading the base file...")
    with open(os.path.join("bin", "nanoshell-base.py"), "r") as f: nanoshellBase = f.read() #reading the base file

    print("Writing the base file...")
    with open("nanoshell.py", "w") as f: f.write(nanoshellBase) #writing the main file

    print("Loading addons (part 1)...")
    with open("nanoshell.py", "a") as f: # here nanoshell.py is being initialized
        i = 0
        for addon in addonList:
            if i != 0: el = "el" # so it can be elif instead of if
            else: el = ""
            triggerCmd = addon[1]
            initFoo = addon[2]
            f.write(f"\n    {el}if prompt.startswith('{triggerCmd}'): {initFoo}(prompt)")
            i += 1

    print("Loading addons (part 2)...")
    with open("imports.py", "w") as f: # here imports.py is being cleared
        f.write("")

    print("Loading addons (part 3)...")
    with open("imports.py", "a") as f: # here imports are written to imports.py
        for addon in addonList:
            importLines = addon[3]
            for importLine in importLines:
                f.write(f"\nfrom {importLine[0]} import {importLine[1]}")

    print("Finished, reloading Nanoshell...")
    os.system("python nanoshell.py")