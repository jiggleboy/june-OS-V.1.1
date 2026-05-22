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
            usn = susn
            usp = susp
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
        print("jokecommands: prints all joke commands | help: prints all commands | whoami: prints the current user | about: prints the information 'bout the OS | File commands, and subprocesses: newfile, ploadfile (prints and loads files), removefile, ls, and runpy (runs python code) | ")
        time.sleep(2)
    elif userComTerminal == "htf":
        with open("happytreefriends.pkl", "rb") as file:
            msg = pickle.load(file)
        print(msg)
    elif userComTerminal == "whoami":
        print(f"The logged in user is {usn}.")
    elif userComTerminal == "about":
        print("JuneOS is an independent project made by Bryan Silva. The project right now is in earlydev, so don't expect much from this simple 'operating system'.")
    elif userComTerminal == "i'llmissyougoodbye":
        pass
        print("It's come a long way since September---we've got new friends, we've started an eocosystem of kindness! But, this is one change that we're simply not ready for. Thank you for your service' it's been a great time! Goood luuuck!")
    elif userComTerminal == "jokecommands":
        pass
        print("htf: happy tree friends meme")
    elif userComTerminal == "syscheck":
        print(f"BIOS: {BIOS} | ACC: {usn} | CURS: {floppy.ldFromFloppy(0)}")
    elif userComTerminal == "newfile":
        contents = str(input("Contents: "))
        filename = str(input("Filename: "))
        with open(f"{filename}.txt", "wb") as file:
            pickle.dump((contents), file)
    elif userComTerminal == "ploadfile":
        filename2 = str(input("Enter filename: "))
        with open(f"{filename2}.txt", "rb") as file:
            sfile = pickle.load(file)
            print(sfile)
    elif userComTerminal == "deletefile":
        filename3 = str(input("Enter filename to delete: "))
        full_filename = f"{filename3}.txt"
        if os.path.exists(full_filename):
            os.remove(full_filename)
            print(f"Success: {full_filename} was wiped from the drive.")
        else:
            print(f"Error: {full_filename} does not exist.")
    elif userComTerminal == "ls":
        print("--- Files ---")
        for file in os.listdir("."):
            if file.endswith((".txt", ".pkl", ".py")):
                print(file)
    elif userComTerminal == "runpy":
        filename = input("Enter Python file to run (without .py): ").strip()
        full_path = f"{filename}.py"

        if os.path.exists(full_path):
        # This tells the host computer to run 'python filename.py'
            os.system(f"python {full_path}")
        else:
            print("Error: File not found.")












