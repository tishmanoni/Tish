#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
            'NewMexico': 'Santa Fe', 'New York': 'Albany','North Carolina': 'Raleigh',
             'North Dakota': 'Bismarck', 
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
            'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
            
            }

for quizNum in range(35):
    #CREATE the quiz and answer keys files
    quizfile = open(f'captalsquiz{quizNum + 1}.txt', 'w')
    answerQuizFile = open(f'captalsquiz_answer{quizNum + 1}.txt', 'w')
    #write out the headers
    quizfile.write('Name:\n\nDate:\n\nPeriod\n\n')
    quizfile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizfile.write('\n\n')

    #shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        #Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # Write the question and the answer options to the quiz file.
        quizfile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

        for i in range(4):
            quizfile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")

        quizfile.write('\n')

        #Write the answer key to a file.
        answerQuizFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        
    quizfile.close()
    answerQuizFile.close()




