import customtkinter as ctk
import os
import json
from pathlib import Path

PKGNAME = "Simple Settings GUI"

_CONFIG_OPTIONS = {
    "settings": {},
    "appearance": "dark",
    "font": None
}
"""Dictionary of available config options to their defaults"""

CONFIG_PATH = Path(f"~/.config/{PKGNAME.lower().replace(' ', '-')}/settings_map.json")
"""Location of the config file."""

DEFAULT_CONFIG_INFO = str(_CONFIG_OPTIONS["settings"])
"""Default data in config file"""

class Settings(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTk, settings: dict[str, str], appearance: str, font: str | None, **kwargs):
        ctk.set_appearance_mode(appearance)
        super().__init__(master=master, **kwargs)
        self.settings = settings
        
        title = ctk.CTkLabel(self, text=PKGNAME, font=(font, 30))
        header1 = ctk.CTkLabel(self, text="Execute", font=font)
        header2 = ctk.CTkLabel(self, text="Command", font=font)
        
        self.construct_settings(font, row=2)
        title.grid(row=0, column=1, columnspan=2, pady=10)
        header1.grid(row=1, column=1, pady=10)
        header2.grid(row=1, column=2, pady=10)
        
    def construct_settings(self, font: str | None, row: int):
        gridkw = {
            "pady": 10,
            "padx": 20
        }
        for name, cmd in self.settings.items():
            ctk.CTkButton(
                self,
                text=name,
                command=lambda cmd=cmd: os.system(cmd),
                font=font
            ).grid(row=row, column=1, **gridkw)
            ctk.CTkLabel(self, text=cmd).grid(row=row, column=2, **gridkw)
            row+=1
       
def handle_resize(settings: Settings, root: ctk.CTk):
    settings.configure(width=root.winfo_width(), height=root.winfo_height())
        
def parse_json(path: Path) -> dict:
    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        
        with path.open("w") as f:
            f.write(DEFAULT_CONFIG_INFO)
            
    with path.open() as f:
        data = json.load(f)
    
    if not isinstance(data, dict):
        raise ValueError("Configuration data must be a dictionary! See the README for more detail.")
    
    for x in data:
        if x not in _CONFIG_OPTIONS:
            raise ValueError(f"Unrecognized Option {x}!")
    
    for name, default in _CONFIG_OPTIONS.items():
        if name not in data:
            data[name] = default
    print(data)
    return data

def main():
    root = ctk.CTk()
    root.title(PKGNAME)
    root.geometry("400x400")
    root.resizable(True, True)
    settings = Settings(
        root,
        **parse_json(CONFIG_PATH)
    )
    canvas = settings.master
    canvas.bind("<Configure>", lambda _: handle_resize(settings, root))
    settings.pack()
    root.mainloop()
    

if __name__ == "__main__":
    main()
