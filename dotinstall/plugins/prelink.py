import subprocess
from logger import Logger

class Prelink(object):
    def execute(self, options, data, pkgManager):
        if not options['update']:
            for script in data['prelink']:
                Logger.info("prelink: " + script + "\n")
                subprocess.call(script, shell=True)
