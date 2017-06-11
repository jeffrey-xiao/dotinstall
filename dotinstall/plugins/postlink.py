import subprocess


from dotinstall.util.logger import Logger


class Postlink(object):
    def execute(self, options, data, pkgManager):
        if not options['update']:
            for script in data['postlink']:
                Logger.info("postlink: " + script + "\n")
                subprocess.call(script, shell=True)
