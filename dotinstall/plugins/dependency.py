class Dependency(object):
    def execute(self, options, data, pkg_manager):  # pragma: no cover
        if not options['update']:
            for dependency in data['dependencies']:
                pkg_manager.install(dependency)
