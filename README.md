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
The recommended way to install this is by cloning the git repository
```bash
git clone https://github.com/JasonGrace2282/settings-gui.git ~/settings-gui`
```
If you would like to remove the ``.git`` folder,
```bash
rm -rf ~/settings-gui/.git
```
You can then edit the configuration file at ``~/.config/simple-settings-gui/settings_map.json``

## Configuration Options

