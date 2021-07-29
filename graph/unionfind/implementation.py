class DisjointSets:
    def __init__(self, n, cnt):
        self.n = n
        self.parents = [i for i in range(n)] # start all elements to own parent
        self.ranks = [1] * n
        self.cnt = cnt

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x]) # path compression
        return self.parents[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x == p_y:
            return

        if self.ranks[p_x] > self.ranks[p_y]: # union by rank
            self.parents[p_y] = p_x
        else:
            self.parents[p_x] = p_y
            if self.ranks[p_x] == self.ranks[p_y]:
                self.ranks[p_y] += 1
        
        self.cnt -= 1


if __name__ == '__main__':
    grid = [
        ["1","1","0","1","0"],
        ["1","1","0","1","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    n = len(grid)
    m = len(grid[0])
    start_count = len(list(filter(lambda x: x == '1', [e for row in grid for e in row])))
    ds = DisjointSets(n * m, start_count)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                for neighbor in [(0,-1), (-1,0), (0,1), (1,0)]:
                    n_i = i + neighbor[0]
                    n_j = j + neighbor[1]
                    if 0 <= n_i < n and 0 <= n_j < m and grid[n_i][n_j] == '1':
                        ds.union(i*m+j, n_i*m+n_j)
    print(ds.parents)