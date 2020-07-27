#usr/bin/python
# Author:   @BlankGodd_

import getpass
from platform import system
import os

class FileError(Exception):
	pass

def add_for_windows(user,script_file):
    bat = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % user
    with open(bat+'\\'+"open.bat","w+") as bat_file:
        bat_file.write(r'python %s' % script_file)

if __name__ == "__main__":
    opsys = system()
    if opsys == "Windows":
        try:
            user = getpass.getuser()
            script_file = input("Enter file path: ")
            add_for_windows(user,script_file)
            print("File added")
        except:
            raise FileError("Could not add file to autorun!")
    if opsys == "Linux":
        pass

        
