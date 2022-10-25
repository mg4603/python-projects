"""1. Ask the user if they'd like to know how to keep an idiot busy for hours.
2. If the user answers no, quit.
3. If the user answers yes, go to Step 1."""

from pyinputplus import inputYesNo

def keep_idiot_busy():
    while True:
        response = inputYesNo('Want to know how to keep an idiot busy for hours?')
        if response == 'no':
            print('Thank you. Have a nice day.')
            break

if __name__ == '__main__':
    keep_idiot_busy()
