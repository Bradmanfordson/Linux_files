#!/usr/bin/python3

import os

def header(message: str):
    print()
    print("#" * (4+ len(message)))
    print("# {} #".format(message))
    print("#" * (4 + len(message)))

def system_update():
    header("Updating")
    os.system("sudo apt update")

    header("Upgrading")
    os.system("sudo apt full-upgrade -y")

    header("Autocleaning")
    os.system("sudo apt autoclean -y")

    header("Autoremoving")
    os.system("sudo apt autoremove -y")


if __name__ in '__main__':
    system_update()