class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = 1
        bob = 0
        prev = 10
        while n >= 0:
            if alice:
                if n >= prev:
                    n -=  prev
                    prev -= 1
                    alice = 0
                else:
                    return False
            elif not alice:
                if n >= prev:
                    n -= prev
                    prev -= 1
                    alice = 1
                else:
                    return True
        return True
