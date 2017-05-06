class Installer(object):
    def __init__(self, logger):
        self.logger = logger

    def install(self, dependency):
        if self._isInstalled(dependency):
            self.logger.info("'{}' is already installed.\n".format(dependency))
        elif self._install(dependency):
            self.logger.success("'{}' has been successfully installed.\n".format(dependency))
        else:
            self.logger.error("'{}' could not be installed.\n".format(dependency))

    def _isInstalled (self, dependency):
        raise NotImplementedError

    def _install (self, dependency):
        raise NotImplementedError
