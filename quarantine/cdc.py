"""Center for Disease Control"""
import os
import sys
import re
import os.path as path
import shutil
from sh import virtualenv, Command
from pycolorterm.pycolorterm import print_pretty


ENV_BOX = path.expanduser("~/.quarantine/envs")
ENV_BIN = path.expanduser("~/.quarantine/bin")
NAME_REGEX = re.compile(r'([a-zA-Z\-_]+)[=<>\!~]?')


class CDC(object):
    """This object handles creating and managing app-specific
    virtual environments.

    """

    def __init__(self, name):
        if not path.isdir(ENV_BOX):
            os.makedirs(ENV_BOX)
        if not path.isdir(ENV_BIN):
            os.makedirs(ENV_BIN)
        self.name = self.package_name(name)
        self.raw_name = name
        self.env = path.join(ENV_BOX, name)
        self.env_bin = path.join(self.env, 'quarantine-bin')

    def list_exes(self):
        """List the installed executables by this project."""
        return [path.join(self.env_bin, f)
                for f
                in os.listdir(self.env_bin)]

    def create_env(self):
        """Create a virtual environment."""
        virtualenv(self.env, _err=sys.stderr)
        os.mkdir(self.env_bin)

    def package_name(self, name):
        """Extracts the name from a potentially version qualified string."""
        return NAME_REGEX.search(name).group(1)

    def install_program(self, extra_args):
        """Install the app to the virtualenv"""
        pip = Command(path.join(self.env, 'bin', 'pip'))
        args = ['install', self.raw_name,
                '--install-option', '--install-scripts={}'
                .format(self.env_bin)] + list(extra_args)
        print_pretty("<BOLD>pip {}<END>\n".format(' '.join(args)))
        pip(args, _out=sys.stdout, _err=sys.stderr)
        print('')

    def create_links(self):
        """Create links to installed scripts in the virtualenv's
        bin directory to our bin directory.

        """
        for link in self.list_exes():
            print_pretty("<FG_BLUE>Creating link for {}...<END>".format(link))
            os.symlink(link, path.join(ENV_BIN, path.basename(link)))

    def remove_links(self):
        """Remove links from our bin."""
        for link in self.list_exes():
            link = path.join(ENV_BIN, path.basename(link))
            print_pretty("<FG_BLUE>Removing link {}...<END>".format(link))
            os.remove(link)
            
    def uninstall(self):
        """Uninstall the environment and links."""
        if path.isdir(self.env_bin):
            self.remove_links()
        if path.isdir(self.env):
            print_pretty("<FG_BLUE>Removing env {}...<END>".format(self.env))
            shutil.rmtree(self.env)

    def install(self, pip_args=None):
        """Install the program and put links in place."""
        if path.isdir(self.env):
            print("<FG_RED>This seems to already be installed.<END>")
        else:
            print_pretty("<FG_BLUE>Creating environment {}...<END>\n".format(self.env))
            self.create_env()
            self.install_program(pip_args)
            self.create_links()
