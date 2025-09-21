class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        vis = set(nums)
        l = list(vis)
        ans = [0] * k
        l.sort()
        i = len(l) -1
        j = 0
        while k > 0 and i >= 0:
            ans[j] = l[i]
            i -= 1
            j += 1
            k -= 1
        return ans[:j]
