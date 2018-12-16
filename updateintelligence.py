
from writetobucket import write_to_bucket

def update_intelligence(received_cluster, previously_played, board_now, row_that_won):
    #previously_play == 'O' means O just won
    if previously_played == 'O':
        #set to 'A' for always the move 'O' for the board with each of the
        #'O's removed, one at a time, from the winning row (so 'O' is played
        #in the winning position
        for i in row_that_won:
            board_now[i] = ' '
            write_to_bucket(received_cluster, board_now, 'A', i)
            board_now[i] = 'O'




    #previously_play == 'X' means X just won
    if previously_played == 'X':
        #set to 'N' for never every possible O move that could come before any
        #one of the Xs in the winning row
        for i in row_that_won:
            board_now[i] = ' '
            #iterate through the board and set each O to a never
            position = 0
            for j in board_now:
                if j == 'O':
                    board_now[position] = ' '
                    write_to_bucket(received_cluster, board_now, 'N', position)
                    board_now[position] = 'O'
                position += 1
            board_now[i] = 'X'
