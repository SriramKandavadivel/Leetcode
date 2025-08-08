class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def rec(idx):
            if idx == n:
                return 1
            cnt = 0
            if s[idx] != '0':
                if idx+1 < n and int(s[idx:idx+2]) <= 26:
                        # print("...")
                    cnt += rec(idx+2)
                # if s[idx] == '0':
                #     return 0
                cnt += rec(idx+1)

            return cnt
        return rec(0)