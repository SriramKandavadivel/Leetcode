class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        
        m,n = len(board), len(board[0])
        vis = set()
        d = [ (0,-1), (-1,0), (0,1), (1,0)]

        def dfs(x,y):
            
            vis.add( (x,y) )
            for c in d:
                nx = c[0] + x
                ny = c[1] + y
                if 0 <=  nx < m and 0 <= ny < n and board[nx][ny] == 'O' and (nx,ny) not in vis:
                    dfs( nx,ny )
            
            return 

        for i in range(m):
            if board[i][0] == 'O' and (i,0) not in vis:
                dfs(i,0)
            if board[i][n-1] == 'O' and (i,n-1) not in vis:
                dfs(i,n-1)
        
        for j in range(n):
            if board[0][j] == 'O' and (0,j) not in vis:
                dfs(0,j)
            if board[m-1][j] == 'O' and (m-1,j) not in vis:
                dfs(m-1,j)



        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in vis:
                    board[i][j] = 'X'
