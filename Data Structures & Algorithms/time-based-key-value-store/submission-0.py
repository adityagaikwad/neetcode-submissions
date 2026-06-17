from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.datastore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.datastore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.datastore[key]) - 1
        res = ""
        while l <= r:
            mid = l + (r - l)//2

            if self.datastore[key][mid][0] <= timestamp:
                # since we need most recent value <= timestamp
                res = self.datastore[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
