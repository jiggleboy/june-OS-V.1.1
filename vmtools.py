# The tinkervmtools package is used for
# help building a VM, not getting a pre-built one. V.1.0

ram = []
flpy = []
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
class floppy:
    def __init__(self):
        pass
    def storeIntoFloppy(data):
        flpy.append(data)
    def popFromFloppy(data):
        return flpy.pop()
    def ldFromFloppy(index):
        return flpy[index]
