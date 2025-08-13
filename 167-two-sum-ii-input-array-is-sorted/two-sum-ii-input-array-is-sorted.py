class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        d = {}
        for i,val in enumerate(numbers):
            if (target-val) in d:
                return list([d[target-val]+1 , i+1])
            d[val] = i