from random import randint

class Room:
    
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)

    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description

    

def getRandomQuip(self):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    return self.quips[randint(0, len(self.quips)-1)]
    
    