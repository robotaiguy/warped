from typing import Dict

from pydantic import BaseModel

BASE16_FOLDER: str = "base16/"
STANDARD_FOLDER: str = "standard/"
THEME_TO_TEST: str = "afterglow.yaml"


class TerminalColorsSet(BaseModel):
    black: str
    blue: str
    cyan: str
    green: str
    magenta: str
    red: str
    white: str
    yellow: str


class TerminalColorsContainer(BaseModel):
    normal: TerminalColorsSet
    bright: TerminalColorsSet


class Theme(BaseModel):
    accent: str
    background: str
    foreground: str
    details: str
    terminal_colors: TerminalColorsContainer
