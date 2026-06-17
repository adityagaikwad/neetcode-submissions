from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Time complexity: O(m+n)
            n be the number of courses and
            m be the size of prerequisites
            Initializing the adj list takes O(m) time as we go through all the edges. The indegree array take O(n) time.
            Each queue operation takes O(1) time, and a single node will be pushed once, leading to O(n) operations for n nodes. We iterate over the neighbors of each node that is popped out of the queue iterating over all the edges once. Since there are total of m edges, it would take O(m) time to iterate over the edges.    
        Space complexity: O(m+n)
            The adj arrays takes O(m) space. The indegree array takes O(n) space.
            The queue can have no more than n elements in the worst-case scenario.
            It would take up O(n) space in that case.
        '''
        graph = defaultdict(list)
        indegrees = {course: 0 for course in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        queue = deque()
        for course, indegree in indegrees.items():
            if indegree == 0:
                queue.append(course)
        
        nodesVisited = 0
        while queue:
            course = queue.popleft()
            nodesVisited += 1

            # subtract 1 from course's neighbor nodes indegrees
            # since we visited it
            for neighbor in graph[course]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return nodesVisited == numCourses