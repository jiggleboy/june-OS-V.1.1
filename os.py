# Import tinkervmtools and time ↓
from vmtools import tinkervmtools as tt
from vmtools import floppy
import pickle
import time
import sys
import os
mg = "when you traumatize your friend with happy tree friends [insert gif of pop doing the michael myers bounce here]"
with open("happytreefriends.pkl", "wb") as file:
    pickle.dump((mg), file)
# BIOS loaders ↓
BIOS = "0x55AA"
FBIOS = "0x55AA"
if BIOS == "0x55aa":
    print("Proceeding on to log-in.")
    time.sleep(3)
    tt.clr()
    time.sleep(3)
elif FBIOS == "0x55AA":
    print("Proceeding on to log-in.")
    time.sleep(3)
    tt.clr()
    time.sleep(3)
else:
    print("JuneOS access has been denied--this software is probably pirated. Check the code first, though. The boot-default to prevent copies is 0x0000. Change the BIOS code(s) to 0x55AA, unless you want this garbage.")
    sys.exit()
# signup
print("Now, would you like to sign in or log in?")
userinput = str(input("'Sign up' or 'Log in'? "))
if userinput == "Sign up" or userinput == "sign up":
    usn = str(input("Username: "))
    usp = str(input("Password: "))
    with open("usr.pkl", "wb") as file:
        pickle.dump((usn, usp), file)


# login
elif userinput == "log in":
    if os.path.exists("usr.pkl"):
        with open ("usr.pkl", "rb") as file:
            susn, susp = pickle.load(file)
        inpus = input("Saved username? ")
        inpup = input("Saved password? ")
        if inpus == susn and inpup == susp:
            with open("cursor.pkl", "rb") as file:
                cursorID = pickle.load(file)
        else:
            print("Error loading your save: either wrong password or user.")
            sys.exit()
    else:
        print("No saved account found.")
        sys.exit()
# prefrences (more soon)
time.sleep(3)
tt.clr()
time.sleep(3)
print(f"Welcome to JuneOS, {susn}!")
time.sleep(3)
tt.clr()
time.sleep(3)
print("But first, you'll need a unique cursor!\n")
time.sleep(3)
cursorID = str(input("Cursor: "))
# store cursor into a .pkl file and hardwrite into the floppy
floppy.storeIntoFloppy(cursorID)
with open("cursor.pkl", "wb") as file:
    pickle.dump((cursorID), file)
# begin the OS

terminalOn = True

while terminalOn:
    userComTerminal = str(input(f"{cursorID} "))
    if userComTerminal == "help":
        print("jokecommands: prints all joke commands | help: prints all commands | whoami: prints the current user | about: prints the information 'bout the OS | clr/cls: clears Terminal")
        time.sleep(2)
    elif userComTerminal == "htf":
        with open("happytreefriends.pkl", "rb") as file:
            msg = pickle.load(file)
        print(msg)
    elif userComTerminal == "whoami":
        print(f"The logged in user is {susn}.")
    elif userComTerminal == "about":
        print("JuneOS is an independent project made by Bryan Silva. The project right now is in earlydev, so don't expect much from this simple 'operating system'.")
    elif userComTerminal == "clr" or "cls":
        tt.clr()
    elif userComTerminal.startswith("echo "):
        message = userComTerminal[5:]
        print(message)
