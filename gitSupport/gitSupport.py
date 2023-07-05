import json, os, webbrowser

commandNames = {
    "settings": "settings"
}

def getJSONdata():
    data = json.load(open("gitSupport.json"))
    global version, author, description, initcommand
    version = data["addonVersion"]
    author = data["author"]
    description = data["description"]
    initcommand = data["triggerCmd"]

def settings():
    print(f"""
    Git Support for Nanoshell - v{version}
    (C) {author} 2023""")
    print(f"""
    1. Change command names
    2. Check for updates
    3. License
    4. More from Kwadratz
    5. Exit
    """)
    match input("Select an option > "):
        case "1": changenames()
        case "2": checkforupdates()
        case "3": addonLicense()
        case "4": moreFromKwadratz()
        case other: exitAddon()

def gitsupport(prompt):
    if "settings" in prompt: settings()
    
    # W. I. P.