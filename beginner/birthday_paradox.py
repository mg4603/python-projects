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

        for i in range(number_of_birthdays):
            random_number_of_days = timedelta(randint(0, 364))
            birthday = start_of_year + random_number_of_days
            self.birthdays.append(birthday)

    def get_match(self):
        pass

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
        pass

    def display_results(self):
        pass

def main():
    pass

if __name__ == '__main__':
    main()