class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def rec(num):
            if num > n:
                return
            ans.append(num) 
            for i in range(10):
                number = num*10 + i
                if number > n:
                    break
                # ans.append(number)
                rec(number)
            
            return
        
        for i in range(1,10):
            rec(i)

        return ans