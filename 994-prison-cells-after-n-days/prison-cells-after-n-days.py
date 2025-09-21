class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # l = len(cells)
        c = [0]*8
        # for i in range(n):
        for i in range(1, 7):
            if cells[i-1] == cells[i+1]:
                c[i] = 1
            else:
                c[i] = 0
        # print(c)
        cells = list(c)
        n = (n-1)%14
        for i in range(n):
            for j in range(1,7):                  #[0,0,1,0,1,0,1,0]
                if cells[j-1] == cells[j+1]:
                    c[j] = 1
                else:
                    c[j] = 0
            cells = list(c)
        return cells
        
