import subprocess
# General functions.

# PoC function that returns hostname. Currently works like "!hostname user ip/host"
def hostname_func(args):
    system_output = subprocess.run(["ssh", args[0]+"@"+args[1], "'hostname'"], stdout=subprocess.PIPE, universal_newlines=True)
    system_output = system_output.stdout.splitlines()
    return system_output[0]

# Command for parsing incoming messages.
def parse_command(incoming_message):
    incoming_message = incoming_message.split()
    command = incoming_message[0]
    args = incoming_message[1:]
    if command in commands:
        func = commands[command]["func"]
        outgoing_message = func(args)
        return outgoing_message
    else:
        return None
    
# Need to do this another way.
commands = {
    "!hostname": {
        "func": hostname_func
        }
    }