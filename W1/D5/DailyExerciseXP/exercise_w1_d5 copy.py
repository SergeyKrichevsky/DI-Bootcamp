# Mini-Project - Tic Tac Tpo (Крестики - Нолики)

# What to create:
# A command-line Tic Tac Toe game that allows two players to take turns 
#   marking a 3x3 grid.
# Tic Tac Toe is played on a 3x3 grid. 
# Players take turns marking empty squares with their symbol (‘O’ or ‘X’). 
# The first player to get three of their symbols in a row 
# (horizontally, vertically, or diagonally) wins. 
# If all squares are filled and no player has three in a row, 
# the game is a tie.

# Element ti create:

# Step 1: Representing the Game Board

# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

def greeting():
    '''greeting()'''
    print("+" + "-" * 48 + "+")
    print("|{:^48}|".format("TOE TAC TOE"))
    print("|{:^48}|".format("Game"))
    print("|{:^48}|".format(" "))
    # print("|{:^48}|".format("presented by"))
    print("|{:^48}|".format("SERGEY KRICHEVSKY"))
    print("|{:^48}|".format("Entertainment"))
    print("|{:^48}|".format(" "))
    print("|{:^48}|".format("Lets Start!"))
    # print("|{:^48}|".format("production"))
    print("+" + "-" * 48 + "+")
# greeting()

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

# ==> for testing:
test_board = [['a','b','c'],
              ['d','e','f'],
              ['g','h','y']]
# ==<

player_1 = {'player N': 1,'name': '', 'symbol': 'X'}
player_2 = {'player N': 2,'name': '', 'symbol': 'O'}


# ==> for testing:
# player_1['name'] = 'Test Name 1'
# player_2['name'] = 'Test Name 2'
# print(player_1['name'])
# print(player_2['name'])
# ==<

def name_player(player):
    '''name_player(player)'''
    if not player['name']:
        player['name'] = input(f'\nYou are player {player['player N']}. What is your name? ')

# name_player(player_1)
# name_player(player_2)
# print(player_1['name'])
# print(player_2['name'])


# Step 2: Displaying the Game Board

# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.

def display_board():
    '''display_board()'''
    for row in board:
        print(f"[{row[0]}]", f"[{row[1]}]", f"[{row[2]}]")

# display_board()


# Step 3: Getting Player Input

# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.


# Creating Visual instruction for user - how to adress to the right position:
positions_instructions = [['1','2','3'],
                          ['4','5','6'],
                          ['7','8','9']]

def show_positions_instructions():
    '''show_positions_instructions()'''
    print('\nThis is the current status of the board: ')
    display_board()
    # print()
    print('These are the position numbers: ')
    for row in positions_instructions:
        print(f"[{row[0]}]", f"[{row[1]}]", f"[{row[2]}]")
    # print()
# show_positions_instructions()


# function to translate user`s input into adress on the board:

def board_adress_indexes(position_input):
    '''board_adress_indexes(position_input) 
       - Output Format: "(0, 0)"'''
    if position_input == 1:
        return (0, 0)
    elif position_input == 2:
        return (0, 1)
    elif position_input == 3:
        return (0, 2)
    elif position_input == 4:
        return (1, 0)
    elif position_input == 5:
        return (1, 1)
    elif position_input == 6:
        return (1, 2)
    elif position_input == 7:
        return (2, 0)
    elif position_input == 8:
        return (2, 1)
    elif position_input == 9:
        return (2, 2)
    else:
        print("Invalid Position Number")
    

# Previous version - 
# (Turned out not working with "update_board(player, position_num)" Function)
# (But works with "empty_position(adress)" Function)
def board_adress(position_input):
    '''board_adress(position_input)
       - Output Format: "board[0][0]"'''
    if position_input == 1:
        return board[0][0]
    elif position_input == 2:
        return board[0][1]
    elif position_input == 3:
        return board[0][2]
    elif position_input == 4:
        return board[1][0]
    elif position_input == 5:
        return board[1][1]
    elif position_input == 6:
        return board[1][2]
    elif position_input == 7:
        return board[2][0]
    elif position_input == 8:
        return board[2][1]
    elif position_input == 9:
        return board[2][2]
    
def update_board(player, position_num):
    '''update_board(player, position_num)'''
    row, col = board_adress_indexes(position_num)
    board[row][col] = player['symbol']
# update_board(player_2, 1)
# display_board()

def empty_position(adress):
    '''empty_position(adress)'''
    if adress == ' ':
        return True
    else:
        return False

# print(empty_position(board_adress(1)))
# print(empty_position(board_adress(0)))

# update_board(player_1, 5)
# display_board()
# print(empty_position(board_adress(5)))

def get_valid_input(player):
    '''get_valid_input(player)'''
    check = False
    while not check:
        show_positions_instructions() #Displays all information player needs
        player_choise = input(f'{player['name']} ,You are playing with {player['symbol']}`s ==> Which position you want to play now (1-9)? \n')
        if player_choise.isdigit():
            player_choise = int(player_choise)
            if 0 < player_choise < 10:
                if empty_position(board_adress(player_choise)):
                    check = True
                    return player_choise
                else:
                    # print()
                    print('\nPosition is Taken! Choose another one')
            else: 
                print("=" * 50) 
                print("*" * 50)
                print("\nNot a valid position number! ")
        else:
            print("=" * 50)
            print("*" * 50)
            print("\nEnter valid position number! ")

# print(get_valid_input(player_1))
# get_valid_input(player_1)
# a = empty_position(board_adress(5))
# print(a)
    

# BackUp:
# def get_valid_input(player):
#     check = False
#     while not check:
#         show_positions_instructions() #Displays all information player needs
#         player_choise = input(f'{player['name']} You are playing with {player['symbol']}`s ==> Which position you want to play now (1-9)? \n')
#         if player_choise.isdigit():
#             player_choise = int(player_choise)
#             if 0 < player_choise < 10:
#                 check = True
#                 return player_choise
#             else: 
#                 print()  
#                 print("Not a valid position number! ")
#         else:
#             print()
#             print("Enter valid position number! ")


def player_input(player):
    '''player_input(player)
       return position (number)'''
    name_player(player) #Only ones askes each player # - Better to get it outside the loop (and add to "greeting") to save computer power. Leaving here for now to do mandatory assingments first.
    position = get_valid_input(player)
    return position
# print(player_input(player_1))


# Step 4: Checking for a Winner
# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

def all_equal(line):
    '''all_equal(line)'''
    return len(set(line)) == 1 and line[0] != ' '
# test_line = ["X", "X", "X",]
# test_line = ["O", "O", "O",]
# test_line = ["X", "O", "X",]
# print(all_equal(test_line))

# def check_win(board, player):
#     '''check_win(board, player):'''
def check_win(player):
    '''check_win(player):'''
    if all_equal([board[0][0], board[0][1],board[0][2]]) and board[0][0] ==  player['symbol']:
        return True
    elif all_equal([board[1][0], board[1][1],board[1][2]]) and board[1][0] ==  player['symbol']:
        return True
    elif all_equal([board[2][0], board[2][1],board[2][2]]) and board[2][0] ==  player['symbol']:
        return True
    elif all_equal([board[0][0], board[1][0],board[2][0]]) and board[0][0] ==  player['symbol']:
        return True
    elif all_equal([board[0][1], board[1][1],board[2][1]]) and board[0][1] ==  player['symbol']:
        return True
    elif all_equal([board[0][2], board[1][2],board[2][2]]) and board[0][2] ==  player['symbol']:
        return True
    elif all_equal([board[0][0], board[1][1],board[2][2]]) and board[0][0] ==  player['symbol']:
        return True
    elif all_equal([board[0][2], board[1][1],board[2][0]]) and board[0][2] ==  player['symbol']:
        return True
    else:
        return False
    

# def check_win(player):
#     '''check_win(player):'''
#     if all_equal([board[0][0], board[0][1],board[0][2]]):
#         return True
#     elif all_equal([board[1][0], board[1][1],board[1][2]]):
#         return True
#     elif all_equal([board[2][0], board[2][1],board[2][2]]):
#         return True
#     elif all_equal([board[0][0], board[1][0],board[2][0]]):
#         return True
#     elif all_equal([board[0][1], board[1][1],board[2][1]]):
#         return True
#     elif all_equal([board[0][2], board[1][2],board[2][2]]):
#         return True
#     elif all_equal([board[0][0], board[1][1],board[2][2]]):
#         return True
#     elif all_equal([board[0][2], board[1][1],board[2][0]]):
#         return True
#     else:
#         return False
    

# Step 5: Checking for a Tie
# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

def full_board():
    '''full_board()'''
    if ' ' in board[0]:
        return False
    elif ' ' in board[1]:
        return False
    elif ' ' in board[2]:
        return False
    else:
        return True
# print(full_board(test_board))

def check_tie():
    '''check_tie()'''
    if full_board():
        if not check_win(player_1) and not check_win(player_2):
            return True
        else:
            return False
    else:
        return False
# print(check_tie())


# Step 6: The Main Game Loop
# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def switch_player(current_player):
    '''switch_player(current_playerr)
       returns the adress for other player'''
    if current_player == player_1:
        return  player_2
    else:
        return player_1


def game_ower():
    '''game_ower()'''
    if full_board() or check_win(player_1) or check_win(player_2):
        return True

# def game_ower(board):
#     '''game_ower(board)'''
#     return full_board()

def play():
    '''play()'''
    greeting()
    current_player = player_2
    while not game_ower():
        current_player = switch_player(current_player)
        move_psition = player_input(current_player)
        update_board(current_player, move_psition)
    if check_tie():
        display_board()
        print('It`s Tie. Thank you for playing our games \U00002665 !')
    elif check_win(player_1):
        display_board()
        print(f'\n{player_1['name']} Wins. Thank you for playing our games! \U00002665\n')
    else:
        display_board()
        print(f'\n{player_2['name']} Wins. Thank you for playing our games! \U00002665\n')




# board = [[' ',' ',' '],
#          [' ',' ',' '],
#          [' ',' ',' ']]
play()



# '''greeting()'''
# '''update_board(player, position_num)'''
# '''player_input(player)
#         return position (number)'''
# '''check_win(player):'''
# '''check_tie()'''