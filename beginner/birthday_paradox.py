from datetime import date, timedelta
from random import randint

class BirthdayParadox:
    def __init__(self):
        self.MONTHS = (
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
                    )
        self.birthdays = []
    
    def get_birthdays(self, number_of_birthdays):
        start_of_year = date(2001, 1, 1)
        self.birthdays = []
        for i in range(number_of_birthdays):
            random_number_of_days = timedelta(randint(0, 364))
            birthday = start_of_year + random_number_of_days
            self.birthdays.append(birthday)

    def get_match(self):
        if len(self.birthdays) == len(set(self.birthdays)):
            return None

        for i, birthday_i in enumerate(self.birthdays):
            for j, birthday_j in enumerate(self.birthdays[i + 1:]):
                if birthday_i == birthday_j:
                    return birthday_i

    def display_intro(self):
        print('''
############################## Birthday Paradox ##############################

The Birthday Paradox shows us that in a group of N people, the odds that two 
of them have matching birthdays is surprisingly large. This program does a 
Monte Carlo simulation (that is, repeated random simulations) to explore this
concept.

(It's not actually a paradox, it's just a surprising result.)
'''
)

    def simulate(self):
        self.display_intro()
        while True:
            print('How many birthdays shall I generate? (Max 100)')
            response = input('> ')
            if response.isdecimal() and (0 < int(response) <= 100):
                number_of_birthdays = int(response)
                break
        print()

        print(f'Here are {number_of_birthdays} birthdays:')
        self.get_birthdays(number_of_birthdays)

        for i, birthday in enumerate(self.birthdays):
            if i != 0:
                print(', ', end='')
            month_name = self.MONTHS[birthday.month - 1]
            date_text = f'{month_name} {birthday.day}'
            print(date_text, end='')
        print('\n')

        match = self.get_match()
        print('In this simulation, ', end='')
        if match != None:
            month_name = self.MONTHS[match.month - 1]
            date_text = f'{month_name} {match.day}'
            print(f'multiple people have a birthday on {date_text}.\n')
        else:
            print('there are no matching birthdays.\n')
        
        print(f'Generating {number_of_birthdays} 100,000 times...')
        input('Press Enter to begin...')

        sim_match = 0
        for i in range(100_000):
            if i % 10_000:
                print(f'{i} simulations run...')
            self.get_birthdays(number_of_birthdays)
            if self.get_match() != None:
                sim_match += 1
        print('100,000 simulations run.')
        self.display_results(sim_match, number_of_birthdays)

    def display_results(self, sim_match, number_of_birthdays):
        probability = round(sim_match / 100_000 * 100, 2)
        print(f'Out of 100,000 simulations of {number_of_birthdays} people, there')
        print(f'was a matching birthday in that group {sim_match} times. This')
        print(f'means that {number_of_birthdays} people have a {probability}%')
        print(f'chance of having a matching birthday in their group.')
        print('That\'s probably more than you would think!')

def main():
    pass

if __name__ == '__main__':
    main()