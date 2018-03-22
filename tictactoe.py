board = [' ',
         ' ',
         ' ',
         ' ',
         ' ',
         ' ',
         ' ',
         ' ',
         ' ']


def print_board():
    print(' {} | {} | {}'.format(board[0], board[1], board[2]))
    print('-----------')
    print(' {} | {} | {}'.format(board[3], board[4], board[5]))
    print('-----------')
    print(' {} | {} | {}'.format(board[6], board[7], board[8]))


def update_board(target):
    if target == "1":
        board[0] = 'X'
    elif target == '2':
        board[1] = 'X'
    elif target == '3':
        board[2] = 'X'
    elif target == '4':
        board[3] = 'X'
    elif target == '5':
        board[4] = 'X'
    elif target == '6':
        board[5] = 'X'
    elif target == '7':
        board[6] = 'X'
    elif target == '8':
        board[7] = 'X'
    elif target == '9':
        board[8] = 'X'


print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()
target = input("Where do you want to go? ")
update_board(target)

print_board()

