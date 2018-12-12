def make_move(previously_played, board_now):

    import random

    if previously_played == ' ':
        play = 'X'
        previously_played = 'X'
    elif previously_played == 'O':
        play = 'X'
        previously_played = 'X'
    elif previously_played == 'X':
        play = 'O'
        previously_played = 'O'

    #create a list named blank_positions that hold all of the positions of board_now that are empty
    j = 0
    blank_positions = []
    for i in board_now:
        if i == ' ':
            blank_positions.append(j)
        j = j + 1

    #randomly select one of the entries of blank_positions
    position_to_update = random.choice(blank_positions)

    #adds the next move to the board
    board_now[position_to_update] = play


    return previously_played, board_now

