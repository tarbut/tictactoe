def database_query(receiving_cluster, board_as_a_string):
    cb = receiving_cluster.open_bucket('boardwascreated')
    cb.get(board_as_a_string).value


    from couchbase.n1ql import N1QLQuery
    row_iter = cb.n1ql_query(N1QLQuery('SELECT BoardAsString FROM boardwascreated'))

    for row in row_iter: print(row)
