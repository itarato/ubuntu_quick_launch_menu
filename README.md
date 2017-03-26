Unity Quick Launch Menu
=======================

The customizable quick launch menu you always wanted - for Ubuntu (using GTK3).

![Screenshot](./extras/screenshot.png)


# Dependencies

- Python 2.x
- Yaml python package
- GTK3


# Install

```bash
git clone git@github.com:itarato/ubuntu_quick_launch_menu.git
cd ubuntu_quick_launch_menu
python setup.py
```

# Configuration

Configuration sample is put in your home folder as `.qml.yml`. You can nest menus as deep as you want. Command for a menu item is optional - parent menus usually does not have commands.

Command is an array of arguments, use double quotes if you are not sure about escaping.

Use `_` (underscore) to mark hot-keys, eg.: "MySQL _Start" marks `s` as hot-key.

```yaml
menu_items:
  _Drush cache clear:
    command:
      - drush
      - "-r"
      - "/var/www"
      - cc
      - all
  Apache:
    menu_items:
      Stop:
        command:
          - service
          - apache2
          - stop
      Start:
        command:
          - service
          - apache2
          - start
```


# Run

```bash
python quick_launch_menu.py
```
