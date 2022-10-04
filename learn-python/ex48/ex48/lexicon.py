from unittest import result


directions = ["north", "south", "east", "west", 
              "up", "down", "left", "right", "back"]

verbs = ["go", "stop", "kill", "eat"]

stop_words = ["the", "in", "of", "from", "at", "it"]

nouns = ["door", "bear", "princess", "cabinet"]

def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def scan(msg):
    msg = msg.lower().split()
    result = []
    for word in msg:
        if word in directions:
            result.append(("direction", word))
        elif word in verbs:
            result.append(("verb", word))
        elif word in stop_words:
            result.append(("stop", word))
        elif word in nouns:
            result.append(("noun", word))
        elif isNum(word):
            result.append(("number", int(word)))
        else:
            result.append(("error", word))
    return result