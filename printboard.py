def print_board(board_to_print):
    print(board_to_print[0] + '|' + board_to_print[1] + '|' + board_to_print[2]  )
    print('-----')
    print(board_to_print[3] + '|' + board_to_print[4] + '|' + board_to_print[5]  )
    print('-----')
    print(board_to_print[6] + '|' + board_to_print[7] + '|' + board_to_print[8] + '\n')

#The '\n' at the end of the last print statement is causing a blank line to print so there is space between the bottom
#of the board and the tie or win text message that will eventually print