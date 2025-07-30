class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        nse = [n]*n
        psee = [-1]*n
        st = []
        MOD = 10**9 + 7
        for i in range(n):
            while st and strength[st[-1]] > strength[i]:
                nse[st.pop()] = i
            st.append(i)
        st =[]
        # print(nse)
        for i in range(n-1,-1,-1):
            while st and strength[st[-1]] >= strength[i]:
                psee[st.pop()] = i
            st.append(i)
        # print(psee)
        prefix = [strength[0]]
        for i in range(1,n):
            prefix.append(prefix[-1]+strength[i])
        # print(prefix)
        suffix = [strength[n-1]]
        for j in range(n-2,-1,-1):
            suffix.append(suffix[-1]+strength[j])
        s_suf = [suffix[0]]
        p_pre = [prefix[0]]
        for i in range(1,n):
            p_pre.append(p_pre[-1]+prefix[i])
            s_suf.append(s_suf[-1]+suffix[i])
        # print(p_pre)
        # print(s_suf)
        s_suf.reverse()
        suffix.reverse()

        
        print(s_suf)


        def get_pre(l,r):
            if l>r:
                return 0
            return prefix[r]-(prefix[l-1] if l-1>=0 else 0) 
        def get_pp(l,r):
            if l>r:
                return 0
            return p_pre[r]-(p_pre[l-1] if l-1>=0 else 0)
        def get_suf(l,r):
            if l>r:
                return 0
            return suffix[l]-(suffix[r+1] if r+1<n else 0)
        def get_ss(l,r):
            if l>r:
                return 0
            return s_suf[l]-(s_suf[r+1] if r+1<n else 0)

        ans = 0
        for idx in range(n):
            left = idx-psee[idx]
            right = nse[idx]-idx
            # print(left,right)
            r_val = get_pp(idx,nse[idx]-1)- right*(get_pre(0,idx-1))
            l_val = get_ss(psee[idx]+1,idx-1)- (left-1)*(get_suf(idx,n-1))
            # print(l_val,r_val)
            left_ans = l_val*right
            right_ans = r_val*left

            ans += (strength[idx]*(left_ans+right_ans))
        return ans%MOD