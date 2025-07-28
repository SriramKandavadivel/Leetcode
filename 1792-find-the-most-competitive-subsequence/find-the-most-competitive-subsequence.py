class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        st = []
        
        for i in range(n):
            while st and st[-1] > nums[i] and len(st)+(n-i) > k:
                st.pop()
            st.append(nums[i])
        while len(st) > k:
            st.pop()
        return st