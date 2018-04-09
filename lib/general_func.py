# General functions.
import lib.commands_obj as c

# Command for parsing incoming messages.
def parse_command(incoming_message):
    # Split incoming, divide into command and arguments.
    incoming_message = incoming_message.split()
    command = incoming_message[0]
    args = incoming_message[1:]
    
    # See if user input is a command object, if so execute the function.
    obj = get_obj(command)
    if obj is not None:
        outgoing_message = obj.func(args)
        return outgoing_message
    else:
        return None
    
# Try to fetch object with user input. If it succeeds user input is a proper command.
def get_obj(command):
    command = command [1:]
    obj = command + "_obj"
    try:
        obj = getattr(c, obj)
        return obj
    except:
        return None