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

    # the moves in order to reach the end
    moves_left = []
    moves_right = []

    # right-moving frontier, starting from left
    frontier_left = set()
    frontier_left.add(start)

    # left-moving frontier, starting from right
    frontier_right = set()
    frontier_right.add(end)

    # distance moved from the origins
    depth = {}
    depth[start] = 0
    depth[end] = 0

    # parent of the respective config
    parent = {}
    parent[start] = None
    parent[end] = None

    # to track depth
    i = 1

    while len(frontier_left) > 0 or len(frontier_right) > 0:
        if len(frontier_left) > len(frontier_right):
            frontier_left, frontier_right = frontier_right, frontier_left
            moves_left, moves_right = moves_right, moves_left

        new_frontier = set()
        new_moves = []
        for move in moves_left:
            #

        i += 1

        # perm_inverse -> get the parent of the config?


    # if left and right frontiers have config in common, shortest path found
    if len(frontier_left & frontier_right) > 0:
        moves = []
        for move in moves_left:
            moves.append(move)
        for move in moves_right.reverse:
            moves.append(move)
        return moves


def bfs(s, adj):
    depth = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while len(frontier) > 0:
        search = []
        for u in frontier:
            for v in adj[u]:
                if v not in depth:
                    depth[v] = i
                    parent[v] = u
                    search.append(v)
        frontier = search
        i += 1
