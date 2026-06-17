from collections import Counter
from heapq import heapify, heappush, heappop

'''
Use maxheap to process the task with highest count first, so that we can
process most of these tasks with the least idle time. We continue processing
other tasks till say task X is waiting and so on.

Add all task counts to maxHeap

Then use a deque (nextAvailableTimes) to add to (queue to wait for n, count left)
time for task X same with other tasks, once processed add to queue
since we need to wait n time

We do this till all tasks from heap are processed once. Then, we check queue
and jump ahead to time when we can start processing first task from queue.

Add it to maxHeap to process.

Time: O(t)
    t is the number of tasks
    task-processing iterations: exactly t (one per task)
    idle-jump iterations: at most t (at most one jump between consecutive tasks)

Space: O(1) since only 26 chars so lens are const
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
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
            if maxHeap:
                # process the task in 1 unit of time
                currTime += 1
                # reduce count by 1 since we are processing one task
                negCount = 1 + heappop(maxHeap)
                if negCount != 0:
                    restTaskUntil = currTime + n
                    nextAvailableTimes.append((restTaskUntil, negCount))                
            else:
                # if maxHeap doesn't exist we skip to next time a task has finished cooldown
                currTime = nextAvailableTimes[0][0]
 
            # i.e the task can now be processed
            # NOTE: We will end up adding only one coz only one will
            # have lowest cooldown due to single task processing
            if nextAvailableTimes and nextAvailableTimes[0][0] <= currTime:
                restTaskUntil, negCount = nextAvailableTimes.popleft()
                heappush(maxHeap, negCount)

        return currTime
