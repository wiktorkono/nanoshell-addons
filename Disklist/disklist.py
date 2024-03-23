import os
from colorama import Fore as c
from colorama import Back as bg
from colorama import Style as s
color_red = c.RED
color_reset = s.RESET_ALL

# get system platform
system_platform = os.name
if system_platform != "nt":
    print(f"{color_red}ERROR{color_reset} - addon 'Disklist' (/addons/Disklist) {color_red}can not run on platform '{system_platform}'{color_reset}. Please remove it from your nanoshell installation.")
    exit()

import win32api, win32file, shutil
from tabulate import tabulate

def driveExists(drive_letter):
    return os.path.exists(drive_letter + ":\\") and os.path.isdir(drive_letter + ":\\")

def list_drives(prompt):
    print("\n")
    driveletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    drivesExist = []
    for i in driveletters:
        check = driveExists(i)
        if check == True:
            drivesExist.append(i)
            
    headers = ["Drive Letter", "Drive Type", "Volume Name", "Total Space", "Used Space", "Free Space", "File System"]
    rows = []
    
    for driveLetter in drivesExist:
        drive_info = win32api.GetVolumeInformation(driveLetter + ":\\")
        volume_name = drive_info[0] if drive_info[0] else "(none)"
        drive_type = win32file.GetDriveType(driveLetter + ":\\")
        drive_format = drive_info[4]
        total, used, free = shutil.disk_usage(driveLetter + ":\\")
        total_gb = total // (2**30)
        used_gb = used // (2**30)
        free_gb = free // (2**30)
        
        drive_type_name = {
            win32file.DRIVE_FIXED: "Fixed",
            win32file.DRIVE_REMOVABLE: "Removable",
            win32file.DRIVE_CDROM: "CD-ROM",
            win32file.DRIVE_REMOTE: "Remote",
            win32file.DRIVE_RAMDISK: "RAM Disk"
        }.get(drive_type, "Unknown")
        
        row = [driveLetter.upper() + ":", drive_type_name, volume_name, str(total_gb) + " GB", str(used_gb) + " GB", str(free_gb) + " GB", drive_format]
        rows.append(row)
    
    print(tabulate(rows, headers=headers))
    print("\n")