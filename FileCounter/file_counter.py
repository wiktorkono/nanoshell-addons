import os, threading

## TODO - Add option to save file count to a file (give the user ability to input any path - no gui!)
## TODO - Add option to compare two saves (show +/- file count)

## ! This addon is work in progress, items on the TODO list will be added soon
## ! PLEASE DO NOT MODIFY THIS FILE, I WILL ADD THE FEATURES ABOVE.

global dirs
global threads
global total_files
global lock

dirs = []

# check if drive exists
def driveExists(drive_letter):
    return os.path.exists(drive_letter + ":\\") and os.path.isdir(drive_letter + ":\\")

# check each drive letter to see if it exists
def get_drive_list():
    global drivesExist
    driveletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    drivesExist = []
    for i in driveletters:
        check = driveExists(i)
        if check == True:
            drivesExist.append(i)

# make a list with the drives that exist on the system
def makeDriveList():
    for drive in drivesExist:
        i = drive + ":\\"
        dirs.append(i)
        

total_files = 0

lock = threading.Lock()

# count files in directory
def count_files(dir):
    global total_files
    print(f"Scanning: {dir}")
    try:
        for entry in os.scandir(dir):
            if entry.is_file():
                with lock: 
                    total_files += 1
            elif entry.is_dir():
                count_files(entry.path)
    except PermissionError:
        print(f"Access denied: {dir}")

#TODO still working on improving this maybe, currently coded just so it works
def results():
    os.system("cls")
    print(f"There are {total_files} files on your system.")
    input("\nPress [ENTER] to exit...")
    os.system("cls")

threads = []

# make a thread for each drive on the system (to count faster), should have no effect if you have one drive on the system
def count():
    for dir in dirs:
        thread = threading.Thread(target=count_files, args=(dir,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results()

# main function
def countConfirmation(prompt):
    os.system("cls")
    print("Counting the amount of files on your system can take some time, depending on the system speed and file count.\n\nDo you want to proceed?")
    confirmationPrompt = input("Y/n > ")
    confirmationPrompt = confirmationPrompt.lower()
    if confirmationPrompt == "": # ? I did not check if each of the checks work, they should though
        FileCounter()
    elif confirmationPrompt == "y":
        FileCounter()
    elif confirmationPrompt == "n":
        os.system("cls")
        exit()
    else:
        os.system("cls")
        print("Invalid option.")

# continue the script in the right order
def FileCounter():
    get_drive_list()
    makeDriveList()
    count()