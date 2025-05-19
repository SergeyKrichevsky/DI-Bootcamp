# Tra end excrpt block

hello = 'Hello world'

if hello == 'Hello world':
    print('Thats right')

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

def player_input(current_player):
    valid = False
    while not valid:
        position = input('enter position 1-9: ')
        try:
            position = int(position) - 1
            if 0 <= position < 9 and board[position] == ' ':
                board[position] = current_player
                print(board)
                valid = True   
            else:
                print('position not in the range')
        except:
            print('pleace enter a number')
            continue

player_input('X')


