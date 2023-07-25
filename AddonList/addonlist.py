import os

def list_addons(folder_path):
    addons_list = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            addons_list.extend(list_addons(item_path))
        elif item.endswith(".json"):
            addon_name = item[:-5]
            if not os.path.exists(os.path.join(folder_path, addon_name + ".py")):
                continue
            addons_list.append(addon_name)
    return addons_list

def addonListMain(prompt):
    addons_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    addons_list = list_addons(addons_dir)

    print("Installed Addons:")
    for addon in addons_list:
        print(f"- {addon}")

    total_addons = len(addons_list)
    print(f"Addon count: {total_addons}")
