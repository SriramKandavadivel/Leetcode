class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        tot = 0
        for i in range(n-1,-1,-3):
            tot += cost[i] + (cost[i-1]  if i-1 >= 0 else 0)
        return tot