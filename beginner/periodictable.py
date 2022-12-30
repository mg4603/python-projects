from csv import reader
from sys import exit
from pathlib import Path
from re import sub

class PeriodicTable:
    ALL_COLUMNS = [
        'Atomic Number', 'Symbol', 'Element', 'Origin of name', 'Group',
        'Period', 'Atomic weight', 'Density', 'Melting point', 
        'Boiling point', 'Specific heat capacity', 'Electro-negativity',
        'Abundance in earth\'s crust'
    ]
    def __init__(s):
        s.longest_column = 0
        s.elements = {}
    
    def get_elements(s):
        with Path('elements.csv').open('r', encoding='utf-8') as file:
            csv_reader = reader(file)
            elements = list(csv_reader)
        
        for line in elements:
            element = {
                'Atomic Number':                line[0],
                'Symbol':                       line[1],
                'Element':                      line[2],
                'Origin of name':               line[3],
                'Group':                        line[4],
                'Period':                       line[5],
                'Atomic weight':                line[6]  + ' u',
                'Density':                      line[7]  + ' g/cm^3',
                'Melting point':                line[8]  + ' K',
                'Boiling point':                line[9]  + ' K',
                'Specific heat capacity':       line[10] + ' J/(g*K)',
                'Electro-negativity':           line[11],
                'Abundance in earth\'s crust':  line[12] + ' mg/kg'
            }
            for key, value in element.items():
                element[key] = sub(r'\[(I|V|X)+\]', '', value)
            
            s.elements[line[0].strip()] = element
            s.elements[line[1].strip()] = element
    
    def get_longest_col(s):
        for key in s.ALL_COLUMNS:
            if len(key) > s.longest_column:
                s.longest_column = len(key)
    
    def setup(s):
        s.get_elements()
        s.get_longest_col()
    
    def display_intro(s):
        print('Periodic Table of Elements')
        print()
    
    def main(s):
        s.setup()
        while True:
            print('''
                Periodic Table of Elements
        1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 
        1 H                                                  He
        2 Li Be                               B  C  N  O  F  Ne
        3 Na Mg                               Al Si P  S  Cl Ar
        4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
        5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
        6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
        7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
    
                Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
        ''')

            print('Enter a symbol or atomic number to examine, or QUIT to quit.')
            response = input('> ').title()
            if response == 'Quit':
                exit()
            
            if response in s.elements:
                for key in s.ALL_COLUMNS:
                    key_justified = key.rjust(s.longest_column)
                    print('{}: {}'.format(key_justified, s.elements[response][key]))
                input('Press Enter to continue...')