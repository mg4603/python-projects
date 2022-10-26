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


# Provides the correct answer and three random wrong answers for each
# question, in random order
def make_question(num, questionDict, wrongAnswerList):
    questionString = f'{num}. What is the capital of { questionDict["question"] }.'
    answersList = wrongAnswerList.copy()
    answersList.append(questionDict['answer'])
    for i in range(4):
        questionString += f"    {'ABCD'[i]}. {answersList[i]}\n"
    questionString += '\n'
    return questionString
    
# Creates 50 multiple-choice questions for each quiz, in random order
def create_quiz(capitalsDict):
    # Use random.shuffle() to randomize the order of the questions 
    # and multiple-choice options
    states = capitalsDict.keys()
    capitals = capitalsDict.values()
    quizString = getBanner()
    for i in range(50):
        questionDict = {
            states[i]: capitalsDict[states[i]]
        }
        wrongAnswersList = sample(capitals, 3)
        quizString += makeQuestion(i, questionDict, wrongAnswersList)

    return quizString

def createAllQuizzes(numOfQuizzes):
    # Creates numOfQuizzes different quizzes
    # Writes the answer keys to 35 text files
    # Writes the quizzes to 35 text files
    path = Path('quizzes')
    path.mkdir(parents=True, exist_ok=True)
    for quizNum in range(numOfQuizzes):
        pass

# Write single quiz to file
def writeQuizToFile():
    pass

# Write single answer key to file
def writeAnswerKeyToFile():
    pass