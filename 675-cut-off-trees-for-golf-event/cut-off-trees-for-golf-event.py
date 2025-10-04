class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m,n = len(forest),len(forest[0])
        d = [ [0,1], [1,0], [0,-1], [-1,0]]
        l = []
        for i,x in enumerate(forest):
            for j,y in enumerate(x):
                if y > 1:
                    l.append( (y,i,j) )
        l.append((-1,0,0))
        l.sort()

        def bfs(sx,sy, ex,ey):
            q = deque()
            q.append( (sx,sy) )
            vis = set()
            lvl = 0  #no. of steps from current tree to next greater tree
            while q:
                z = len(q)
                # print(q)
                while z > 0:
                    i,j = q.popleft()
                    if i == ex and j == ey:
                        return lvl
                    if (i,j) in vis:
                        z -= 1
                        continue
                    vis.add((i,j))
                    # tree = forest[i][j]
                    for x in d:
                        nx = i+x[0]
                        ny = j+x[1]
                        
                        if 0 <= nx < m and 0 <= ny < n:
                            if forest[nx][ny] != 0 and forest[nx][ny] not in vis:
                                q.append((nx,ny))
                    z -= 1
                lvl += 1
            return -1  #no path to next greater element
            
        ans = 0
        for idx,(val,x,y) in enumerate(l[:-1]):
            steps = bfs(x,y, l[idx+1][1], l[idx+1][2] )
            if steps == -1:
                return -1
            ans += steps
        
        return ans