import subprocess

def getOutput (cmd):
    ret = ""
    try:
	ret = subprocess.check_output(cmd.split())
    except subprocess.CalledProcessError as e:
	pass
    return ret
class Format(object):
    BOLD = getOutput("tput bold")
    RESET = getOutput("tput sgr0")

    BLUE = getOutput("tput setaf 4")
    GREEN = getOutput("tput setaf 2")
    YELLOW = getOutput("tput setaf 3")
    RED = getOutput("tput setaf 1")
