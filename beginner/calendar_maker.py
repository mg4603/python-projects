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
    pass