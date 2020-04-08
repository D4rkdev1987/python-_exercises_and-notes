# Exercise 27 - Tic Tac Toe Draw
# Exercise to draw Tic Tac Toe gameboard the game board getting input from Player 1 and Player 2
# Last updated: 17/02/2016
#
# - gets input from two players
# - checks the input for correctness: row,col
# - exits if board is full or there is a winner


# initialise the game board
gameboard = [(['.']*3) for i in range(3)]

# variables for input and turn count
row_col = [0]
turn = 1

# checks that the input is valid 
# - that it is in the format "row,col"
# - that the position is free
def input_valid(values):
	# input has only two values
    if len(values) != 2:
        print ("Input must be two numbers in format row,col e.g.  1,2 ")
        return 0
    # input is a number between 1 and 3 (inclusive)
    try:
        if (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):
            # checks if the position on the board is alreay filled
            if gameboard[int(values[0])-1][int(values[1])-1] != '.':
                print( "Position on board already taken.")
                return 0
            return 1
        else:
            print("Input values must be numbers between 1 and 3 (inclusive)")
            return 0
    except ValueError:
        print ("Input values must be numbers between 1 and 3 (inclusive)")
        return 0


# draw the board
def draw_board(values, player):
    # changes the value to X or O
    gameboard[int(values[0])-1][int(values[1])-1]=player

    # print the gameboard
    for row in gameboard:
        print(row)

# calculate if game is over (no more '.' or has winner)
def game_over():
    searcht = '.'
    
    # check win by row
    for i in range(3):
        if len(set(gameboard[i])) == 1:
            if gameboard[i][1] == '.':
                continue
            elif gameboard[i][1] == 'X':
                print ("Game over - Player 1 wins")
            #elif gameboard[i][1] == 'O':
            else:
                print( "Game over - Player 2 wins")
            return 1

    # check win by column
    for i in range(3):
        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i]:
            if gameboard[0][i] == '.':
                continue
            elif gameboard[0][i] == 'X':
                print ("Game over - Player 1 wins")
            else:
                print( "Game over - Player 2 wins")
            return 1

    # check win by diagonal
    if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2]) or (gameboard[0][2] == gameboard[1][1] == gameboard[2][0]): 
        if gameboard[1][1] == 'X':
            print( "Game over - Player 1 wins")
        elif gameboard[1][1] == 'O':
            print( "Game over - Player 2 wins")
        else:
            return 0
        return 1

    # check board is full
    for sublist in gameboard:
        if searcht in sublist:
            return 0

    print ("Game over - the board is filled")
    return 1




# main function that runs the game while board is not full
while not game_over():
    piece = '.'

    # Player input - checks for input correctness
    while not input_valid(row_col):
        player = turn % 2
        if player == 0:
         	player = 2
        piece = 'O'
    else:
        piece = 'X'
        p1 = input('Player ' + str(player) +' input: ')
        row_col = p1.split(",")

    draw_board(row_col, piece)

    row_col = [0]
    turn += 1