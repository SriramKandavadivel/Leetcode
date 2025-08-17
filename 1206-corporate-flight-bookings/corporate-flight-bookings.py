class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        1        2        3         4         5  -->index

        10               -10

                20                 -20
                25       
                           
    --->10      55        45        25        25
        '''
        m = len(bookings)
        ans = [0]* n

        for i in range(m):
            st,end = bookings[i][0], bookings[i][1]
            ans[st-1] += bookings[i][2]
            if end < n:
                ans[end] -= bookings[i][2]
        for j in range(1,n):
            ans[j] += ans[j-1]
        return ans
