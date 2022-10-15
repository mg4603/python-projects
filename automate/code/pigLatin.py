#!/usr/bin/env python3
"""
Program to convert english text to pig latin
"""

def convert(message):
    VOWELS = ('a', 'e', 'i', 'o', 'u')

    pigLatin = []
    for word in message.split(" "):
        prefixNonLetters = ""

        # separate non letters at start of word
        while(len(word) > 0 and not word[0].isalpha()):
            prefixNonLetters += word[0]
            word = word[1:]

        if(len(word) == 0):
            pigLatin.append(prefixNonLetters)
            continue
        
        suffixNonLetters = ""

        # separate non letters at end of word
        while(not word[-1].isalpha()):
            suffixNonLetters += word[-1]
            word = word[:-1]

        wasUpper = word.isupper() # check upper case
        wasTitle = word.istitle() # check title case

        word = word.lower()

        prefixConsonants = ""

        while(len(word) > 0 and word[0] not in VOWELS):
            prefixConsonants += word[0]
            word = word[1:]

        if(prefixConsonants != ""):
            word += prefixConsonants
            word += "ay"
        else:
            word += "yay"

        if(wasUpper):
            word = word.upper()
        elif(wasTitle):
            word = word.title()
        
        pigLatin.append("%s%s%s" %(prefixNonLetters, word, suffixNonLetters))

    return " ".join(pigLatin)

if __name__ == "__main__":
    message = input("Enter the english message to translate to pig latin:\n")
    print(convert(message))