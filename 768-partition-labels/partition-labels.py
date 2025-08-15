class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        l = [-1] * n
        d = {}
        for i in range(n):
            if s[i] in d:
                idx = d[s[i]]
                l[idx][1] = i
            l[i] = [i,i]
            d[s[i]] = i
        
        l = deque(l)
        # print(l)
        ans = []
        while l:
            if len(l) > 1 and l[1][0] <= l[0][1] <= l[1][1]:
                l[1][0] = l[0][0]
                l.popleft()
            elif len(l) > 1 and l[1][0] <= l[0][1] and l[1][1] <= l[0][1]:
                l[1] = l[0]
                l.popleft()
            else:
                part = l[0][1] - l[0][0] +1
                ans.append(part)
                l.popleft()
        return ans
