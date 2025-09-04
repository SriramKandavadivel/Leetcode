class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        INF = 10**20
        # ans = [[ INF for i in range(n)]for j in range(m)]
        # dire = [ [0,-1], [-1,0], [0,1], [1,0] ]
        # q = deque()
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == 0:
        #             ans[i][j] = 0
        #         else:
        #             q.append([i,j,0])
        #             while q:
        #                 idx = q.popleft()
        #                 if mat[ idx[0] ][ idx[1] ] == 0:
        #                     ans[i][j] = idx[2]
        #                     break
        #                 for z in dire:
        #                     nx = idx[0]+ z[0] 
        #                     ny = idx[1]+ z[1]
        #                     if 0 <= nx < m and 0 <= ny < n:
        #                         q.append([nx,ny,idx[2]+1])
        #             q.clear()

        # return ans
        q = deque()
        dire = [ (1,0), (0,1), (-1,0), (0,-1)]
        ans = [[-1]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for a,b in dire:
                nx = a+x
                ny = b+y
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    ans[nx][ny] = 1+ ans[x][y]
                    q.append((nx,ny))
        return ans