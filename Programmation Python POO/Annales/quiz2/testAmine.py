# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 23:26:50 2021

@author: zahra
"""

#import numpy as np

class Maze:
    def __init__(self,width, height, tStr):
        self.dims = [width,height]
        self.grid  = []
        self.moves = []
        
        
    def str2maze(self,tStr):
        
        for i,line in enumerate(tStr):
            self.grid.append(list(line))
    
    def maze2move(self):
        
        for i in range(self.dims[1]):
            movesLine = []
            for j in range(self.dims[0]):
                nbMoves = 0
                if self.grid[i][j] == "0":
                    if j != self.dims[0] -1 :
                        if self.grid[i][j+1] == "0":
                            nbMoves +=1
                    if j != 0:
                        if self.grid[i][j-1] == "0":
                            nbMoves +=1
                            
                    if i != self.dims[1] -1 :        
                        if self.grid[i+1][j] == "0":
                            nbMoves += 1
                    if i != 0:    
                        if self.grid[i-1][j] == "0":
                            nbMoves += 1
                            
                else :
                    nbMoves = "#"          
                movesLine.append(nbMoves)
            
            self.moves.append(movesLine)
 

    
    def __str__(self):
        res = ""
        for line in self.moves:
            for c in line :
                res += str(c)
            res += "\n"
        return res
        



#width = 5
#height = 12
#tStr = ['00###', '000#0', '####0', '0##0#', '00#00', '0#000', '0#000', '0000#', '0000#', '0##00', '#0#00', '#00#0']

width = 10
height = 4
tStr = ['00#000##00', '##0####00#', '0000000000', '0#00000000']
    
myMaze = Maze(width,height,tStr) 
myMaze.str2maze(tStr)

myMaze.maze2move()


print(myMaze)

