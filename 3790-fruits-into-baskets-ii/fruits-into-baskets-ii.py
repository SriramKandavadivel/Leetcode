class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        d = collections.defaultdict(lambda : 0)
        # baskets.sort()
        cnt = 0
        for i,y in enumerate(fruits):
            for j,z in enumerate(baskets):
                if y <= z:
                    fruits[i] = -1
                    baskets[j] = -1
                    break
        
        for x in fruits:
            if x != -1:
                cnt += 1
        return cnt