class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hash_map.get(key, [])

        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res
    