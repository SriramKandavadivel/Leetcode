class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n =  len(matrix), len(matrix[0])
        dire = [[0,-1], [-1, 0], [0,1], [1,0]]
        @cache
        def path(i,j):
            if i < 0 or j < 0:
                return 0
            # if matrix[i][j] > matrix[p_i][p_j]:
            #     return 0
            cnt = 0
            for x in dire:
                nx = i+x[0]
                ny = j+x[1]
                if 0 <= nx < m and 0 <= ny < n :
                    if matrix[nx][ny] > matrix[i][j]:
                        cnt = max(cnt , 1+path(nx,ny))
                        # path(nx,ny)
            return cnt
        res = 0 
        for i in range(m):
            for j in range(n):
                res = max(res,1+ path(i,j))
        return res