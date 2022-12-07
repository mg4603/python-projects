from random import randint, choice

class ClickBaitGenerator:
    def __init__(self, number_of_headlines):
        self.OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
        self.POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
        self.PERSONAL_PRONOUNS = ['She', 'He', 'They']
        self.STATES = [
            'California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
            'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan'
        ]
        self.NOUNS = [
            'Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
            'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
            'Plastic Straw', 'Serial Killer', 'Telephone Psychic'
        ]
        self.PLACES = [
            'House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
            'Workplace', 'Donut Shop', 'Apocalypse Bunker'
        ]
        self.WHEN = [
            'Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week'
        ]
        self.number_of_headlines = number_of_headlines

    def display_intro(self):
        print('----------------------------------------------------------------')
        print('------------------Clickbait Headline Generator------------------')
        print('----------------------------------------------------------------')
        print()
        print('Our website needs to trick people into looking at ads!')

    def generate_are_millennials_killing_headline(self):
        noun = choice(self.NOUNS)
        return 'Are millennials killing the {} Industry?'.format(noun)

    def generate_what_you_dont_know_headline(self):
        noun = choice(self.NOUNS)
        plural_noun = choice(self.NOUNS) + 's'
        when = choice(self.WHEN)
        return 'Without this {}, {} could kill you {}'.format(
            noun, plural_noun, when
        ).title()

    def generate_big_companies_hate_headline(self):
        pronoun = choice(self.OBJECT_PRONOUNS)
        state = choice(self.STATES)
        noun1 = choice(self.NOUNS)
        noun2 = choice(self.NOUNS)
        headline = 'big companies hate {}! see how this {} {} invented a cheaper {}'
        return headline.format(
            pronoun, state, noun1, noun2
        ).title()


    def generate_you_wont_believe_headline(self):
        state = choice(self.STATES)
        noun = choice(self.NOUNS)
        pronoun = choice(self.POSSESSIVE_PRONOUNS)
        place = choice(self.PLACES)
        return 'You won\'t believe what this {} {} found in {} {}'.format(
            state, noun, pronoun, place
        ).title()

    def generate_you_dont_want_to_know_headline(self):
        noun1, noun2 = choice(self.NOUNS), choice(self.NOUNS)
        return 'what {}s don\'t want you to know about {}s'.format(
            noun1, noun2
        ).title()

    def generate_gift_idea_headline(self):
        number = randint(7, 15)
        noun = choice(self.NOUNS)
        state = choice(self.STATES)
        return '{} gift ideas to give your {} from {}'.format(
            number, noun, state
        )

    def generate_reasons_why_headline(self):
        number1 = randint(3, 19)
        plural_noun = choice(self.NOUNS)
        number2 = randint(1, number1)
        headline = '{} reasons why {}s are more interesting than you think (number {} will surprise you!'
        return headline.format(
            number1, plural_noun, number2
        ).title()

    def generate_job_automated_headline(self):
        state = choice(self.STATES)
        noun = choice(self.NOUNS)

        i = randint(0, 2)
        pronoun1 = self.POSSESSIVE_PRONOUNS[i]
        pronoun2 = self.PERSONAL_PRONOUNS[i]
        if pronoun1 == 'Their':
            headline = 'this {} {} didn\'t think robots would take {} job. {} were wrong.'
        else:
            headline = 'this {} {} didn\'t think robots would take {} job. {} was wrong.'
        return headline.format(
            state, noun, pronoun1, pronoun2
        ).title()

    def generate(self):
        for i in range(self.number_of_headlines):
            clickbait_type = randint(1, 8)

            if clickbait_type == 1:
                headline = self.generate_are_millennials_killing_headline()
            elif clickbait_type == 2:
                headline = self.generate_what_you_dont_know_headline()
            elif clickbait_type == 3:
                headline = self.generate_big_companies_hate_headline()
            elif clickbait_type == 4:
                headline = self.generate_you_wont_believe_headline()
            elif clickbait_type == 5:
                headline = self.generate_you_dont_want_to_know_headline()
            elif clickbait_type == 6:
                headline = self.generate_gift_idea_headline()
            elif clickbait_type == 7:
                headline = self.generate_reasons_why_headline()
            elif clickbait_type == 8:
                headline = self.generate_job_automated_headline()
            
            print(headline)
        print()

        website = choice(
            [
                'wobsite', 'blag', 'Facebuuk', 'Googles', 'Fasebook', 
                'teewide', 'Pastagram'
            ]
        )

        when = choice(self.WHEN).lower()
        print(
            'Post these to our {} {} or you\'re fired!'.format(website, when)
            )

def get_number_of_headlines():
    pass

