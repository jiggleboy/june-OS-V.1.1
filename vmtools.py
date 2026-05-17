# The tinkervmtools package is used for
# help building a VM, not getting a pre-built one. V.1.0

# floppymemtools is used to manage your virtual floppy
# and emulate one, before you run the OS, just make sure
# to pre-load data on to it.

ram = []
floppy = []
class tinkervmtools:
    def __init__(self):
        pass
    def stor(value):
        ram.append(value)
    def pop():
        return ram.pop()
    def ld(index: int):
        return ram[index]
    def clr():
        print("\033[2J\033[H")
class floppymemtools:
    def __init__(self):
        pass
    def writeToFloppy(data):
        floppy.append(data)
    def loadFromFloppy(index):
        return floppy[index]
    def popFloppy():
        return floppy.pop()
    def peekFromFloppy():
        return floppy.peek()
