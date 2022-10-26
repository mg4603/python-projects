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
from random import shuffle
from pathlib import Path

def getBanner(num):
    banner = '''Name:\n\nDate:\n\nPeriod:\n\n{}{}\n\n'''.format(
        ' '*20, f'State Capitals Quiz (Form{num + 1})'
    )
    return banner


# Provides the correct answer and three random wrong answers for each
# question, in random order
def makeQuestion(num, questionDict, wrongAnswerList):
    questionString = f'{num}. What is the capital of { questionDict["question"] }.'
    answersList = wrongAnswerList.copy()
    answersList.append(questionDict['answer'])
    for i in range(4):
        questionString += f"    {'ABCD'[i]}. {answersList[i]}\n"
    questionString += '\n'
    return questionString
    
