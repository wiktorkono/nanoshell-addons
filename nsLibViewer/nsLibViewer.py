import sys
from bin.coloramasetup import a as accentColor, r as resetColor, red as errorColor

def nsLibViewer(prompt):
    try:
        if not prompt.startswith("nslib "):
            print(f"{errorColor}Error:{resetColor} Missing argument. Use 'nslib <variable_name1> [variable_name2] ...'")
            return

        variable_names = prompt.split(" ")[1:]

        if not variable_names:
            print(f"{errorColor}Missing argument:{resetColor} no variable specified")
            return

        nanoshell_lib = sys.modules.get('bin.nanoshell_lib')

        if not nanoshell_lib:
            print(f"{errorColor}Error:{resetColor} bin.nanoshell_lib module not found")
            return

        for requestedVariable in variable_names:
            if hasattr(nanoshell_lib, requestedVariable):
                variable_value = getattr(nanoshell_lib, requestedVariable)
                print(f"{accentColor}{requestedVariable}{resetColor} = {variable_value}")
            else:
                print(f"{errorColor}Error:{resetColor} variable {errorColor}'{requestedVariable}'{resetColor} not found in bin.nanoshell_lib")

    except IndexError:
        print(f"{errorColor}Missing argument:{resetColor} no variable specified")
