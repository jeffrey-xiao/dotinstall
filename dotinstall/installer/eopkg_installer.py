import subprocess


from dotinstall.installer.installer import Installer


class EopkgInstaller(Installer):

    def _is_installed(self, dependency):  # pragma: no cover
        eopkg_pipe = subprocess.Popen(
            ["eopkg", "li", "-i"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )

        grep_pipe = subprocess.Popen(
            ["grep", dependency],
            stdin=eopkg_pipe.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )

        grep_pipe.communicate()

        return grep_pipe.returncode == 0
    
    def _install(self, dependency):  # pragma: no cover
        return subprocess.call(
            ["sudo", "eopkg", "it", "-y", dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0
