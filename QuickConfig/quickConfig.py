import json
from bin.coloramasetup import *

def viewSetting(viewedSetting):
    with open("config/preferences.json", "r") as f:
        configFile = json.load(f)
    try:
        print(viewedSetting, "|", configFile[viewedSetting])
    except:
        print(f"{bright}{red}ERROR:{r} setting does not exist")

def setSetting(changedSetting, value):
    with open("config/preferences.json", "r") as f:
        configFile = json.load(f)
    if changedSetting in configFile:
        configFile[changedSetting] = value
        with open("config/preferences.json", "w") as f:
            f.write(json.dumps(configFile))
        print("Setting changed. Reload Nanoshell to apply changes. Type 'reload'")
    else:
        print(f"{bright}{red}ERROR:{r} setting does not exist")

def listSettings():
    with open("config/preferences.json", "r") as f:
        configFile = json.load(f)
    for setting, value in configFile.items():
        print(f"{setting} | {value}")

def setDefault(changedSetting):
    with open("config/preferences.json") as f:
        configFile = json.load(f)
    with open("config/preferences_default.json") as fd:
        defaultConfigFile = json.load(fd)
    if changedSetting in configFile:
        configFile[changedSetting] = defaultConfigFile[changedSetting]
        with open("config/preferences.json", "w") as f:
            f.write(json.dumps(configFile))
        print("Setting set to default. Reload Nanoshell to apply changes. Type 'reload'")
    else:
        print(f"{bright}{red}ERROR:{r} setting does not exist.")

def argumentParser(args):
    if args.startswith("config "):
        split_args = args.split(" ", 4)

        if len(split_args) >= 4:
            option = split_args[1]
            setting = split_args[2]
            settingValue = split_args[3]
            if option == "set":
                setSetting(setting, settingValue)
            elif option == "default":
                setDefault(setting)
            elif option == "list":
                listSettings()
            else:
                print("Command syntax: config <set|default|list|view> [setting] [value]")

        elif len(split_args) >= 3:
            option = split_args[1]
            setting = split_args[2]
            if option == "default":
                setDefault(setting)
            elif option == "view":
                viewSetting(setting)
            elif option == "list":
                listSettings()
            else:
                print("Command syntax: config <set|default|list|view> [setting] [value]")

        elif len(split_args) >= 2:
            option = split_args[1]
            if option == "list":
                listSettings()
            else:
                print("Command syntax: config <set|default|list|view> [setting] [value]")
        else:
            print("Command syntax: config <set|default|list|view> [setting] [value]")
    
    elif args == "config":
        print("Command syntax: config <set|default|list|view> [setting] [value]")

    else:
        pass