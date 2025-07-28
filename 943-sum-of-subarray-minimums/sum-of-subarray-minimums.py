class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        next_sm = [n] * n
        prev_sme = [-1]* n
        """
        
        
        """
        st1 = []
        for i in range(n):
            while st1 and arr[st1[-1]] > arr[i]:
                next_sm[st1[-1]] = i
                st1.pop()
            prev_sme[i] = st1[-1] if st1 else -1
            st1.append(i)
        tot = 0
        for i in range(n):
            left = i-prev_sme[i]
            right = next_sm[i]-i
            print(left,right)
            tot += left*right*arr[i]
        MOD = 10**9 +7
        return (tot)%MOD