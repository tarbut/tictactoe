def game_over(current_board):

    from printboard import print_board

    def letter_won(letter):
        print_board(current_board)
        print('')
        print(letter + ' won')
        return True

#check if O has won
    if current_board[0]==current_board[1] and current_board[1]==current_board[2] and current_board[0]=='O':
        return letter_won(current_board[0])
    elif current_board[3]==current_board[4] and current_board[4]==current_board[5] and current_board[3]=='O':
        return letter_won(current_board[3])
    elif current_board[6]==current_board[7] and current_board[7]==current_board[8] and current_board[6]=='O':
        return letter_won(current_board[6])



    elif current_board[0]==current_board[3] and current_board[3]==current_board[6] and current_board[0]=='O':
        return letter_won(current_board[0])
    elif current_board[1]==current_board[4] and current_board[4]==current_board[7] and current_board[1]=='O':
        return letter_won(current_board[1])
    elif current_board[2]==current_board[5] and current_board[5]==current_board[8] and current_board[2]=='O':
        return letter_won(current_board[2])


    elif current_board[0]==current_board[4] and current_board[4]==current_board[8] and current_board[0]=='O':
        return letter_won(current_board[0])
    elif current_board[2]==current_board[4] and current_board[4]==current_board[6] and current_board[2]=='O':
        return letter_won(current_board[2])




#check if X has won
    elif current_board[0] == current_board[1] and current_board[1] == current_board[2] and current_board[0] == 'X':
        return letter_won(current_board[0])
    elif current_board[3] == current_board[4] and current_board[4] == current_board[5] and current_board[3] == 'X':
        return letter_won(current_board[3])
    elif current_board[6] == current_board[7] and current_board[7] == current_board[8] and current_board[6] == 'X':
        return letter_won(current_board[6])



    elif current_board[0] == current_board[3] and current_board[3] == current_board[6] and current_board[0] == 'X':
        return letter_won(current_board[0])
    elif current_board[1] == current_board[4] and current_board[4] == current_board[7] and current_board[1] == 'X':
        return letter_won(current_board[1])
    elif current_board[2] == current_board[5] and current_board[5] == current_board[8] and current_board[2] == 'X':
        return letter_won(current_board[2])


    elif current_board[0] == current_board[4] and current_board[4] == current_board[8] and current_board[0] == 'X':
        return letter_won(current_board[0])
    elif current_board[2] == current_board[4] and current_board[4] == current_board[6] and current_board[2] == 'X':
        return letter_won(current_board[2])

#check if it is a tie...
#Note that current_board[0:9] is itself a list made up of the first 9 entries of current_board
#In other words current_board[0:9] returns the board list from positions zero to eight... which is nine positions
#(here, we don't care about the tenth position, which is in slot 9, because that is reserved for the "never" business)
    elif ' ' not in current_board[0:9]:
        print_board(current_board)
        print('')
        print('It is a tie')
        return True

    else:
        return False