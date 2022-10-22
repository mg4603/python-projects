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
from re import VERBOSE, compile

def ph_number_extractor(text):
    phone_number_regex = compile(
        r'''
        (\d{2,3})?        # region code
        [-\ ]?              # separator
        (\d{4})             # first five digits
        [-\ ]?              # separator
        (\d{4})
        ''',
        VERBOSE
    )
    phone_numbers = ['-'.join([group for group in phone_number_groups if group]) for phone_number_groups in phone_number_regex.findall(text)]
    return phone_numbers

def email_extractor(text):
    email_regex = compile(
        r'''
        ([a-zA-Z0-9._%+-]+)       # username
        (@)                       # @ symbol
        ([a-zA-Z0-9-]+)          # domain name
        (\.[a-zA-Z]{2,4})      # dot something
        #(\.[a-zA-Z]{2, 4})?     # tld
        ''',
        VERBOSE
    )
    emails = [''.join(email) for email in  email_regex.findall(text)]
    return emails

def extractor(text):
     

    phone_numbers = ph_number_extractor(text)
    emails = email_extractor(text)
    
    return 'Phone Numbers: \n\t{}\nEmails: \n\t{}'.format(
        '\n\t'.join(phone_numbers),
        '\n\t'.join(emails)
    )

if __name__ == "__main__":
    text = paste()
    extracted_data = extractor(text)
    copy(extracted_data)

