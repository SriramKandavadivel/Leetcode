class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def rec(rows):
            if rows == 0:
                return []
            if rows == 1:
                return [[1]]
            
            new_row = [1]

            res = rec(rows-1)
            last_row = res[-1]
            for i in range(len(last_row)-1):
                num = last_row[i]+last_row[i+1]
                new_row.append(num)
            new_row.append(1)
            res.append(new_row)

            return res
        return rec(numRows)