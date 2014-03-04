__author__ = 'Emmalee Roach'
__title___ = 'battle_ship'

from random import randint

board = []
sunk_ships = 0

for x in range(6):                 #initialize a 6X6 playing board
    board.append(["O"] * 6)

def print_board(board):           #display the playing board
    for row in board:
        print "  ".join(row)

def random_row(board):                   #generate random row value for the ship placement
    return randint(0, len(board) - 1)

def random_col(board):                    #generate random column value for the ship placement
    return randint(0, len(board[0]) - 1)

print "Let's play Battleship! You have 10 turns to sink my 3 ships."

print_board(board)

ship_row1 = random_row(board)
ship_col1 = random_col(board)

ship_row2 = random_row(board)
ship_col2 = random_col(board)

while(ship_row1 == ship_row2 and ship_col1 == ship_col2):
    ship_row2 = random_row(board)
    ship_col2 = random_row(board)

ship_row3 = random_row(board)
ship_col3 = random_col(board)

while(ship_row2 == ship_row3 and ship_col2 == ship_col3):
    ship_row3 = random_row(board)
    ship_col3 = random_row(board)



for turn in range(10):                    #player has 10 turns

    guess_row = raw_input("Guess Row:")           #check that row input is an integer
    while guess_row.isdigit() == False:
        print "Error: input must be an integer"
        print "Tip: do not enter any spaces with your number"
        guess_row = raw_input("Guess Row:")
    guess_row = int(guess_row)

    guess_col = raw_input("Guess Column:")        #check that column input is an integer
    while guess_col.isdigit() == False:
        print "Error: input must be an integer"
        print "Tip: do not enter any spaces with your number"
        guess_col = raw_input("Guess Column:")
    guess_col = int(guess_col)

    #check if user has chosen the correct row/column combination for one of the ships

    if (guess_row == ship_row1 and guess_col == ship_col1) or (guess_row == ship_row2 and guess_col == ship_col2) or (guess_row == ship_row3 and guess_col == ship_col3):
        if board[guess_row][guess_col] == "*":
            print "You sunk that ship already!"
        elif sunk_ships == 2:
            board[guess_row][guess_col] = "*"
            print_board(board)
            print "You Win!"
            break
        else:
            print "Congratulations! You sunk one of my battleships!"
            board[guess_row][guess_col] = "*"
            print_board(board)
            sunk_ships += 1
            if turn == 10:
                print "Game Over"
                break

    #if user's input is incorrect, output information accordingly
    else:
        if turn == 10:
            print "Game Over"
            break
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print "Oops, that's not in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    print ("Turns left: " + str(9-turn))
print "Game Over"