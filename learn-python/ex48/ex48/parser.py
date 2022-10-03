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

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

class Parser():

    def __init__(self, word_list):
        self.word_list = word_list
    
    