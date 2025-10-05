class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        m,n = len(arr1),len(arr2)

        class Node:
            def __init__(self):
                self.children = [None] * 10
        
        root = Node()    
        def insert(string):
            curr = root
            k = len(string)

            for x in string:
                idx = ord(x) - ord('0')
                # print(idx,curr.children[idx])
                if not curr.children[idx] :
                    curr.children[idx] = Node()
                # print("after",idx,curr.children[idx])
                curr = curr.children[idx]

        def search(string):
            curr = root
            cnt = 0
            # print("search")
            for x in string:
                idx = ord(x) - ord('0')
                # print(idx,curr.children[idx])
                if not curr.children[idx]:
                    break
                curr = curr.children[idx]
                cnt += 1
            # print("cnt",cnt)
            return cnt
        
        for num in arr1:
            insert(str(num))
        
        res = 0
        for num in arr2:
            res = max(res, search(str(num)))

        return res