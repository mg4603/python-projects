'''         Periodic Table of Elements
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
    '''

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
        pass