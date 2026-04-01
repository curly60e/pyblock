"""
Data-driven menu system for PyBLOCK.

Replaces 80+ duplicate menu functions with a composable Menu class.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional


COLOR_MAP = {
    "A": "black", "B": "red", "C": "green", "D": "yellow",
    "E": "blue", "F": "magenta", "G": "cyan", "H": "white", "I": "gray",
}

COLOR_DISPLAY = """
    \033[1;30;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;32;40mC.\033[0;37;40m Green
    \033[1;33;40mD.\033[0;37;40m Yellow
    \033[1;34;40mE.\033[0;37;40m Blue
    \033[1;35;40mF.\033[0;37;40m Magenta
    \033[1;36;40mG.\033[0;37;40m Cyan
    \033[1;37;40mH.\033[0;37;40m White
    \033[0;37;40mI.\033[0;37;40m Gray
    \033[1;31;40mR.\033[0;37;40m <<< Back
"""


@dataclass
class MenuItem:
    key: str
    label: str
    action: Callable
    color: str = "\033[0;37;40m"
    modes: tuple = ("local", "remote", "onchain_only")


@dataclass
class Menu:
    title: str
    items: list = field(default_factory=list)
    header_fn: Optional[Callable] = None
    show_sysinfo: bool = True

    def display(self, mode="local", clear_fn=None, logo_fn=None, sysinfo_fn=None):
        if clear_fn:
            clear_fn()
        if logo_fn:
            logo_fn()
        if self.show_sysinfo and sysinfo_fn:
            sysinfo_fn()

        if self.header_fn:
            self.header_fn()

        visible = [i for i in self.items if mode in i.modes]
        for item in visible:
            print(f"    {item.color}{item.key}.\033[0;37;40m {item.label}")
        print("\n\n\x1b[?25h")

    def run(self, mode="local", clear_fn=None, logo_fn=None, sysinfo_fn=None):
        self.display(mode, clear_fn, logo_fn, sysinfo_fn)
        choice = input("\033[1;32;40mSelect option: \033[0;37;40m")
        visible = [i for i in self.items if mode in i.modes]
        for item in visible:
            if choice.lower() == item.key.lower():
                item.action()
                return True
        return False


def select_color(settings_dict, key, on_select_fn, back_fn):
    """Generic color selection that replaces ~20 duplicate color menu functions.

    Args:
        settings_dict: The settings dictionary to modify (settings or settingsClock)
        key: The key to set ("colorA" or "colorB")
        on_select_fn: Function to call after selecting a color (testlogo/testlogoRB)
        back_fn: Function to call when user presses R (back)
    """
    print(COLOR_DISPLAY)
    choice = input("\033[1;32;40mSelect color: \033[0;37;40m")
    upper = choice.upper()
    if upper == "R":
        back_fn()
        return
    if upper in COLOR_MAP:
        settings_dict[key] = COLOR_MAP[upper]
        on_select_fn()
