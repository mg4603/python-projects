from sys import exit
try:
    import pyttsx3
except ImportError:
    print('This program requires the pyttsx3 module to run.')
    print('Use: python3 -m pip install pyttsx3 to install')
    exit()

def display_intro():
    print('Text To Speech Talker')
    print()
    print('Text-to-speech using the pyttsx3 module, which in turn uses')
    print('the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows),')
    print('or eSpeak (on Linux) speech engines.')
    print()

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