import subprocess
from logger import Logger

class Postlink(object):
    def execute(self, options, data, pkgManager):
        if not options['update']:
            for script in data['prelink']:
                Logger.logPipe(subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
