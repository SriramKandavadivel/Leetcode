class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        cmax = cmin = 0
        for x in s:
            if x == '(':
                cmin += 1
                cmax += 1
            elif x == ')':
                cmin = max(cmin -1 , 0)
                cmax -= 1
            elif x == '*':
                cmax += 1
                cmin = max(cmin -1 , 0)
            if cmax < 0:
                return False
        return cmin == 0

            