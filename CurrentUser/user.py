import socket, getpass

def showUser(prompt):
    run_user = getpass.getuser()
    host_name = socket.gethostname()

    print("Running as {0} on {1}".format(run_user, host_name))