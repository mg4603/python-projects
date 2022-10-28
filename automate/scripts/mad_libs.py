from sys import argv, exit

def parse_args():
    if len(argv) == 3:
        in_file = argv[1]
        out_file = argv[2]
        return {'in': in_file, 'out': out_file}
    elif len(argv) == 2:
        in_file = argv[1]
        return {'in', in_file}
    else:
        exit("Enter an option\n\t1. <input_file>\n\t2. <input_file> <output_file>\n")

def parse_text(text):
    pass

def main():
    pass