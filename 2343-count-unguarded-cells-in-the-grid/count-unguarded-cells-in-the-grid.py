class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr = [[-1 for i in range(n)] for j in range(m)]
        d = [ [-1,0], [0,-1], [1,0], [0,1]]

        def cover(i,j):

            for k in range(i+1,m): #down
                if arr[k][j] == 'g' or arr[k][j] == 'w':
                    break
                else:
                    arr[k][j] = 0
            for k in range(i-1,-1,-1):  #upward
                if arr[k][j] == 'g' or arr[k][j] == 'w':
                    break
                else:
                    arr[k][j] = 0
            for k in range(j+1,n): #right
                if arr[i][k] == 'g' or arr[i][k] == 'w':
                    break
                else:
                    arr[i][k] = 0
            for k in range(j-1,-1,-1):  #upward
                if arr[i][k] == 'g' or arr[i][k] == 'w':
                    break
                else:
                    arr[i][k] = 0

        for x in walls:
            i,j = x[0], x[1]
            arr[i][j] = 'w'
        
        q = deque()
        for y in guards:
            i,j = y[0],y[1]
            arr[i][j] = 'g'
            q.append((i,j))
        
        while q:
            nx,ny = q.popleft()
            cover(nx,ny)
        cnt = 0
        for c in arr:
            for v in c:
                if v == -1:
                    cnt += 1
        
        return cnt

        
            