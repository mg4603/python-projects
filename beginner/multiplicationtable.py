class MultiplicationTable:
    def __init__(s, num):
        s.num = num
        s.length = len(str(num * num))
    
    def display_intro(s):
        print('----------------------------------------------------')
        print('--------------- Multiplication Table ---------------')
        print('----------------------------------------------------')
        