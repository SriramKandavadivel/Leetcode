class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = n-1
        ans = 0
        while l <= r:
            m =((l+r)//2)
            if citations[m] >= n-m :
                r=  m-1 
                ans = max(ans,n-m)
            else:
                l = m+1
        return ans

        