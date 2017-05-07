from logger import *


class Installer(object):
    def install(self, dependency):
        if self._isInstalled(dependency):
            Logger.info("'{}' is already installed.\n".format(dependency))
        elif self._install(dependency):
            Logger.success("'{}' has been successfully installed.\n".format(dependency))
        else:
            Logger.error("'{}' could not be installed.\n".format(dependency))

    def _isInstalled(self, dependency):
        raise NotImplementedError

    def _install(self, dependency):
        raise NotImplementedError
