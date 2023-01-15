from sys import exit
try:
    import pyttsx3
except ImportError:
    print('This program requires the pyttsx3 module to run.')
    print('Use: python3 -m pip install pyttsx3 to install')
    exit()


def main():
    engine = pyttsx3.init()
    display_intro()
    while True:
        print('Enter text to speak, or QUIT to quit.')
        text = input('> ').upper()

        if text == 'QUIT':
            exit()

        engine.say(text)
        engine.runAndWait()