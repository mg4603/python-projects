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
    quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
    ]

    def __init__(self, room, cause):
        self.room = room
        self.cause = cause

    def getRoom(self):
        return self.room
    
    def getCause(self):
        return self.cause
    
    def getRandomQuip(self):
        return self.quips[randint(0, len(self.quips)-1)]