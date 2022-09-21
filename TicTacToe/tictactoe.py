# Import the library that needed on the project
import numpy as np
import random

# Create the empty board using np.zeros method create matrix 3x3 the data type is integer
board = np.zeros((3, 3)).astype(int)

# Create a function for check if player win or not
def check_win():
    if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
        return True
    if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
        return True
    return False

# Function to input the player choices to draw on the board
def play_turn():
    # If player using input
    if(turn ==1):
        x = int(input(f"What is player {turn}'s x position?"))
        y = int(input(f"What is player {turn}'s y position?"))
    # Computer using random
    else:
        x = random.randint(0,2);
        y = random.randint(0,2);
    # Try using exception if the input is right or not
    try:
        # If the input right
        if board[y, x]==0:
            board[y, x]=turn
        else:
            # If the column and row already filled
            if(turn == 1):
                print("The board already contains")
            # Draw again
            play_turn()
    # If the input out of the range of board
    except IndexError:
        print("Input error")
        play_turn()

# Initialization variable
# Turn -> player
turn = 1
# Move -> the reminder game turn left
move = 9

# Check if there is a game reminder left
while move >0:
    # Draw the board
    print (board)
    play_turn()
    if check_win():
        print (f"Player {turn} has won!")
        break
    turn = turn*-1
    move = move -1