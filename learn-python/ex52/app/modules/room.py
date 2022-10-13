from random import randint

class Room:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)

    

class Death:
    
    def __init__(self, room, cause, description):
        self.room = room
        self.cause = cause
        self.description = description

    def getRoom(self):
        return self.room
    
    def getCause(self):
        return self.cause
    
    def getDescription(self):
        return self.description
    

def getRandomQuip(self):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    return self.quips[randint(0, len(self.quips)-1)]
    
    