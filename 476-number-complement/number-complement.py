class Solution:
    def findComplement(self, num: int) -> int:
        bi = bin(num)
        # print(bi)  -> 0b101 for 5

        bi = bi[2:]
        # print(int(bi,2))
        n = list(str(bi))

        for i,x in enumerate(n):
            if x == '0':
                n[i] = '1'
            else:
                n[i] = '0'
        m = "".join(n)
        print(m)
        return int(m,2)