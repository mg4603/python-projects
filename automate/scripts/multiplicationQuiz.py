"""
1. Ask 10 questions
    - query user for product of two random numbers between 0 and 9
    - set a limit of 3 tries
    - set a time limit of 8 seconds
    - use block regex to reject all answers other than the correct one
    - use an allow regex to accept the correct answer
2. count number of correct answers
3. Display number of correct answers
"""

from random import randint
from time import sleep
from pyinputplus import inputNum, TimeoutException, RetryLimitException

def quiz(numberOfQuestions):
    correctAnswers = 0
    for i in range(numberOfQuestions):
        number1 = randint(0, 9)
        number2 = randint(0, 9)
        prompt = '#%s: %s x %s = ' % (i+1, number1, number2)
        try:
            inputNum(
                prompt, 
                allowRegexes=['^%s$' % (number1 * number2)], 
                blockRegexes=[('.*', 'Incorrect!')],
                limit=3, timeout=9
            )
        except TimeoutException:
            print('Out of Time')
        except RetryLimitException:
            print('Out of Tries')
        else:
            correctAnswers += 1
            print("Correct!")
    
    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
    sleep(1)

if __name__ == '__main__':
    quiz(10)