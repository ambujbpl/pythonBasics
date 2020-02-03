# All Global Variable is here:-)
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_still_in_progress = True

winner = None;

current_player = "X";

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def play_game():
    # display 1
    # initial board
    # display_board()
    while game_still_in_progress:
        take_user_input()
        flip_players()
        winner = check_if_game_over()
    if winner == "X" or winner == "O":
        print(winner + ' won the match.');
    else:
        print('Match Tie');
    return
def take_user_input():
    print(current_player + " 's turn now")
    position = int(input("chose any position from 1 to 9 :- ")) -1;
    while position not in [0,1,2,3,4,5,6,7,8]:
        position = int(input("Position : " + str(position + 1) + " is not valid input. So please chose any position from 1 to 9 :- ")) -1;
    while board[position] != '-':
        position = int(input("Position : " + str(
            position + 1) + " is already filled. So please chose new position from 1 to 9 :- ")) - 1;
    if(current_player == "X"):
        board[position] = "X"
    else:
        board[position] = "O"
    display_board()
    return

def check_if_game_over():
    win = check_if_win()
    check_if_tie()
    return win
def check_if_win():
    global game_still_in_progress
    global current_player
    # check rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if(row_1 or row_2 or row_3):
        game_still_in_progress = False
        if row_3:
            return board[6]
        elif row_2:
            return board[3]
        elif row_1:
            return board[0]
    # check columns
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if(col_1 or col_2 or col_3):
        game_still_in_progress = False
        if col_3:
            return board[2]
        elif col_2:
            return board[1]
        elif col_1:
            return board[0]
    # check Diagonals
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[6] == board[4] == board[2] != "-"
    if(dia_1 or dia_2):
        game_still_in_progress = False
        if dia_1:
            return board[0]
        elif dia_2:
            return board[2]
    return

def check_if_tie():
    global game_still_in_progress
    if '-' not in board:
        game_still_in_progress = False
    return

def flip_players():
    global current_player
    if(current_player == "X"):
        current_player = "O";
    else:
        current_player = "X";
    return
#display_board()
play_game()