#Julian Shniter
#Dice game
#Simulates a game of pig between two players and a computer
#Lasted Edited: 12/03/2021


from dice import Die
computerpoints=0
player1points=0
player2points=0

def playerturn(playerpoints, die):
    pointsdelta=0
    while True:
        roll=die.roll()
        print("You rolled a {}".format(roll))
        pointsdelta+=roll
        
        if roll==1 or roll==2:
            print("You get zero points")
            pointsdelta=0
            break
        print("You've scored {} more points".format(pointsdelta))
        playerchoice=str(input("Would you like to roll again\nEnter Y or yes and N for no\n"))
        if playerchoice=='N':
            playerpoints+=pointsdelta
            print("You currently have {} points.".format(playerpoints))
            break
    
def computerturn(points, die):
    pointsdelta=0
    while pointsdelta<20:
        roll=die.roll()
        pointsdelta+=roll
        if roll==1 or roll ==2:
            pointsdelta=0
            break
    points+=pointsdelta
    print("The computer has {} points".format(points))



die=Die(10)
while True:
    #player 1 turn
    print("Player 1's turn")
    playerturn(player1points, die)
    if player1points>=100:
        print('Player 1 wins!')
        break
    #player 2 turn
    print("Player 2's turn")
    playerturn(player2points, die)
    if player2points>=100:
        print("Player 2 wins!")
        break
    #computer turn
    computerturn(computerpoints, die)
    if computerpoints>=100:
        print("The computer wins")
        break