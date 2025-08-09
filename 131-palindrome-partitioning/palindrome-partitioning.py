class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        l = []
        def rec(idx):
            if idx == n:
                ans.append(list(l))
                return

            for i in range(idx,n):
                if isPal(idx,i):
                    l.append(s[idx:i+1])
                    rec(i+1)
                    l.pop()
            return ans
                
        def isPal(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        return rec(0)