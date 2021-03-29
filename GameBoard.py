class Tile():

    def __init__(self,pos,picture,obstacle = False):
        self.pos = pos
        self.picture = picture
        self.distance = 9999 # a.k.a infinity
        self.fScore = 9999
        self.obstacle = obstacle

    def __str__(self):
        return self.picture

class Board():

    def __init__(self,col,row):
        self.board = [[] for i in range(row)]
        self.col = col
        self.row = row
        self.currentTile = [0,0] # Tile to be replaced [row,col]
        self.goal = None
        self.start = None

    def addTile(self,picture):
        pos = (self.currentTile[0],self.currentTile[1])
        tile = Tile(pos,picture)
        self.board[self.currentTile[0]].append(tile)
        
        if picture == "@": self.goal = tile
        if picture == "S": self.start = tile
        if picture == "#": tile.obstacle = True

        if self.currentTile[1] >= self.col - 1: # Catch out of bounds
            self.currentTile[1] = -1 # Restart to 0 de col
            self.currentTile[0] = self.currentTile[0]+1
        
        self.currentTile[1] = self.currentTile[1]+1 # Move to the next col

    # Print map that is stored in 1D
    def __str__(self):
        Map = ""
        for y in range(self.row):
            for x in range(self.col):
                Map += str(self.board[y][x]) + " "
            Map += "\n"
        return Map

    def neighbors(self,tile):
        neighbor = []
        pos = tile.pos
        if pos[0] - 1  >= 0:
            n = self.board[pos[0] - 1][pos[1]]
            if not n.obstacle: neighbor.append(n)
        if pos[0] + 1  < self.row:
            n = self.board[pos[0] + 1][pos[1]]
            if not n.obstacle: neighbor.append(n)
        if pos[1] - 1  >= 0:
            n = self.board[pos[0]][pos[1] - 1]
            if not n.obstacle: neighbor.append(n)
        if pos[1] + 1  < self.col:
            n = self.board[pos[0]][pos[1] + 1]            
            if not n.obstacle: neighbor.append(n)
        return neighbor

def makeBoard(gameMap):

    # Clear Map data
    lines = gameMap.splitlines()
    row = len(lines)
    col = len(lines[1].replace(" ",""))

    # Create new Map
    Map = Board(col,row)

    for c in gameMap:
        if c != ' ' and c != '\n':
            Map.addTile(c)
    return Map