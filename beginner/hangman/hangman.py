from random import randint
import sys
sys.path.append('/path/to/helper.py')
import helper

f = open('/path/to/wordlist.txt' ,'r')
words = f.read().splitlines()
f.close()

while True:
    num = randint(1,len(words))
    word = words[num-1]
    counter = 8
    guess_state = ['_']*len(word)
    while counter > 0:
        alpha = helper.validated_alpha("Guess an alphabet")
        if alpha in word:
            for i in range(len(word)):
                if word[i] == alpha:
                    guess_state[i] = alpha
            if "".join(guess_state) == word:
                print("You got it right!. The word is "+word+".")
                break
            print("Current State:\n"+"".join(guess_state))
        else:
            counter -= 1
            print("Sory, Wrong Guess! You have "+str(counter)+" more guesses.")
            print("Current State:\n"+"".join(guess_state))
        
        if counter == 0:
            print("The word is :"+word+".")

    choice = helper.validated_y_n("Do you want to play again?(Y/n)")
    if choice == 'n':
        break
