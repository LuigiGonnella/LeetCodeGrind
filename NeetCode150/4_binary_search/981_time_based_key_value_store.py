class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
            
    def get(self, key: str, timestamp: int) -> str:
        if len(self.time_map[key]) == 0 or timestamp < self.time_map[key][0][0]:
            return ""

        if timestamp >= self.time_map[key][-1][0]:
            return self.time_map[key][-1][1]

        def searchR(l: int, r: int) -> str:

            lastRes = self.time_map[key][0][1]
            
            while l <= r:
                m = l + (r - l) // 2
                if timestamp >= self.time_map[key][m][0]:
                    lastRes = self.time_map[key][m][1]
                    l = m + 1
                else:
                    r = m - 1
            return lastRes
        
        return searchR(1, len(self.time_map[key]) - 2)

        
                
                


        
