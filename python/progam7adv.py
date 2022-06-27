#Julian Shniter
#Eight Queens Puzzle
#lists all possible solution for SAFE queen placement on an 8x8 chessboard
#last edited 11/10/2021

#note, i havent looked but there is no way somebody on the internet didn't do the same thing as me 
def is_possible(matrix, r, x):
    #this one needs to return a boolean value 
    #first i got to check the horizontal values
    for i in range(r):
        if matrix[i][x]=='Q':
            return False
    #then check diagonal values
    #we need to iterate over the previous top rows and cokumns to check if a queen is already there
    n, z=r, x#assign new values and start from the biggest possible row/column
    #this one we check if is diagonal from the right, by iterating j down by 1 
    #i tried a for loop but that wouldnt work cause it goes throw each row and column value instead of just diagonal values
    while n>=0 and z>=0:
        if matrix[n][z]=='Q':
            return False
        n-=1
        z-=1
    #since we use while we have to reset n and z
    n,z=r,x
    while n>=0 and z<N:#use N or len(matrix)
        if matrix[n][z]=='Q':
            return False
        n-=1
        z+=1
        #this time we iterate up because its from the left diagonals 
    return True
def write_sol(matrix):
    for r in matrix:
        f.write(str(r).replace(',','').replace('\'','')+'\n')
    f.write('\n')
def printsol(matrix):
    for r in matrix:
        print(str(r).replace(',', '').replace('\'', ''))
    print()
    
    #im telling the file it has 92 of them so it can label all the solutions
# to iterate by row set r
def place(matrix, r):
    #the place function needs to check if its possible then return the value
    if r==len(matrix): #checks if we actually made it all the way to the end 
        write_sol(matrix)
        #return
    #first we iterate the column with x
    for i in range(len(matrix)):
       if is_possible(matrix, r, i):
           matrix[r][i]='Q'
           place(matrix, r+1)#and here we use this to iterate the row using recursion
           matrix[r][i] ='X' #backtracks and makes it so the queen and only appear once in a single row, otherwise it gets all messed up 
        
        
    

#start r at zero
f=open("chess.txt", 'a')
N=8
board = [['X']*N for _ in range(N)] #i dont remember where i found it but the internet definitely gave me this line of code
#print(board)
place(board, 0)
f.close()

# i found something on the internet that was the same as this after i wrote it, but i forgot to grab the link