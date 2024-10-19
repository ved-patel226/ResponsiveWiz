from termcolor import cprint

def print(string, color="green"):
    cprint(string, color, attrs=["bold"])