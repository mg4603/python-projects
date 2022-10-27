# Store the states and their capitals in a dictionary
capitals = {

    'Alabama': 'Montgomery', 
    'Alaska': 'Juneau', 
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 
    'California': 'Sacramento', 
    'Colorado': 'Denver',
    'Connecticut': 'Hartford', 
    'Delaware': 'Dover', 
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 
    'Hawaii': 'Honolulu', 
    'Idaho': 'Boise', 
    'Illinois': 'Springfield', 
    'Indiana': 'Indianapolis', 
    'Iowa': 'Des Moines', 
    'Kansas': 'Topeka', 
    'Kentucky': 'Frankfort', 
    'Louisiana': 'Baton Rouge', 
    'Maine': 'Augusta', 
    'Maryland': 'Annapolis', 
    'Massachusetts': 'Boston', 
    'Michigan': 'Lansing', 
    'Minnesota': 'Saint Paul', 
    'Mississippi': 'Jackson', 
    'Missouri': 'Jefferson City', 
    'Montana': 'Helena', 
    'Nebraska': 'Lincoln', 
    'Nevada': 'Carson City', 
    'New Hampshire': 'Concord', 
    'New Jersey': 'Trenton', 
    'New Mexico': 'Santa Fe', 
    'New York': 'Albany', 
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 
    'Ohio': 'Columbus', 
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 
    'Pennsylvania': 'Harrisburg', 
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 
    'South Dakota': 'Pierre', 
    'Tennessee': 'Nashville', 
    'Texas': 'Austin', 
    'Utah': 'Salt Lake City', 
    'Vermont': 'Montpelier', 
    'Virginia': 'Richmond', 
    'Washington': 'Olympia', 
    'West Virginia': 'Charleston', 
    'Wisconsin': 'Madison', 
    'Wyoming': 'Cheyenne'

}

from random import shuffle, sample
from pathlib import Path

def get_banner(num):
    banner = '''Name:\n\nDate:\n\nPeriod:\n\n{}{}\n\n'''.format(
        ' '*20, f'State Capitals Quiz (Form{num + 1})'
    )
    return banner

def get_answer_banner(num):
    banner = '''{}{}\n\n'''.format(
        ' '*20, f'State Capitals Quiz (Answer Key{num + 1})'
    )
    return banner

# Provides the correct answer and three random wrong answers for each
# question, in random order
def make_question(num, questionDict, wrongAnswerList):
    questionString = f'{num + 1}. What is the capital of { questionDict["question"] }?\n'
    answersList = wrongAnswerList.copy()
    answersList.append(questionDict['answer'])
    for i in range(4):
        questionString += f"    {'ABCD'[i]}. {answersList[i]}\n"
    questionString += '\n'
    return questionString

def choose_wrong_answers(rightAnswer, capitals):
    if rightAnswer in capitals:
        capitals.remove(rightAnswer)
    wrongAnswerList = sample(capitals, 3)
    return wrongAnswerList
 
# Creates 50 multiple-choice questions for each quiz, in random order
def create_quiz(num, capitalsDict):
    # Use random.shuffle() to randomize the order of the questions 
    # and multiple-choice options
    states = list(capitalsDict.keys())
    shuffle(states)
    capitals = list(capitalsDict.values())
    quizString = get_banner(num)
    answerString = get_answer_banner(num)
    for i in range(50):
        questionDict = {
            'question': states[i],
            'answer': capitalsDict[states[i]]
        }
        wrongAnswersList = choose_wrong_answers(capitalsDict[states[i]], capitals.copy())
        quizString += make_question(i, questionDict, wrongAnswersList)
        answerString += make_answers(i, questionDict['answer'])
    return quizString, answerString

# Write single quiz to file
def write_quiz_to_file(num, quizText, path):
    with (path / f'capitalsquiz{num + 1}.txt').open('w+') as f:
        f.write(quizText)

# Write single answer key to file
def write_answer_key_to_file(num, answers, path):
    with (path / f'capitalsquiz_answers{num + 1}.txt').open('w+') as f:
        f.write(answers)

def create_all_quizzes(numOfQuizzes):
    # Creates numOfQuizzes different quizzes
    # Writes the answer keys to 35 text files
    # Writes the quizzes to 35 text files
    path = Path('quizzes')
    path.mkdir(parents=True, exist_ok=True)
    for quizNum in range(numOfQuizzes):
        pass

