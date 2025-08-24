class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # q = deque([])
        h = deque([1])
        # def push(val):
        #     heapq.heappush(h,val)
        # def pop():
        #     heapq.heappop(h)
        ans = 0
        vis = set()
        while len(h) > 0:
            m = len(h)
            while m > 0:
                val = h.popleft()
                if val == n*n:
                    return ans
                if val not in vis:
                    vis.add(val)
                    for next in range(val+1, min(val+6, n*n)+1):
                        row = n-1-((next-1)//n)
                        if ((next-1)//n) % 2 == 1:
                            col = n-1-((next-1) % n)
                        else:
                            col = ((next-1) % n)
                        
                        des = board[row][col] if board[row][col] != -1 else next
                        if des not in vis:
                            h.append(des)

                m -= 1
            ans += 1
        return -1
                
