from collections import defaultdict

'''
Hashmap key = key, value = list((timestamp, value))
Value has ascending order of timestamps
Use binary search to get prev_timestamp <= timestamp

Time:
    Set - O(1)
    Get - O(log n)
        n = total values for a key
Space:
    O(n * m)
        m = total number of keys
'''
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # values list sorted ascending by timestamp
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        # binary search on values list
        valuesList = self.hashmap[key]
        n = len(valuesList)
        left = 0
        right = n - 1

        res = ""
        # need largest storedTimestamp <= timestamp
        while left <= right:
            mid = left + (right - left)//2

            # if mid is lower than required, mid can be one ans
            # set res and set left = mid + 1 to check for larger ts <= required
            if valuesList[mid][0] <= timestamp:
                res = valuesList[mid][1]
                left = mid + 1
            # mid is greater than required, right = mid - 1
            else:
                right = mid - 1
        
        return res
        
