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
        split_args = prompt.split(' ', 3)
        if len(split_args) >= 3:
            keyType = split_args[1]
            keyCount = split_args[2]
            keyType = keyType.lower()
            if keyType == "cd":
                for i in range(1, int(keyCount)):
                    key = cd_keygen()
                    print(key)
            elif keyType == "oem":
                for i in range(1, int(keyCount)):
                    key = oem_keygen()
                    print(key)
            else:
                print("Invalid choice.")
        if len(split_args) >= 2:
            keyType = split_args[1]
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
