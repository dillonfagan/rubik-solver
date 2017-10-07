import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    # if the start and end configs are the same, return empty list
    if start == end:
        return []

    # right-moving frontier, starting from left
    frontier_left = set() # invariant - initialization
    frontier_left.add(start)

    # left-moving frontier, starting from right
    frontier_right = set() # invariant - initialization
    frontier_right.add(end)

    # distance moved from the origins
    dist = {} # invariant - initialization
    dist[start] = 0 # invariant - initialization
    dist[end] = 0 # invariant - initialization

    # parent of the respective config
    left_prev = {} # invariant - initialization
    right_prev = {} # invariant - initialization

    left_prev[start] = None # invariant - initialization
    right_prev[end] = None # invariant - initialization

    left_path = {} # invariant - initialization
    right_path = {} # invariant - initialization
    # path[(position, neighbor)] = the move

    def return_shortest_path():
        moves = [] # invariant - initialization
        target = None # invariant - initialization
        for n in (frontier_left & frontier_right):
            target = n

        while left_prev[target]:
            move = left_path[(left_prev[target], target)]
            moves.append(move)
            target = left_prev[target]

        for n in (frontier_left & frontier_right):
            target = n

        reverse_moves = [] # invariant - initialization
        while right_prev[target]:
            move = right_path[(right_prev[target], target)]
            reverse_moves.append(move)
            target = right_prev[target]

        for move in reverse_moves[::-1]:
            moves.append(move)

        return moves # invariant - termination

    # to track depth
    i = 1 # invariant - initialization

    # to flip between left and right
    left = False # invariant - initialization
    while True:
        # if true, there is no solution
        if i > 7:
            return None

        left = not left

        frontier = set() # invariant - initialization

        # for each cube state in the frontier...
        for position in frontier:

            # if left and right frontiers have config in common, shortest path found
            if position in frontier_left and position in frontier_right:
                return return_shortest_path()

            # for each possible move from the position...
            for move in rubik.quarter_twists:
                # get the next state given a move
                neighbor = rubik.perm_apply(move, position) # invariant - initialization

                if neighbor not in frontier_left or neighbor not in frontier_right:
                    frontier.add(neighbor)
                    dist[neighbor] = i

                    if left:
                        left_path[(position, neighbor)] = move
                        left_prev[neighbor] = position
                    else:
                        right_path[(position, neighbor)] = move
                        right_prev[neighbor] = position

        if left:
            frontier_left = frontier
        else:
            frontier_right = frontier
            # increment depth
            i += 1  # invariant - maintenance
