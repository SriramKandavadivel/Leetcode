class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        pgee = [-1]*n
        nge = [n]*n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                nge[st.pop()] =  i
                
            st.append(i)
        print(nge)
        st = []
        for j in range(n-1,-1,-1):
            while st and nums[st[-1]] <= nums[j]:
                pgee[st.pop()] = j
            st.append(j)
        print(pgee)
        st = []
        psee = [-1]*n
        nse = [n]*n
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                nse[st.pop()] = i
            st.append(i)
        print(nse)
        st = []
        for j in range(n-1,-1,-1):
            while st and nums[st[-1]] >= nums[j]:
                psee[st.pop()] = j
            st.append(j)
        print(psee)
        max_val = 0
        for i in range(n):
            r = nge[i] - i
            l = i-pgee[i]
            val = l*r*nums[i]
            max_val += val
        min_val = 0
        for i in range(n):
            r = nse[i] -i
            l = i-psee[i]
            val = l*r*nums[i]
            min_val += val
        return (max_val)-(min_val)