from time import sleep, localtime
from sys import exit
try:
    from sevseg import SevSeg
except ModuleNotFoundError:
    exit('Import error: sevseg module needs to be in the same dir.')
class DigitalClock:
    def __init__(self):
        pass

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('------------------------Digital Clock------------------------')
        print('-------------------------------------------------------------')
        print('Displays a digital clock of the current time with a seven')
        print('segment display. Press CTRL-C to stop.')

    def main(self):
        sev_seg = SevSeg()
        try:
            while True:
                # clear screen after each second
                print('\n' * 60)

                current_time = localtime()
                hours = str(current_time.tm_hour)
                mins = str(current_time.tm_min)
                secs = str(current_time.tm_sec)
                
                h_digits = sev_seg.get_sev_seg(hours, 2)
                h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()
                m_digits = sev_seg.get_sev_seg(mins, 2)
                m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()
                s_digits = sev_seg.get_sev_seg(secs, 2)
                s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

                print('{}   {}   {}'.format(
                    h_top_row, m_top_row, s_top_row
                ))
                print('{} * {} * {}'.format(
                    h_middle_row, m_middle_row, s_middle_row
                ))
                print('{} * {} * {}'.format(
                    h_bottom_row, m_bottom_row, s_bottom_row
                ))
                print('Press CTRL-C to quit.')
                while True:
                    sleep(0.01)
                    if current_time.tm_sec != localtime().tm_sec:
                        break
        except KeyboardInterrupt:
            print('Digital Clock')
            exit()

if __name__ == '__main__':
    clock = DigitalClock()
    clock.display_intro()
    clock.main()