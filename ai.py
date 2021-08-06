import library
from copy import deepcopy

# Function to print the board
def print_board(board):
    print('\n')
    for row in board:
        for column in row:
            print(column, end = ' ')
        
        print('\n')
        
# Function to play the game
def move(board, position, player):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == position:
                board[row][column] = player
                
    return board

# Function to determine game winner
def has_won(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
            
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
            
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
        
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
        
    return False

# Function to evaluate available position
def available_position(board):
    position = []
    for row in board:
        for column in row:
            if column != 'X' and column != 'O':
                position.append(int(column))
    return position

# Function to evaluate the end of game
def gameover(board):
    if has_won(board, 'X') or has_won(board, 'O') or len(available_position(board)) == 0:
        return True
    else:
        return False

# Function to evaluate the winning score for Minimax
def evaluate(board):
    if has_won(board, 'X'):
        return 1 # X player is maximizing
    elif has_won(board, 'O'):
        return -1 # O player is minimizing
    else:
        return 0

# Function of Minimax algorithm
def minimax(board, maximizing):
    # Return the score when the game is over
    if gameover(board):
        score = evaluate(board)
        return [score, '']
    
    # Algorithm for the maximizing player: X
    if maximizing:
        best_score = - float('Inf') # Initiate the lowest score
        best_move = ''
        
        # Loop through all the available position
        for position in available_position(board):
            # Copy the board
            board_copy = deepcopy(board)
            
            # Select the move
            board_copy = move(board_copy, position, 'X')
            
            # Recursively find opponent's movement
            simulation_score = minimax(board_copy, False)[0]
            
            # Update the best score with higher score
            if simulation_score > best_score:
                best_score = simulation_score
                best_move = position
        
        # Return list of the score and the move
        return [best_score, best_move]
        
    else:
        best_score = float('Inf') # Initiate the highest score
        best_move = ''
        
        # Loop through all the available position
        for position in available_position(board):
            # Copy the board
            board_copy = deepcopy(board)
            
            # Select the move
            board_copy = move(board_copy, position, 'O')
            
            # Recursively find the opponent's movement
            simulation_score = minimax(board_copy, True)[0]
            
            # Update the best score with the lower score
            if simulation_score < best_score:
                best_score = simulation_score
                best_move = position
        
        return [best_score, best_move]
    
