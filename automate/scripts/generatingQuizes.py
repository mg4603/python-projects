"""
1. Creates 35 different quizzes
2. Creates 50 multiple-choice questions for each quiz, in random order
3. Provides the correct answer and three random wrong answers for each
question, in random order
4. Writes the quizzes to 35 text files
5. Writes the answer keys to 35 text files
This means the code will need to do the following:
1. Store the states and their capitals in a dictionary
2. Call open(), write(), and close() for the quiz and answer key text files
3. Use random.shuffle() to randomize the order of the questions and
multiple-choice options
"""

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