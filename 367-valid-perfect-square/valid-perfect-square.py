class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = sqrt(num)
        # print(num)
        return n == floor(n)