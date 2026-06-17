from collections import Counter
from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Time: O(n * m)
            m is the idletime worst case we have all A's
            we need to wait m units after every completion
        1. Process max frequency task first
        2. Then increment time
        3. Then add the next available time for that task to a queue
        4. Then while next available time <= current time, pop from queue
           and add to heap
        5. Repeat till heap is empty
        '''
        taskCounts = Counter(tasks)

        maxHeap = [-count for count in taskCounts.values()]
        # O(n * log(26)) = O(n)
        heapify(maxHeap)

        nextAvailableTimes = deque()
        currTime = 0
        while maxHeap or nextAvailableTimes:
            currTime += 1

            if maxHeap:
                # reduce count by 1 since we are processing one task
                negCount = 1 + heappop(maxHeap)
                if negCount != 0:
                    restTaskFor = currTime + n
                    nextAvailableTimes.append((restTaskFor, negCount))                
            else:
                # if maxHeap doesn't exist
                currTime = nextAvailableTimes[0][0]
 
            # i.e the task can now be processed
            # we add only one coz only one will have low cooldown
            if nextAvailableTimes and nextAvailableTimes[0][0] <= currTime:
                restTaskFor, negCount = nextAvailableTimes.popleft()
                heappush(maxHeap, negCount)
        
        return currTime


