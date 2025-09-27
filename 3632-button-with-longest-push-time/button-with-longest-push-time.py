class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        d = collections.defaultdict(lambda : 0)
        n = len(events)
        max_ = events[0][0]
        for i,x in enumerate(events):
            if i == 0:
                d[x[0]] = x[1]
                diff = x[1]
            else:
                idx = x[0]
                prev = events[i-1]
                diff = x[1] - prev[1]
                d[x[0]] = max( d[x[0]], diff)
            if diff == d[max_]:
                if x[0] < max_:
                    max_ = x[0]
            elif diff > d[max_]:
                max_ = x[0]

        return max_