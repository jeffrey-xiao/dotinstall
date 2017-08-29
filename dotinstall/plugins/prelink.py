import subprocess

from dotinstall.util.logger import Logger


class Prelink(object):

    def execute(self, options, data, pkg_manager):
        if not options['update']:
            for script in data['prelink']:
                Logger.info('prelink: ' + script + '\n')
                subprocess.call(script, shell=True)
