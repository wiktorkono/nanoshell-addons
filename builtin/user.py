import socket, getpass
from bin.coloramasetup import *

def showUser(prompt):
    run_user = getpass.getuser()
    host_name = socket.gethostname()

    print(f"Running as {c.LIGHTCYAN_EX}{run_user}{r} on {c.LIGHTBLUE_EX}{host_name}{r}")