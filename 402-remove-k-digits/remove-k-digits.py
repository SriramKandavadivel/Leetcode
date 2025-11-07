class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []
        i = 0
        num = list(num)
        while i < n:
            while st and int(num[i]) < int( st[-1] ) and k > 0:
                
                # print("k",k, st[-1])
                st.pop()
                k -= 1
                
            st.append(num[i])
            # print(i, num[i])
            i += 1
            
        j = len(st)
        while k != 0 and j > 0:
            st.pop()
            j -= 1
            k-=1

        n1 = len(st)
        while st and st[0] == '0':
            st.pop(0)
        res = "".join(st)
        return res if res else '0'