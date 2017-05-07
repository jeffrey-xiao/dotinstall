class Dependency(object):
    def execute(self, options, data, pkgManager):
        if not options['update']:
            for dependency in data['dependencies']:
                pkgManager.install(dependency)
