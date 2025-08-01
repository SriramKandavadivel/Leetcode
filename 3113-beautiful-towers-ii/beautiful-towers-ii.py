class Solution:
    def maximumSumOfHeights(self, h: List[int]) -> int:
        n = len(h)
        left = [0]*n
        st = [-1]
        curr = 0
        for i in range(n):
            while len(st) > 1 and h[st[-1]] > h[i]:
                j = st.pop()
                curr -= (j-st[-1])*h[j]
            curr += (i-st[-1])*h[i]
            st.append(i)
            left[i] = curr
        print(left)
        right = [0]*n
        st = [n]
        curr = 0
        res = 0
        for i in range(n-1,-1,-1):
            while len(st) > 1 and h[st[-1]] > h[i]:
                j = st.pop()
                curr -= (st[-1]-j)*h[j]
            curr+= (st[-1]-i)*h[i]
            st.append(i)
            right[i] = curr
            res = max(res,(left[i]+right[i]-h[i]))
            
        print(right)
        return res