import heapq


def a_star(grid, start, goal, simple_bfs=False):
    def h(s, e):
        if simple_bfs:
            return 0
        return abs(e[0]-s[0]) + abs(e[1]-s[1])

    pq = [(0, 0, start)]
    # if you're tracking state, like obstacles removed, which allows you to get
    # to same square from different choices, then you cannot simply avoid
    # repeating squares.  This is where A* becomes more efficient.
    # A* == BFS when not repeating visited squares (look at <steps> var)
    # visited = set([start])
    steps = 0
    while pq:
        est_dist, cur_dist, cur_loc = heapq.heappop(pq)
        steps += 1
        if cur_loc == goal:
            return cur_dist, steps

        for d_r, d_c in [(1,0),(-1,0),(0,1),(0,-1)]:
            row = cur_loc[0] + d_r
            col = cur_loc[1] + d_c
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]) \
            and grid[row][col] == 0:
            # and (row,col) not in visited:
                # visited.add((row,col))
                heapq.heappush(pq, (cur_dist+h((row,col),goal), cur_dist+1, (row,col)))

    return -1, steps


if __name__ == "__main__":
    grid = [
        [0,0,0,0,1,0],
        [0,0,0,0,0,0],
        [0,0,1,1,1,0],
        [0,1,0,0,0,1],
        [0,0,0,1,0,0],
        [0,1,0,1,0,0],
    ]

    goal_row, goal_col = len(grid)-1, len(grid[-1])-1
    a_star_dist, a_star_steps = a_star(grid, (0,0), (goal_row, goal_col), False)
    bfs_dist, bfs_steps = a_star(grid, (0,0), (goal_row, goal_col), True)

    # if heuristic is admissible (never overestimates cost)
    assert a_star_dist == bfs_dist == 12

    assert a_star_steps < bfs_steps