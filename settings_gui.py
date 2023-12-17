import argparse
import customtkinter as ctk
import os
import json

_CONFIG_OPTIONS = {
    "settings": r"{}",
    "appearance": "dark",
    "font": None
}
"""Dictionary of available config options to their defaults"""

class Settings(ctk.CTk):
    def __init__(self, settings: dict[str, str], appearance: str, font: str | None):
        ctk.set_appearance_mode(appearance)
        super().__init__()
        super(self, Settings).title("Simple Settings GUI")
        self.geometry("400x400")
        self.settings = settings
        self.construct_settings(font)
        
    def construct_settings(self, font: str | None):
        for name, cmd in self.settings.items():
            ctk.CTkButton(
                self,
                text=name,
                command=lambda cmd=cmd: os.system(cmd),
                font=font
            ).pack()
        
def parse_json(path) -> dict:
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(r"{}")
    with open(path) as f:
        data = json.load(f)
    
    if not isinstance(data, dict):
        raise ValueError("Configuration data must be a dictionary! See the README for more detail.")
    
    for x in data:
        if x not in _CONFIG_OPTIONS:
            raise ValueError(f"Unrecognized Option {x}!")
    for name, default in _CONFIG_OPTIONS.items():
        if name not in data:
            data[name] = default
    
    return data
    

def main():
    parser = argparse.ArgumentParser(
        prog="Simple Settings GUI",
        description="Keep the launching command of GUIs together!",
        epilog="Made with <3"
    )
    parser.add_argument(
        "config_path",
        default="~/settings_map.json",
        help="File to read for configuration options. Defaults to ~/settings_map.json"
    )
    args = parser.parse_args()
    Settings(**parse_json(args.config_path)).mainloop()
    

if __name__ == "__main__":
    main()
