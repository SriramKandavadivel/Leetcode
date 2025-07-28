class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        mono = []

        for i in range(n):
            while mono and mono[-1] > nums[i] and len(mono)+(n-i) > k:
                mono.pop()
            mono.append(nums[i])

        while len(mono) > k:
            mono.pop()
        return mono