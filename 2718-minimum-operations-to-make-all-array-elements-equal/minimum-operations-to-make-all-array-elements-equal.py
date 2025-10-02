class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        '''
        a b c d e
        if c is centre
        c -a +c-b + 
        d-c +e-c 


        c -a +c-b + 
        d-c +e-c +1

        a b c d  ---> b : centre -> cost = b-a +c-b + d-b = -a +c +d-b
                      c : centre -> cozt = c-a + c-b + d-c = c-a -b+d

        '''
        nums.sort()
        n =  len(nums)
        m = len(queries)
        # print(nums)
        # ans = []
        # for x in queries:
        #     idx = (bisect.bisect_right(nums, x) -1 )    # lesser or equal to
        #     if idx < 0:
        #         idx = 0
        #     # print(idx)
        #     val = 0
        #     for i in range(idx):
        #         val += abs( nums[idx]-nums[i] ) + ( x-nums[idx] )
        #     # print(val)

        #     for i in range(idx+1, n):
        #         val += abs( nums[i]-nums[idx] ) + ( nums[idx]-x )
        #     val += abs( nums[idx]-x )
        #     ans.append(val)
        
        # return ans

        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        ans = []
        for x in queries:
            idx = bisect.bisect_left(nums, x)
            if idx > 0:
                prev = -1 * prefix[idx-1] 
                prev_count = idx
                prev += prev_count * (x )
            else:
                prev = 0
            print(prev)
            
            if idx <= n-1:
                next_ = prefix[n-1] - ( prefix[idx-1] if idx > 0 else 0)
                next_count = n - (idx  if idx < n else 0)
                next_ += next_count * (-x )
            else:
                next_ = 0

            val = prev + next_
            # val += x - (nums[idx] if 0 <= idx < n else 0)
            
            ans.append(val)
        
        return ans