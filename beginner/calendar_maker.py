from pathlib import Path
from datetime import date, timedelta

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

    def get_calendar(self):
        calendar = ''
        
        calendar += f'{(" " * 32)}{self.MONTHS[self.month - 1]} {self.year}\n'
        calendar += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....'
        calendar += 'Friday....Saturday..\n'

        week_separator = f"{'+----------'*7}\n"

        blank_row = f"{'|          ' * 7}|\n"

        current_date = date(self.year, self.month, 1)

        while current_date.weekday() != 6:
            current_date -= timedelta(days=1)
        
        while True:
            calendar += week_separator

            days_number_row = ''
            for i in range(7):
                days_number_row += f'|{str(current_date.day).rjust(2)}{" " * 8}'
                current_date += timedelta(days=1)
            days_number_row += '|\n'

            calendar += days_number_row
            for i in range(3):
                calendar += blank_row
            
            if current_date.month != self.month:
                break
        
        calendar += week_separator
        return calendar

def get_year():
    while True:
        print('Enter the year for the calendar')
        year = input('> ')

        if year.isdecimal() and int(year) > 0:
            return int(year)
            
        print('Please enter a numeric year, like 2020')

def get_month():
    while True:
        print('Enter the month for the calendar, 1-12:')
        month = input('> ')

        if month.isdecimal() and 1 <= int(month) <= 12:
            return int(month)
        
        print('Please enter a numeric month, like 1 for January.')

def save_calendar(output_path, calendar):
    with output_path.open('w') as file:
        file.write(calendar)

if __name__ == '__main__':
    year = get_year()
    month = get_month()
    calendar = CalendarMaker(month, year)
    try:
        calendar_filename = f'calendar_{year}_{month}.txt'
        save_calendar(Path(calendar_filename), calendar.get_calendar())
        print(f'Saved to {calendar_filename}')
    except:
        print('Error while attempting to save file.')