class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        n,m = len(g),len(s)
        cnt = 0
        j = 0
        for i in range(n):
            while  j < m and s[j] < g[i]:
                j += 1
            if j<m and s[j] >= s[i]:
                cnt += 1
                j +=1
        return cnt 
             