# Functions that are tied to chat commands.
import subprocess

# PoC function that returns hostname. Currently works like "!hostname user ip/host"
def hostname_func(args):
    try:
        system_output = subprocess.run(["ssh", args[0]+"@"+args[1], "'hostname'"], stdout=subprocess.PIPE, universal_newlines=True, check=True)
        system_output = system_output.stdout.splitlines()
        message = "Hostname is " + system_output[0]
        return message
    except subprocess.CalledProcessError as e:
        print (e)

def free_func(args):
    system_output = subprocess.run(["ssh", args[0]+"@"+args[1], "'free'"], stdout=subprocess.PIPE, universal_newlines=True, check=True)
    print (system_output)
    system_output = system_output.stdout.split()
    total = system_output[7]
    used = system_output[8]
    free = system_output[9]
    message = "Total = " + total + " Used = " + used + " Free = " + free
    return message