class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        if startFuel >= target:
            return 0 
        h = []
        fuel = startFuel
        stn = 0
        i = 0
        while fuel < target:
            while i < n and stations[i][0] <= fuel:
                heapq.heappush(h,-stations[i][1])
                i += 1
            if not h:
                return -1
            val = abs(heapq.heappop(h))
            stn += 1
            fuel += val
        return stn