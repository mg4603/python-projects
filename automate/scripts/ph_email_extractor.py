"""
1) Copy from clipboard
2) Extract emails and phone numbers
3) Copy to keyboard

1) Use pyperclip to copy selection from clipboard
2) Create regexen to extract emails and phone numbers
3) Format the extracted emails and phone numbers
4) Copy back to the clipboard
5) Display a message if nothing was found
"""

from pyperclip import copy, paste

if __name__ == "__main__":
    text = paste()
    extracted_data = extractor(text)
    copy(extracted_data)

