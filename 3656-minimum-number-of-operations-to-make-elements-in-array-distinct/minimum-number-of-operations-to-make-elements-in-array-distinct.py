class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        # traverse from reverse and find the first point where the duplicate appears
        s = set()
        idx = -1
        for i in range(n-1,-1,-1):
            if nums[i] in s:
                idx = i
                break
            else:
                s.add(nums[i])

        dup_arr_len = idx+1
        print(dup_arr_len)
        op = dup_arr_len//3 + (1 if dup_arr_len % 3 != 0 else 0)
        return op