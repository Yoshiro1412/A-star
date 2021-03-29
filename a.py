from MyQueue import *
from GameBoard import *

def h(start,end):
    return ((start.pos[0]-end.pos[0])**2+(start.pos[1]-end.pos[1])**2)**0.5

def getPath(cameFrom,current):
    path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        path.append(current)
    reversed(path)
    return path

def minPath(Board,start,end):

    cameFrom = {}

    openSet = PQ()
    openSet.add(start)

    start.distance = 0
    start.fScore = h(start,end)

    while not openSet.empty():
        current = openSet.top()
        if(current == end):
            return getPath(cameFrom,current)
        
        openSet.pop()
        for neighbor in Board.neighbors(current):
            tentative = current.distance + 1 # gScore + distance to neighbor
            if tentative < neighbor.distance:
                cameFrom[neighbor] = current
                neighbor.distance = tentative
                neighbor.fScore = neighbor.distance + h(neighbor,end)
                if neighbor not in openSet.queue:
                    openSet.add(neighbor)
    return None

gameMap = ""
with open("map.txt",'r') as f:
    gameMap = f.read()

Map = makeBoard(gameMap)
print(Map)

path = minPath(Map,Map.start,Map.goal)
if path:
    for tile in path:
        Map.board[tile.pos[0]][tile.pos[1]].picture = "x"

print(Map)

