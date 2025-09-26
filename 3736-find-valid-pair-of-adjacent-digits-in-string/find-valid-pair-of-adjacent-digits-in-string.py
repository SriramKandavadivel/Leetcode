class Solution:
    def findValidPair(self, s: str) -> str:
        l = list(s)
        d = Counter(l)
        n = len(l)
        for i in range(1,n):
            if s[i] != s[i-1]:
                if d[s[i-1]] == int(s[i-1]) and d[s[i]] == int(s[i]):
                    return s[i-1 : i+1]
        return ""