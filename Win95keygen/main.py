from addons.Win95keygen.functions import cd_keygen, oem_keygen

def uiPicker():
    key_pick = input("Enter key type (CD/oem): ")
    key_pick = key_pick.lower()

    if key_pick == "":
        key = cd_keygen()
        print(key)

    elif key_pick == "cd":
        key = cd_keygen()
        print(key)

    elif key_pick == "oem":
        key = oem_keygen()
        print(key)

    else:
        print("Invalid choice.")


def keyPicker(prompt):
    if prompt.startswith('win95keygen '):
        keyType = prompt.split(' ', 1)[1]
        keyType = keyType.lower()
        if keyType == "cd":
            key = cd_keygen()
            print(key)
        elif keyType == "oem":
            key = oem_keygen()
            print(key)
        else:
            print("Invalid choice.")
    else:
        uiPicker()
