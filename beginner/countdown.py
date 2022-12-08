from sevseg import SevSeg
from sys import exit
from time import sleep
class Countdown:
    def __init__(self, hours, mins, secs, message):
        self.hours, self.mins, self.secs = hours, mins, secs
        self.message = message
    
    def display_intro(self):
        print('-------------------------------------------------------------')
        print('--------------------------Countdown--------------------------')
        print('-------------------------------------------------------------')
        print('Show a countdown timer animation using a seven-segment ')
        print('display.')
        print('Requires sevseg to be in the same folders')
        print('Press CTRL-C to stop.')
        print()
    
    def main(self):
        sevSeg = SevSeg()
        try:
            while True:
                print('\n' * 60)
                h_digits = sevSeg.get_sev_seg(self.hours, 2)
                h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

                m_digits = sevSeg.get_sev_seg(self.mins, 2)
                m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

                s_digits = sevSeg.get_sev_seg(self.secs, 2)
                s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

                print('{}   {}   {}'.format(h_top_row, m_top_row, s_top_row))
                print('{} * {} * {}'.format(h_middle_row, m_middle_row, s_middle_row))
                print('{} * {} * {}'.format(h_bottom_row, m_bottom_row, s_bottom_row))
                

                if self.secs > 0:
                    self.secs -= 1

                elif self.secs == 0 and self.mins > 0:
                    self.mins -= 1
                    self.secs = 59

                elif self.secs == 0 and self.mins == 0 and self.hours > 0:
                    self.hours -= 1
                    self.mins = 59
                    self.secs = 59

                elif self.hours == 0 and self.mins == 0 and self.secs == 0:
                    print()
                    print('     * * * * {} * * * *'.format(self.message))
                    break

                print()
                print('Press CTRL-C to quit.')

                sleep(1)


        except KeyboardInterrupt:
            print('Countdown')
            exit()

if __name__ == '__main__':
    timer = Countdown(1, 1, 10, 'boom')
    timer.display_intro()
    timer.main()
