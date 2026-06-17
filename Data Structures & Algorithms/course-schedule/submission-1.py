'''
Topological Sort (BFS / Kahn's Algorithm)
To find a valid order in a DAG to iterate all nodes/vertices

Time complexity: O(V + E)
    V = number of courses, E = number of prerequisite pairs
    Building the adjacency list/graph takes O(E)
    Building the indegree array takes O(V)
    Each node is enqueued and dequeued at most once: O(V) queue operations
    Each edge is visited once when we decrement neighbor indegrees: O(E)
    Total: O(V + E)

Space complexity: O(V + E)
    Adjacency list stores all edges: O(E)
    Indegree array and queue each store at most V entries: O(V)
    Total: O(V + E)
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # key = node, val = list of neighbor nodes
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