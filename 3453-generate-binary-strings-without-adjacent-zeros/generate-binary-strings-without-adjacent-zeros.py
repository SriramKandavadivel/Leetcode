class Solution:
    def validStrings(self, n: int) -> List[str]:
        l = ['0','1']
        ans = set()

        def rec(comb,prev):
            if len(comb) == n:
                ans.add(comb)
                return
        
            ##take
            for i in range(2):
                if prev == '1' or l[i] == '1':
                    comb += l[i]
                    rec(comb,l[i])
                    comb = comb[:-1]
            
            return ans
        
        return list( rec("", '1') )
            
                