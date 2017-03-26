"""
Quick Launch Menu
"""

import signal
import os
from subprocess import call
from yaml import load as yaml_load

from gi import require_version as gi_require_version
gi_require_version('Gtk', '3.0')
gi_require_version('AppIndicator3', '0.1')
gi_require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


class AppConfig(object):
    """
    App configuration.
    """

    def __init__(self, config_file_path):
        """
        Ctor.
        """
        try:
            raw = open(config_file_path).read()
        except IOError:
            print """Error - configuration file cannot find. Make sure you 
                     called setup.py and you have ~/.qlm.yml file."""
            exit(1)
        cfg = yaml_load(raw)

        self.menu_raw = cfg['menu_items']


def gen_on_select_callback(name, command):
    """
    Generates a callback for menu items created from config.
    """
    return lambda _: execute_command(name, command)


def execute_command(name, command):
    """
    Execute the menu command and notify the user about the completion.
    """
    ret_code = call(command)
    message = 'Command has been completed with code: ' + str(ret_code)
    notify.Notification.new(name, message, None).show()


def attach_config_to_menu(menu_raw, menu):
    """
    Attach the config elements to the main menu.
    """
    for name in menu_raw.keys():
        if name.find('_') >= 0:
            menu_item = gtk.MenuItem.new_with_mnemonic(name)
        else:
            menu_item = gtk.MenuItem(name)

        if menu_raw[name].has_key('command'):
            on_fn = gen_on_select_callback(name.replace('_', ''), menu_raw[name]['command'])
            menu_item.connect('activate', on_fn)

        if menu_raw[name].has_key('menu_items'):
            submenu = gtk.Menu()
            attach_config_to_menu(menu_raw[name]['menu_items'], submenu)
            menu_item.set_submenu(submenu)

        menu.append(menu_item)


def build_menu(cfg):
    """
    Create app menu.
    """
    menu = gtk.Menu()

    attach_config_to_menu(cfg.menu_raw, menu)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', on_quit)

    menu.append(item_quit)
    menu.show_all()

    return menu


def on_quit(_):
    """
    Quit menu item action.
    """
    notify.uninit()
    gtk.main_quit()


def main():
    """
    Main entry point.
    """
    app_id = 'quick_launch_menu'
    cfg = AppConfig(os.path.expanduser('~/.qlm.yml'))

    notify.init(app_id)

    indicator = appindicator.Indicator.new(
        app_id, 'qlm', appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_icon_theme_path(os.path.abspath('./icons'))
    indicator.set_menu(build_menu(cfg))

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    gtk.main()


if __name__ == '__main__':
    main()
