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
#https://www.techiedelight.com/print-possible-solutions-n-queens-problem/
#this is going to check if its possible to do it 
def is_possible(grid, r, x):
    #this one needs to return a boolean value 
    #first i got to check the horizontal values
    for i in range(r):
        if board[i][x]=='Q':
            return False
    #then check diagonal values
    #we need to iterate over the previous top rows and cokumns to check if a queen is already there
    n, j=r, x#assign new values and start from the biggest possible row/column
    #this one we check if is diagonal from the right
    for z in range(n,0,-1): #rows 
        for y in range(j,0,-1):#columns 
            if

            
# to iterate by row set r
def place(grid, r):
    #the place function needs to check if its possible then return the value
    #first we iterate the column with x
    for i in range(N):
       if is_possible(board, r, i):
           grid[r][i]='Q'
           place(grid, r+1)

        #and here we use this to iterate the row using recursion
        
    

#start r at zero

place(board, 0)