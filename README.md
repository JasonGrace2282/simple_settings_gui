# Settings-gui
A simple barebones gui to keep from having to remember the commands to launch an individual gui

## Dependencies
* python-tk
* python-customtkinter

For most distro's, you can just run ``python -m pip install customtkinter``.

If you're on Archlinux, you might need to do
```bash
pacman -S tk
paru -S customtkinter
```
## Installing the package

### Manually
```bash
git clone https://github.com/JasonGrace2282/settings-gui.git ~/settings-gui`
echo "alias settings='python ~/settings-gui/settings_gui.py ~/settings_map.json'" >> ~/.bashrc`
```

### Archlinux
WIP, do not use!
```bash
paru -S simple-settings-gui-git
```

## Configuration Options

