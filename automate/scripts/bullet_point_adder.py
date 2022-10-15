#!/usr/bin/env python3
"""
bullet_point_adder will take the text from the clipboard, add a star and space in
front of each line and paste it back to the clipboard
"""

from pyperclip import copy, paste

def bullet_point_adder(text):
    lines = text.split("\n")
    lines = list(line for line in lines if line)
    result = ""
    for line in lines:
        result += "* %s\n" % line
    return result

if __name__ == "__main__":
    text = paste()
    text = bullet_point_adder(text)
    copy(text)