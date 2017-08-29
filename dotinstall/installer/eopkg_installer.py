import subprocess

from dotinstall.installer.installer import Installer


class EopkgInstaller(Installer):

    def installer_exists(self):
        return subprocess.call(
            ['which', 'eopkg'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _is_installed(self, dependency):
        eopkg_pipe = subprocess.Popen(
            ['eopkg', 'li', '-i'],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )

        grep_pipe = subprocess.Popen(
            ['grep', '-e', r'\b{}\b'.format(dependency)],
            stdin=eopkg_pipe.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )

        grep_pipe.communicate()

        return grep_pipe.returncode == 0

    def _install(self, dependency):
        return subprocess.call(
            ['sudo', 'eopkg', 'it', '-y', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        ) == 0
