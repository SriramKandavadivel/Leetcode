class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        # print(l)
        ans = ""
        n = len(l)
        for i in range(n-1,-1,-1):
            ans += l[i] + " "
        return ans[:-1]