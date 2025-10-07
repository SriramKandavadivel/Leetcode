class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # print(int('0010'))
        l1 = version1.split('.')
        l2 = version2.split('.')
        m,n = len(l1),len(l2)

        if m > n:
            k = m-n
            for i in range(k):
                l2.append(0)
        else:
            k = n-m
            for i in range(k):
                l1.append(0)
        print(l1,l2)

        j = 0
        while j < max(m,n):
            print(l1[j],l2[j])
            if int(l1[j]) < int(l2[j]):
                return -1
            elif int(l1[j]) > int(l2[j]):
                return 1
            j += 1
        
        return 0