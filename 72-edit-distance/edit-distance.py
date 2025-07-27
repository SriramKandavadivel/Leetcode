class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        INF = 10**20
        @cache
        def rec(i,j):
            if i == n and j == m:
                return 0
            if j == m:
                return n-i
            if i == n:
                return m-j
            cnt = INF
            if i < n and j < m and word1[i] == word2[j]:
                cnt = min(cnt,rec(i+1,j+1))
            if i < n and j < m and word1[i] != word2[j]:
                cnt = min(cnt, 1+rec(i+1,j+1))
                cnt = min(cnt, 1+rec(i+1,j))
                cnt = min(cnt, 1+rec(i,j+1))
            return cnt
        return rec(0,0)