#importing to main.py all of the functions that we wrote for main.py to use
from startdatabase import start_database
from databasequery import database_query
from writetobucket import write_to_bucket
from gameover import game_over
from makemove import make_move

#starting the database
cluster = start_database()

board = [' '] * 10
previous_play = ' '

#keeps randomly generating moves until the game is over
while True:
    previous_play, board = make_move(previous_play, board)
    # add a document to the bucket containing the current board
    write_to_bucket(cluster, board)
    if game_over(board):
        break



#querying the database
#database_query(cluster, board_as_a_string)


