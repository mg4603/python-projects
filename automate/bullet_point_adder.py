#!/usr/bin/env python3
"""
bullet_point_adder will take the text from the clipboard, add a star and space in
front of each line and paste it back to the clipboard
"""

from pyperclip import copy, paste


if __name__ == "__main__":
    text = paste()
    bullet_point_adder(text)
    copy(text)