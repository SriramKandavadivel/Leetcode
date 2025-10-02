class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        c_a = sum(aliceSizes)
        c_b = sum(bobSizes)
        aliceSizes.sort()
        bobSizes.sort()
        A = set(aliceSizes)
        B = set(bobSizes)

        split = (c_a - c_b) // 2
        for b in B:
            if split + b in A:
                return [split+b , b]
        