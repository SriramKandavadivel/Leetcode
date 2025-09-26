class Solution:
    def reverseDegree(self, s: str) -> int:
        # print(ord('z')-ord('a'))  #// 25
        deg = 0
        for idx,lett in enumerate(s):
            print(ord('z')-ord('a'))
            val = (idx+1) * (ord('z') - ord(lett) + 1)
            deg += val
        return deg