Unity Quick Launch Menu
=======================

The customizable quick launch menu you always wanted - for Ubuntu (using GTK3).


![Screenshot](./extras/screenshot.png)


# Dependencies

- Python 2.x
- Yaml python package
- GTK3


# Configuration format

Use `_` (underscore) to mark shortkeys.

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
