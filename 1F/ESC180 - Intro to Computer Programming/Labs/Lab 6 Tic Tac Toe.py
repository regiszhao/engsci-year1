'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''
#%%
import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    

def which_square(square_num):
    row = (square_num - 1) // 3
    column = (square_num - 1) % 3
    coord = [row, column]
    return (coord)


def put_in_board(board, mark, square_num):
    coord = which_square(square_num)
    board[coord[0]][coord[1]] = mark
    return board


def get_free_squares(board):
    free_squares = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                free_squares.append([i, j])
    return free_squares


def make_random_move(board, mark):
    free_squares = get_free_squares(board)
    coord = free_squares[random.randint(0, len(free_squares) - 1)]
    board[coord[0]][coord[1]] = mark
    return board


def is_row_all_marks(board, row_i, mark):
    for entry in board[row_i]:
        if entry != mark:
            return False
    return True


def is_col_all_marks(board, col_i, mark):
    for row in board:
        if row[col_i] != mark:
            return False
    return True
    

def is_win(board, mark):
    is_diag1_all_marks = True
    is_diag2_all_marks = True
    for i in range(len(board)):
        if board[i][i] != mark:
            is_diag1_all_marks = False
        if board[i][len(board)-1-i] != mark:
            is_diag2_all_marks = False
        if is_row_all_marks(board, i, mark) or is_col_all_marks(board, i, mark):
            return True
    return is_diag1_all_marks or is_diag2_all_marks


def make_move(board, mark):
    if mark == 'X':
        opp_mark = '0'
    else:
        opp_mark = 'X'
    opp_winning_squares = []
    for free_square in get_free_squares(board):
        board[free_square[0]][free_square[1]] = mark
        if is_win(board, mark):
            return
        board[free_square[0]][free_square[1]] = opp_mark
        if is_win(board, opp_mark):
            opp_winning_squares.append(free_square)
        board[free_square[0]][free_square[1]] = ' '

    if len(opp_winning_squares) > 0:
        board[opp_winning_squares[0][0]][opp_winning_squares[0][1]] = mark
    else:
        make_random_move(board, mark)
    return board
    

    

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)
    print("\n\n")

# PROBELM 1 - USER VS USER
    # turn = 'X'
    # while True:
    #     move = int(input('Enter your move: '))
    #     if move == -1:
    #         break
    #     put_in_board(board, turn, move)
    #     print_board_and_legend(board)
    #     print("\n\n")
    #     if turn == 'X':
    #         turn = '0'
    #     else:
    #         turn = 'X'
    # print('game ended.')

# COMPUTER VS USER
    # turn = 'X'
    # while len(get_free_squares(board)) > 0:
    #     if turn == 'X':
    #         make_move(board, 'X')
    #         print("computer's move:")
    #         print_board_and_legend(board)
    #         if is_win(board, 'X'):
    #             print('computer wins.')
    #             break
    #         turn = '0'
    #     else:
    #         move = int(input('Enter your move: '))
    #         put_in_board(board, turn, move)
    #         print("user's move:")
    #         print_board_and_legend(board)
    #         if is_win(board, '0'):
    #             print('user wins.')
    #             break
    #         turn = 'X'
    #     print("\n\n")
    
    # if not(is_win(board, 'X') or is_win(board, '0')):
    #     print('draw.')

# %%
