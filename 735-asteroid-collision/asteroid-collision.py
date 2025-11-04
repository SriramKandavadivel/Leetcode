class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        # st.append(asteroids[0])
        for x in asteroids:
            if st and x < 0 and st[-1] > 0:
            # while st and x < 0:
                while st and st[-1] > 0 and st[-1] < abs(x):
                    st.pop()
                if st and st[-1] > abs(x):
                    continue
                elif st and st[-1] == abs(x):
                    st.pop()
                else:
                    st.append(x)
            else:
                st.append(x)
            print(st)
        return st
        