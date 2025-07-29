class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        ##find factors of l
        factors = []
        i = 1
        
        while i*i <= l:
            if l%i == 0:
                if i*i == l:
                    factors.append(i)
                else:
                    factors.append(i)
                    factors.append(l//i)
            i+=1
        n = len(factors)
        print(factors)
        i = 0
        while i < n:
            if factors[i] == l:
                i+=1
                continue
        
            sub_str = s[:factors[i]]
            # x = factors[i]+1
            flag = True
            for j in range(factors[i],l,factors[i]):
                if sub_str != s[j:j+factors[i]]:
                    flag = False
                    break
            if flag:
                print(sub_str)
                return True
            i += 1
        return False
                