class ParserError(Exception):
    pass

class Sentence():

    def __init__(self, subj, verb, obj):
        self.subj = subj[1]
        self.verb = verb[1]
        self.obj = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None