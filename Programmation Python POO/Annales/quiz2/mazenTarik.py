# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 02:27:06 2021

@author: zahra
"""

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
                    nbMoves = "0"          
                movesLine.append(nbMoves)
            
            self.moves.append(movesLine)
 
    
    def __str__(self):
        res = ""
        self.str2maze(tStr)
        self.maze2move()
        for i in range(self.dims[1]):
            for j in range(self.dims[0]):
                if self.grid[i][j] == "#":
                    res += self.grid[i][j]
                else:
                    res += str(self.moves[i][j])
            res += "\n"
        return res
        
        