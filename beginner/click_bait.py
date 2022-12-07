from random import randint, choice

class ClickBait:
    def __init__(self):
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
        pass

    def generate_you_wont_believe_headline(self):
        pass

    def generate_you_dont_want_to_know_headline(self):
        pass

    def generate_gift_idea_headline(self):
        pass

    def generate_reasons_why_headline(self):
        pass

    def generate_job_automated_headline(self):
        pass

    def main(self):
        number_of_headlines = self.get_num_of_headlines()

        for i in range(number_of_headlines):
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