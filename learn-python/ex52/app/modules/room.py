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
    def __init__(self, room, cause):
        self.room = room
        self.cause = cause

    def getRoom(self):
        return self.room
    
    def getCause(self):
        return self.cause