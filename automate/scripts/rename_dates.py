"""
American-style dates: (MM-DD-Y Y Y Y) 
European-style dates" (DD-MM-Y Y Y Y)

Here’s what the program does:
1. It searches all the filenames in the current working directory for
American-style dates.
2. When one is found, it renames the file with the month and day
swapped to make it European-style.

This means the code will need to do the following:
1. Create a regex that can identify the text pattern of American-style dates.
2. Call os.listdir() to find all the files in the working directory.
3. Loop over each filename, using the regex to check whether it has a date.
4. If it has a date, rename the file with shutil.move().
"""
from re import VERBOSE, compile

def parse_args():
    pass

def contains_american_date(text):
    american_date_regex = compile(
        r"""
        ^(\D*?)                                 # all text before the date
        ([1-9]|0[1-9]|1[0-2])-                  # month (single or double digits)
        ([1-9]|0[1-9]|[12][0-9]|3[0-1])-        # day   (single or double digits)
        ((19|20)\d\d)                           # four digits for year
        (\D*?)$                                 # all text after the date
        """
        , VERBOSE
    )
    return american_date_regex.search(text)


def get_filenames(path):
    return list(path.rglob('*'))

def generate_european_date(date):
    pass

def rename_filename(path):
    pass

def main():
    pass

if __name__ == "__main__":
    main()