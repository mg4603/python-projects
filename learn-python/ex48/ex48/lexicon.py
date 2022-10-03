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

def scan():
    pass