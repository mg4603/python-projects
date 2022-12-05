class CalendarMaker():
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.DAYS = (
            'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday'
        )
        self.MONTHS = (
            'January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December'
        )

    def display_intro(self):
        print('----------------------------Calendar Maker----------------------------')
        print('  Create monthly calendars, saved to a text file and fit for printing')
        print('----------------------------------------------------------------------\n')

def get_year():
    while True:
        print('Enter the year for the calendar')
        year = input('> ')

        if year.isdecimal() and int(year) > 0:
            return int(year)
            
        print('Please enter a numeric year, like 2020')

def get_month():
    pass