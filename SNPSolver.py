#Athavan Jesunesan

import copy
cutoffList = [3]

# ----------- Classes and functions ------- #
class Puzzle(object):
    def __init__(self):
        self.found = False                       # Whether or not the IDS is completed
        self.size = 0
        self.arr = [0][0]
        self.position = (0, 0)

    def goalState(self):
        if self.size == 3:
            return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', 'x']]
        elif self.size == 4:
            return [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', 'x']]

    def availableMoves(self):
        moves = ''
        row, col = self.position
        
        if col > 0:                 # Can move to the left
            moves += 'left '

        if col < (self.size - 1):   # Can move to the right
            moves += 'right '    

        if row > 0:                 # Can move up

            moves += 'up '       

        if row < (self.size - 1):   # Can move down
            moves += 'down'     

        return moves

    def left(self): # moves x to the left
        row, col = self.position
        self.arr[row][col] = self.arr[row][col-1]
        self.arr[row][col-1] = 'x'
        self.position = (row, col - 1)
        return self


    def right(self): # moves x to the right
        row, col = self.position
        self.arr[row][col] = self.arr[row][col+1]
        self.arr[row][col+1] = 'x'
        self.position = (row, col + 1)
        return self
        

    def up(self): # moves x up
        row, col = self.position
        self.arr[row][col] = self.arr[row-1][col]
        self.arr[row-1][col] = 'x'
        self.position = (row - 1, col)
        return self

    def down(self): # moves x down
        row, col = self.position
        self.arr[row][col] = self.arr[row+1][col]
        self.arr[row+1][col] = 'x'
        self.position = (row + 1, col)
        return self

    def hammingDistance(self):
        # --------- Set up arrays for ham ------- #
        temp1 = [0 for i in range(self.size*self.size - 1)] 
        temp2 = [0 for i in range(self.size*self.size - 1)]
        x = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.arr[row][col] != 'x':
                    temp1[x] = self.arr[row][col]
                    x+=1
                

        x = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.goalState()[row][col] != 'x':
                    temp2[x] = self.goalState()[row][col]
                    x+=1
        
        # --------------- get the ham ----------- #

        ham = 0

        for val in range(self.size*self.size - 1):
            if temp1[val] != temp2[val]:
                ham += 1

        return ham

def ids(puzzle, completedMoves, depth): # Iterative Deepening Search
    if puzzle.arr == puzzle.goalState():
        print()
        print(completedMoves)
        print()
        pubPuzzle.found = True
        return
    if depth != 0:
        for move in puzzle.availableMoves().split(' '):
            if move == 'left':
                ids(copy.deepcopy(puzzle).left(), completedMoves + 'left ', depth-1)
            if move == 'right':
                ids(copy.deepcopy(puzzle).right(), completedMoves + 'right ', depth-1)
            if move == 'up':
                ids(copy.deepcopy(puzzle).up(), completedMoves + 'up ', depth-1)
            if move == 'down':
                ids(copy.deepcopy(puzzle).down(), completedMoves + 'down ', depth-1)


def idas(puzzle, completedMoves, depth, cutoff, curDepth): # iterative deepening A* Search
    if puzzle.arr == puzzle.goalState():
        pubPuzzle.found = True
        print()
        print(completedMoves)
        print()
        return
    if depth != 0 and puzzle.hammingDistance()+curDepth <= cutoff:
        for move in puzzle.availableMoves().split(' '):
            if move == 'left':
                idas(copy.deepcopy(puzzle).left(), completedMoves + 'left ', depth-1, cutoff, curDepth+1)
            if move == 'right':
                idas(copy.deepcopy(puzzle).right(), completedMoves + 'right ', depth-1, cutoff, curDepth+1)
            if move == 'up':
                idas(copy.deepcopy(puzzle).up(), completedMoves + 'up ', depth-1, cutoff, curDepth+1)
            if move == 'down':
                idas(copy.deepcopy(puzzle).down(), completedMoves + 'down ', depth-1, cutoff, curDepth+1)

    elif puzzle.hammingDistance() + curDepth > cutoff and pubPuzzle.found == False:
        cutoffList.append(puzzle.hammingDistance()+curDepth) 
        


#  --------- Set up ----------- #
pubPuzzle = Puzzle()
file = open('puzzle.txt', 'r')
pubPuzzle.size = int(file.readline())
pubPuzzle.arr = [[0 for i in range(pubPuzzle.size)] for j in range(pubPuzzle.size)]


for i in range(pubPuzzle.size):
    x = file.read(5).split(' ')
    for j in range(pubPuzzle.size):
        pubPuzzle.arr[i][j] = x[j]
        if x[j] == 'x':
            pubPuzzle.position = (i, j)
    file.readline()


# ------- Iterative deepening search ----- #

depth = 3
while pubPuzzle.found == False:                                                      # If not complete then increment
    ids(copy.deepcopy(pubPuzzle), ' ', depth)
    depth+=1


# -------- Iterative deepening A* search ----- #

pubPuzzle.found = False
depth = 1

while pubPuzzle.found == False:
    low = min(cutoffList) #The smallest f(n) value
    cutoffList = []
    idas(copy.deepcopy(pubPuzzle), ' ', depth, low, 0)
    depth+=1


file.close()




    



