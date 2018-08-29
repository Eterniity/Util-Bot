# Functions that are tied to chat commands.
import subprocess

# PoC function that returns hostname. Currently works like "!hostname user ip/host"
def hostname_func(args):
    system_output = subprocess.run(["ssh", args[0]+"@"+args[1], "'hostname'"], stdout=subprocess.PIPE, universal_newlines=True)
    system_output = system_output.stdout.splitlines()
    message = "Hostname is " + system_output[0]
    return message