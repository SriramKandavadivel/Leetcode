class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(values)
        vis = set()
        i = 0
        score = 0
        while 0 <= i < n and i not in vis:
            vis.add(i)
            if instructions[i] == 'jump':
                i = i+ values[i]
            else:
                score += values[i]
                i += 1
        return score