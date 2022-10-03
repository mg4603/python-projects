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
    
    def parse_verb(self):
        skip(self.word_list, "stop")

        if peek(self.word_list) == "verb":
            return match(self.word_list, "verb")
        else:
            raise ParserError("Expected a verb next.")
    
    def parse_object(self):
        skip(self.word_list, "stop")
        next = peek(self.word_list)

        if next == "noun":
            return match(self.word_list, "noun")
        elif next == "direction":
            return match(self.word_list, "direction")
        else:
            raise ParserError("Expected a noun or direction next.")
    
    def parse_subject(self, subj):
        verb = self.parse_verb()
        obj = self.parse_object()
        
        return Sentence(subj, verb, obj)
    
    def parse_sentence(self):
        skip(self.word_list, "stop")

        start = peek(self.word_list)

        if start == "noun":
            subj = match(self.word_list, "noun")
            return self.parse_subject(subj)
        elif start == "verb":
            return self.parse_subject(("noun","player"))
        else:
            raise ParserError("Must start with subject object, or verb not:%s" % start)
            