"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

# board = [[" "," "," "," "," "," "," "," "],
#          [" "," "," "," "," "," "," "," "],
#          [" "," "," "," "," "," "," "," "],
#          [" "," "," "," "," "," "," "," "],
#          [" "," "," "," "," "," "," "," "],
#          [" "," "," "," "," "," "," "," "],
#          [" "," "," "," "," "," "," "," "],
#          [" "," "," "," "," "," "," "," "]]

#%%
def is_empty(board):
    for row in board:
        if ('b' in row) or ('w' in row):
            return False
    return True

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True



def is_in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    # Determining start and end bound positions
    start_bound_pos = ( y_end - (length * d_y), x_end - (length * d_x) )
    end_bound_pos = ( y_end + d_y, x_end + d_x )
    max_pos = len(board) - 1

    # Checking if start of sequence is bounded:
    if (is_in_range(start_bound_pos[0], 0, max_pos) and is_in_range(start_bound_pos[1], 0, max_pos)) and (board[start_bound_pos[0]][start_bound_pos[1]] == ' '):
        start_open = True
    else:
        start_open = False

    # Checking if end of sequence is bounded:
    if (is_in_range(end_bound_pos[0], 0, max_pos) and is_in_range(end_bound_pos[1], 0, max_pos)) and (board[end_bound_pos[0]][end_bound_pos[1]] == ' '):
        end_open = True
    else:
        end_open = False
    
    # Open, semiopen, or closed?:
    if start_open and end_open:
        return 'OPEN'
    elif start_open or end_open:
        return 'SEMIOPEN'
    return 'CLOSED'


    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    max_pos = len(board) - 1
    len_cur_seq = 0
    open_seq_count = 0
    semi_open_seq_count = 0
    y, x = y_start, x_start
    while is_in_range(y, 0, max_pos) and is_in_range(x, 0, max_pos):
        if board[y][x] == col:
            len_cur_seq += 1
            if not(is_in_range(y+d_y, 0, max_pos) and is_in_range(x+d_x, 0, max_pos)):
                if len_cur_seq == length:
                    bound_state = is_bounded(board, y, x, length, d_y, d_x)
                    if bound_state == 'OPEN':
                        open_seq_count += 1
                    elif bound_state == 'SEMIOPEN':
                        semi_open_seq_count += 1
        else:
            if len_cur_seq == length:
                bound_state = is_bounded(board, y-d_y, x-d_x, length, d_y, d_x)
                if bound_state == 'OPEN':
                    open_seq_count += 1
                elif bound_state == 'SEMIOPEN':
                    semi_open_seq_count += 1
            len_cur_seq = 0
        y += d_y
        x += d_x
    return open_seq_count, semi_open_seq_count




def detect_rows(board, col, length):
    max_pos = len(board) - 1
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(max_pos + 1):
        # Checking left to right (0, 1):
        new_seq_counts = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count, semi_open_seq_count = (open_seq_count + new_seq_counts[0]) , (semi_open_seq_count + new_seq_counts[1])

        # Checking top to bottom (1, 0):
        new_seq_counts = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count, semi_open_seq_count = (open_seq_count + new_seq_counts[0]) , (semi_open_seq_count + new_seq_counts[1])

        # Checking upper left to bottom right (1, 1) (top to bottom):
        new_seq_counts = detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count, semi_open_seq_count = (open_seq_count + new_seq_counts[0]) , (semi_open_seq_count + new_seq_counts[1])
        # Checking upper right to bottom left (1, -1) (left to right):
        new_seq_counts = detect_row(board, col, 0, i, length, 1, -1)
        open_seq_count, semi_open_seq_count = (open_seq_count + new_seq_counts[0]) , (semi_open_seq_count + new_seq_counts[1])
        if i != 0:
            # Checking upper left to bottom right (1, 1) (left to right):
            new_seq_counts = detect_row(board, col, 0, i, length, 1, 1)
            open_seq_count, semi_open_seq_count = (open_seq_count + new_seq_counts[0]) , (semi_open_seq_count + new_seq_counts[1])
            # Checking upper right to bottom left (1, -1) (top to bottom):
            new_seq_counts = detect_row(board, col, i, max_pos, length, 1, -1)
            open_seq_count, semi_open_seq_count = (open_seq_count + new_seq_counts[0]) , (semi_open_seq_count + new_seq_counts[1])
    return open_seq_count, semi_open_seq_count




def search_max(board):
    board_size = len(board)
    high_score = -100000
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == ' ':
                board[i][j] = 'b'
                board_score = score(board)
                if board_score > high_score:
                    move_y, move_x = i, j
                    high_score = board_score
                board[i][j] = ' '
    return move_y, move_x



def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])



# FOR DETECTING 5 IN A ROW FOR WINS
def seq_in_row(board, col, y_start, x_start, length, d_y, d_x):
    max_pos = len(board) - 1
    len_cur_seq = 0
    y, x = y_start, x_start
    while is_in_range(y, 0, max_pos) and is_in_range(x, 0, max_pos):
        if board[y][x] == col:
            len_cur_seq += 1
            if not(is_in_range(y+d_y, 0, max_pos) and is_in_range(x+d_x, 0, max_pos)):
                if len_cur_seq == length:
                    return True
        else:
            if len_cur_seq == length:
                return True
            len_cur_seq = 0
        y += d_y
        x += d_x
    return False

def seq_in_rows(board, col, length):
    max_pos = len(board) - 1
    for i in range(max_pos + 1):
        # Checking left to right (0, 1):
        if seq_in_row(board, col, i, 0, length, 0, 1):
            return True
        # Checking top to bottom (1, 0):
        if seq_in_row(board, col, 0, i, length, 1, 0):
            return True
        # Checking upper left to bottom right (1, 1):
        if seq_in_row(board, col, i, 0, length, 1, 1) or seq_in_row(board, col, 0, i, length, 1, 1):
            return True
        # Checking upper right to bottom left (1, -1):
        if seq_in_row(board, col, 0, i, length, 1, -1) or seq_in_row(board, col, i, max_pos, length, 1, -1):
            return True
    return False
    
def is_win(board):
    if seq_in_rows(board, 'w', 5):
        return 'White won'
    elif seq_in_rows(board, 'b', 5):
        return 'Black won'
    else:
        if is_full(board):
            return 'Draw'
        else:
            return 'Continue playing'


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


#%%
            
if __name__ == '__main__':
    play_gomoku(8)

# %%
