class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        d  = {5:0, 10:0, 20:0}
        in_hand = 0
        for x in bills:
            if x == 5:
                d[5] += 1
                in_hand += 5
            elif x == 10:
                if d[5] == 0:
                    return False
                d[5] -= 1
                d[10] += 1
                in_hand += 5
            elif x == 20:
                if in_hand < 15:
                    return False
                elif d[5] >= 1 and d[10] >= 1:
                    d[5] -= 1
                    d[10] -= 1
                    d[20] += 1
                    in_hand += 5
                elif d[5] >= 3:
                    d[5] -= 3
                    d[20] += 1
                    in_hand += 5
            
                else:
                    return False
        return True