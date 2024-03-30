import socket, getpass
from bin.coloramasetup import *

def showUser(prompt):
    run_user = getpass.getuser()
    host_name = socket.gethostname()

    print(f"Running as {a}{run_user}{r} on {a}{bright}{host_name}{r}")
