board = \
    [
        [' ', '|', ' ', '|', ' '],
        ['_', '+', '_', '+', '_'],
        [' ', '|', ' ', '|', ' '],
        ['_', '+', '_', '+', '_'],
        [' ', '|', ' ', '|', ' ']
    ]

PLAYER1 = 'X'
PLAYER2 = 'O'
current_player = 'X'
game_over = False

def margin_top_bottom(func):
    '''
    Adds empty lines before and after the output of the wrapped function.
    Enhances readability and visual separation in console output.
    '''
    def wrapper():
        print()
        func()
        print()
    return wrapper

@margin_top_bottom
def display_board():
    '''
    Prints the current state of the 5x5 Tic Tac Toe board.
    Uses a grid format with separators for visual clarity.
    '''
    for i in range(5):
        for j in range(5):
            print(board[i][j], end=" ")
        print()

# to display game title, game instruction and game board
print("***********************")
print("----Tic Tac Toe Game---")
print("***********************")
print('''
         NOTE : Even numbers represents rows and columns.
           For instance,
               - '0' for first row/column,
               - '2' for second row/column,
               - '4' for third row/column.''')
display_board()

def check_winner():
    '''
    Checks the game board to determine if the current player has won.
    Evaluates horizontal, vertical, and diagonal winning conditions.
    If a win is found, prints the winner and sets game_over to True.
    '''
    global current_player, game_over

    # Horizontal
    for i in range(0, 5, 2):
        if board[i][0] == ' ': continue
        if board[i][0] == board[i][2] and board[i][2] == board[i][4]:
            game_over = True
            print(f"{current_player} Wins!")
            return

    # Vertical
    for i in range(0, 5, 2):
        if board[0][i] == ' ': continue
        if board[0][i] == board[2][i] and board[2][i] == board[4][i]:
            game_over = True
            print(f"{current_player} Wins!")
            return

    # Diagonal
    if board[0][0] == board[2][2] and board[2][2] == board[4][4] and board[0][0] != ' ' or \
       board[0][4] == board[2][2] and board[2][2] == board[4][0] and board[0][4] != ' ':
        game_over = True
        print(f"{current_player} Wins!")
        return

def check_draw():
    '''
    Checks if the board is full and there is no winner.
    If the game ends in a draw, sets game_over to True and prints a message.
    '''
    global game_over
    if game_over:
        return
    else:
        for i in range(5):
            for j in range(5):
                if board[i][j] == ' ':
                    return
    game_over = True
    print("Draw!")

@margin_top_bottom
def ask_restart():
    '''
    Prompts the user to choose whether to restart the game or quit.
    Accepts 'y' for yes or 'n' for no. Clears the board if restarting.
    Provides visual spacing around messages using margin_top_bottom.
    '''
    global game_over
    choice = input("Do you want to play again? Type 'y' for yes or 'n' for no : ").lower()
    if choice == 'n':
        print("================================")
        print("Thank you for playing this game.\nHave a Great DAY!")
        print("================================")
        return
    elif choice == 'y':
        game_over = False
    else:
        print("Please enter valid input. Either 'y' or 'n' ")
        ask_restart()
    for i in range(5):
        for j in range(5):
            if board[i][j] == PLAYER1 or board[i][j] == PLAYER2:
                board[i][j] = ' '
    display_board()

while not game_over:
    print("----------")
    print(f"{current_player}'s Turn : ")
    print("----------")
    try:
        row = int(input("Enter row : "))
        col = int(input("Enter column : "))
        if row % 2 == 0 and col % 2 == 0:
            if board[row][col] == ' ':
                board[row][col] = current_player
                display_board()
                check_winner()
                check_draw()
                current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1
                if game_over:
                    ask_restart()
            else:
                print("This place is already taken by your opponent. Enter another")
        else:
            print("Please enter valid row or column (only even numbers are allowed).")
    except ValueError as e:
        print(f"Please enter valid input : {e}")
    except IndexError:
        print("Out of bounds! Valid values are 0, 2, or 4 for both row and column.")
