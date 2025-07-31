class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque([])  ##ind,type,minute
        oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([(i,j),0])
                if grid[i][j] == 1:
                    oranges += 1
        di = [(0,1),(1,0),(0,-1),(-1,0)]  ## 4 directions
        time = 0
        rotten = 0
        while q and oranges > 0:
            ind,t = q.popleft()
            rotten+=1
            for d in di:
                x= ind[0]+d[0]  ##index in each direction
                y= ind[1]+d[1]
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1:
                        oranges -= 1
                        grid[x][y] = 2
                        q.append([(x,y),t+1])
                        time = max(time,t+1)
            print(t)
        
        return time if oranges == 0 else -1
                