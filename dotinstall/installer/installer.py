import subprocess


from dotinstall.util.logger import Logger


class Installer(object):
    def install(self, dependency):  # pragma: no cover
        if self._is_installed(dependency):
            Logger.info("'{}' is already installed.\n".format(dependency))
        elif self._install(dependency):
            Logger.success("'{}' has been successfully installed.\n".format(dependency))
        else:
            Logger.error("'{}' could not be installed.\n".format(dependency))

    def _is_installed(self, dependency):
        raise NotImplementedError

    def _install(self, dependency):
        raise NotImplementedError
