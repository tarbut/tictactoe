def write_to_bucket(received_cluster, current_board, always_never, position):

    board_with_E_for_empty = ['E' if x == ' ' else x for x in current_board]
    board_with_E_for_empty[9] = always_never
    board_with_E_for_empty[10] = str(position)
    board_as_a_string = ''.join(board_with_E_for_empty)

    cb = received_cluster.open_bucket('boardwascreated')
    cb.upsert(board_as_a_string,
              {'BoardAsString': board_as_a_string})
