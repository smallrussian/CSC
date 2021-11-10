import numpy as np
from itertools import permutations
#i tried to figure out all the stuff myself, but i stole the check diagonals from this 
#and this https://www.codespeedy.com/solve-8-queens-problem-in-python/
N=8
board = [['x']*N for _ in range(N)]

print(board)
# i need to do multiple things
#check if it can be placed
#place actually place it 
#print all possible solutions
#do it row by row

#this is going to check if its possible to do it 
def if_possible(grid, r, x):
    #first i got to check the horizontal values
    for i in range(r):
        if board[i][x]=='Q': 
            return False
    #then check diagonal values
            

def place(grid):
    #the place function needs to check if its possible then return the value
    for x in range(r):
       if if_possible(grid, x):
