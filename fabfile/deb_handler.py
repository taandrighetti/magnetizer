from fabric.api import sudo


def apt_install(package):
    """ Helper method to install deb packages through apt-get. """
    cmd = 'apt-get install --asume-yes %s' % package
    sudo(cmd)
