from GameBoard import Tile

class PQ(): 
    def __init__(self):
        self.queue = []
        self.size = 0

    def add(self,tile):
        self.queue.append(tile)
        self.updateQueue()
        self.size += 1

    def sortQueue(_,tile):
        return tile.distance

    def updateQueue(self):
        self.queue = sorted(self.queue,key=self.sortQueue)

    def top(self):
        return self.queue[0]

    def pop(self):
        self.queue.remove(self.queue[0])
        self.updateQueue()
        self.size -= 1
    
    def empty(self):
        return self.size == 0