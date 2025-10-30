class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)

        d = sorted(d, key = lambda x: (-d[x]) )
        print(d)
        return d[:k]