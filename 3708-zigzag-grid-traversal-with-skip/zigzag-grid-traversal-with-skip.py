class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid), len(grid[0])
        row,col = 0,0
        # i,j = 0,0
        l_to_r = 1
        ans = []
        while row < m:
            if l_to_r:
                while col < n:
                    ans.append(grid[row][col])
                    col += 2
                if col == n:
                    col = n-1
                elif col == n+1: #or col > n
                    col = n-2
                l_to_r = 0
            else:
                while col >= 0:
                    # print(ans,row,col)
                    ans.append( grid[row][col] )
                    col -= 2
                if col == -1:
                    col = 0
                elif col == -2:  #or col < -1
                    col = 1
                l_to_r = 1
            row += 1
        print(ans)
        return ans