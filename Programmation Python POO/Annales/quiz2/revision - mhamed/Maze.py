#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 23:50:32 2021

@author: benaissa
"""

class Maze:
    def __init__(self,width,height,tStr):
        self.dims = [width,height]
        
        l = width
        w = height
        
        self.grid = [[1]*l]*w
        #self.str2maze()
        for i,e in enumerate(tStr):
            for j,c in enumerate(e):
                self.grid[i][j] = c 
        
        self.move = [[1]*l]*w
        #self.maze2move()
        compteur = 0
        for i,l in enumerate (tStr):
            for j,c in enumerate (l):
                if self.grid[i][j] == '#':
                    self.move[i][j] = 0
                    break

                if self.grid[i-1][j] == '0':
                    compteur += 1
                if self.grid[i+1][j] == '0':
                    compteur += 1
                if self.grid[i][j+1] == '0':
                    compteur += 1
                if self.grid[i][j-1] == '0':
                    compteur += 1
                self.move[i][j] = compteur
                compteur = 0
        
        def str2maze(self,tStr):
            for i,e in enumerate(tStr):
                for j,c in enumerate(e):
                    self.grid[i][j] = c 
        
        
        
        
        
        def maze2move(self):
            compteur = 0
            for i,l in enumerate (self.grid):
                for j,c in enumerate (l):
                    if self.grid[i][j] == '#':
                        self.move[i,j] = 0
                        break
    
                    if self.grid[i-1][j] == '0':
                        compteur += 1
                    if self.grid[i+1][j] == '0':
                        compteur += 1
                    if self.grid[i][j+1] == '0':
                        compteur += 1
                    if self.grid[i][j-1] == '0':
                        compteur += 1
                    self.move[i][j] = compteur
                    compteur = 0
                    
        def toString(self):
            for i in range(self.dims[0]):
                for j in range(self.dims[1]):
                   
                    if self.grid[i][j] == "#":
                       
                        print("#", end = "")
                       
                    else :
                        print(self.move[i][j], end="")
            
                       
                   
           
                
        
        
    
                
    
width = 5
height = 12
tStr = ['00###', '000#0', '####0', '0##0#', '00#00', '0#000', '0#000', '0000#', '0000#', '0##00', '#0#00', '#00#0']

M = Maze(width,height,tStr)

M.toString()

