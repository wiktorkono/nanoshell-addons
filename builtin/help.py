from bin.coloramasetup import *
import os, json

def main(prompt):
    addonList = [] #[0 name, 1 triggerCmd, 2 initFoo, 3 imports, 4 platform, 5 description]
    addons = os.listdir("addons")
    howManyAddons = 0
    howManyScripts = 0
    for addon in addons:
        howManyAddons += 1
        addonScripts = os.listdir(os.path.join("addons", addon))
        for obj in addonScripts:
            if obj.endswith(".json"):
                addonData = json.load(open(os.path.abspath(os.path.join("addons", addon, obj))))
                secondaryName = addonData["name"].replace(" ", "").replace("-", "").replace("_", "")
                addonList.append([addonData["name"], addonData["triggerCmd"], f"{secondaryName}{addonData['initFoo']}", addonData["imports"], addonData["platform"], addonData["description"]])
                howManyScripts += 1
    print(f"Now listing all available commands")

    for addon in addonList:
        print(f"{r}{a}{addon[1]}{r} {dim}>{r} {addon[5]} {dim}(from {addon[0]}){r}")