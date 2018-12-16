#importing to main.py all of the functions that we wrote for main.py to use
from startdatabase import start_database
from databasequery import database_query
from writetobucket import write_to_bucket
from gameover import game_over
from makemove import make_move
from updateintelligence import update_intelligence


def print_board(board_to_print):
    print(board_to_print[0] + '|' + board_to_print[1] + '|' + board_to_print[2]  )
    print('-----')
    print(board_to_print[3] + '|' + board_to_print[4] + '|' + board_to_print[5]  )
    print('-----')
    print(board_to_print[6] + '|' + board_to_print[7] + '|' + board_to_print[8] + '\n')


#starting the database
cluster = start_database()




#for i in range(100000):
board = [' '] * 11
previous_play = ' '
#keeps randomly generating moves until the game is over
while True:
    previous_play, board = make_move(previous_play, board)
    # add a document to the bucket containing the current board
    #write_to_bucket(cluster, board, '', '')
    over, the_winning_row, tie = game_over(board)
    if over == 'True':
        if tie != 'yes tie':
            1 == 1
            #update_intelligence(cluster, previous_play, board, the_winning_row)
        break





