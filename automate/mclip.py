#!/usr/bin/env python3
"""
mclip.py - A multi-clipboard program
"""
from argparse import ArgumentParser
from sys import exit
from pyperclip import copy

TEXT = {"agree" : """Yes, I agree. That sounds fine to me.""",
        "busy"  : """Sorry, can we do this later this week or next week?""",
        "upsell": """Would you consider making this a monthly donation?"""
        }

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("key", help="copy-phrase's key")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    key_phrase = args.key

    if(key_phrase in TEXT):
        copy(TEXT[key_phrase])
        print("Text for %s copied to clipboard" % key_phrase)
    else:
        print("There is no text for %s" % key_phrase)

