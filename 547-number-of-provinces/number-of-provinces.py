class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = set()
        cnt = 0

        def dfs(node):
            vis.add(node)
            l = len(isConnected[node-1])
            for i in range(l):
                if isConnected[node-1][i] == 1 and i+1 not in vis:
                    dfs(i+1)


        for node in range(1,n+1):
            if node not in vis:
                cnt += 1
                dfs(node)
        
        return cnt 