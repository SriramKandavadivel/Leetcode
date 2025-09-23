class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        a = x+k-1
        mid = x + k//2
        c_bou = y+k
        while x <= mid and a >= mid:
            b = y
            while b < c_bou:
                # print(grid[x][b], grid[a][b])
                grid[x][b], grid[a][b] = grid[a][b], grid[x][b]
                b += 1
            x += 1
            a -= 1
        
        # print(grid)
        return grid