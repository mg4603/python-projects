#!/usr/bin/env python3
"""
mclip.py - A multi-clipboard program
"""

TEXT = {"agree" : """Yes, I agree. That sounds fine to me.""",
        "busy"  : """Sorry, can we do this later this week or next week?""",
        "upsell": """Would you consider making this a monthly donation?"""
        }
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("key-phrase", help="copy-phrase's key")
    return parser.parse_args()

