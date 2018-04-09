# Commands class and objects.
import lib.commands_func as c

# Class for commands. Will eventually include possible time/role limitations.
class Commands:
    
    def __init__(self, func, cooldown):
        self.func = func     

hostname_obj = Commands(c.hostname_func, 30)