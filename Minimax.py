import time
import logging
from sys import maxsize
from Base import Base

DEPTH = 3

class Minimax(Base):
    def __init__(self):
        logging.basicConfig(filename="./PlayerAI.log",level=logging.DEBUG)
        self._logger = logging.getLogger()
        self._logger.info("="*90+"\n"+"="*100)
        self._logger.info("Heuristic is: return len(grid.getAvailableCells())")

        self._no_of_moves = 0
        self._no_of_leaves = 0
        self._avg_move_time = 0
        self._move_time = 0
        self._depth_limit = DEPTH
        self._max_move_depth = 0

        self._time = 0 

    def getMove(self, grid):
        self._max_move_depth = 0
        self._move_time = self._time = time.clock()
        self._no_of_moves+=1
        best_value = maxsize*-1
        for move in grid.getAvailableMoves():
            temp_grid = grid.clone()
            temp_grid.move(move)
            if best_value < self.min(Node(move=move,grid=temp_grid,depth=DEPTH-1)):
                best_move = move

        self._move_time = time.clock() - self._move_time
        self._avg_move_time += self._move_time
        self._logger.info("Move number={}, number of leaves={},max depth{}, time to find={}".format(self._no_of_moves,self._no_of_leaves,self._max_move_depth,self._move_time))

        if move is None:
            raise ValueError("MOVE CANNOT BE NONE")
        return move

    def max(self,node):
        if node._depth > self._max_move_depth:
            self._max_move_depth = node._depth
        if (node._depth <= 0):
            return evaluate(node._grid)
        children = node.get_max_children()
        if len(children) == 0: 
            self._no_of_leaves+=1
            return evaluate(node._grid)

        max_value = maxsize*-1
        for child in children:
            value = self.min(child)
            if value > max_value:
                max_value = value
        return max_value

    def min(self,node):
        if node._depth > self._max_move_depth:
            self._max_move_depth = node._depth
        if (node._depth <= 0):
            return evaluate(node._grid)
        children = node.get_min_children()
        if len(children) == 0: 
            self._no_of_leaves+=1
            return evaluate(node._grid)

        min_value = maxsize
        for child in children:
            value = self.max(child)
            if value < min_value:
                min_value = value
        return min_value

def evaluate(grid):
    heur_vec = []

    number_of_blank_tiles = len(grid.getAvailableCells())
    heur_vec.append(number_of_blank_tiles)

    grid_mask = [[4096,1024,256,64],
                [1024,256,64,16],
                [256,64,16,4],
                [64,16,4,1]]

    monotonicity_score = 0
    for row in range(3):
        for column in range(3):
            monotonicity_score += grid.map[row][column] * grid_mask[row][column]
    heur_vec.append(monotonicity_score)

    bonus = 0
    if grid.map[0][0] == grid.getMaxTile():
        bonus+=10
    elif grid.map[0][3] == grid.getMaxTile():
        bonus+=10
    elif grid.map[3][0] == grid.getMaxTile():
        bonus+=10
    elif grid.map[3][3] == grid.getMaxTile():
        bonus+=10
    heur_vec.append(bonus)

    weight_vec = [1] * len(heur_vec)
    weight_vec = [2,1,1]

    sum = 0
    for i in range(len(heur_vec)):
        sum+=heur_vec[i] * weight_vec[i] 
    return sum

class Node:
    def __init__(self,move=None,grid=None,depth=None):
        self._move = move
        if grid is None:
            raise ValueError("GRID CANNOT BE NONE")
        self._grid = grid
        self._depth = depth

    def get_max_children(self):
        children = []
        for move in self._grid.getAvailableMoves():
            grid=self._grid.clone()
            grid.move(move)
            children.append(Node(move=move,grid=grid,depth=self._depth-1))
        return children

    def get_min_children(self):
        children = []
        for cell in self._grid.getAvailableCells():
            grid=self._grid.clone()
            grid.setCellValue(cell,2)
            children.append(Node(move=None,grid=grid,depth=self._depth-1))
            grid.setCellValue(cell,4)
            children.append(Node(move=None,grid=grid,depth=self._depth-1))
        return children

