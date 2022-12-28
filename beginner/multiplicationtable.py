class MultiplicationTable:
    def __init__(s, num):
        s.num = num + 1
        s.length_num = len(str(num))
        s.offset = len(str(num * num))
    
    def display_intro(s):
        print('Multiplication Table')
    
    def display_table(s):
        top_line = ' ' * s.length_num + '|'
        for num in range(s.num):
            top_line += (str(num).rjust(s.offset) + ' ')
        
        second_line = '-' * (len(top_line) - s.length_num - 1)
        second_line = '-' * s.length_num + '|' + second_line
        print()
        print(top_line)
        print(second_line)
        for num1 in range(s.num):
            print(str(num1).rjust(s.length_num), end= '|')
            for num2 in range(s.num):
                print(str(num1 * num2).rjust(s.offset), end=' ')
            print()

if __name__ == '__main__':
    table = MultiplicationTable(13)
    table.display_intro()
    table.display_table()
