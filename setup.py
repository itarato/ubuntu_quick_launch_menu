"""
Verifies the environment for the app and sets up default config file.
"""

import imp
import os


def check_dependencies(err):
    """
    Verify dependencies.
    """
    for module in ['yaml', 'gi']:
        try:
            imp.find_module(module)
        except ImportError:
            err[0] += 1
            print "- Error: module '" + module + "' cannot be found. Try:"
            print "python -m pip install " + module


def setup_basic_config_file():
    """
    Initialize example config file.
    """
    file_path = os.path.expanduser('~/.qlm.yml')
    if not os.path.exists(file_path):
        with open(file_path, 'a+') as cfg_file:
            sample = open(os.path.dirname(__file__) + '/extras/sample.qml.yml').read()
            cfg_file.write(sample)
        print "- Example config file has been added to " + file_path
    else:
        print "- Config file is already in place at " + file_path


def main():
    """
    Main entry point.
    """
    print "- Setup Unity Quick Launch Menu"
    err = [0]
    check_dependencies(err)
    setup_basic_config_file()

    if err[0] > 0:
        print "- Setup cannot be completed due to issues. Please, fix them."
        exit(1)
    else:
        print "- All good. To start run:"
        print "python quick_launch_menu.py"


if __name__ == '__main__':
    main()
