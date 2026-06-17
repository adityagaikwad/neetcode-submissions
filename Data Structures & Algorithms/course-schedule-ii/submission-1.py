'''
Recursive DFS (post-order topological sort)

Build an adjacency list mapping each course to the courses that depend on it.
Run post-order DFS from every unvisited node: a node is appended to sorted_order
only after all of its dependents have been fully explored, so reversing the list
at the end yields a valid topological ordering where prerequisites come first.
The active set tracks nodes on the current recursion stack. Encountering a
neighbor that is already active means there is a back edge, i.e. a cycle, making
completion impossible.

Time: O(V + E)
    Each node and each edge is visited exactly once across all DFS calls
Space: O(V + E)
    graph stores all E edges; visited and active each hold up to V entries;
    call stack depth is at most V in the worst case (a single prerequisite chain)
'''
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         sorted_order = []

#         if numCourses <= 0:
#             return sorted_order

#         # i is the start of the edge and the array contains it's neighbors
#         # aka end of the edge
#         graph = {i: [] for i in range(numCourses)}

#         # build the DAG
#         for course, prereq in prerequisites:
#             graph[prereq].append(course) # adding edge from prereq -> course

#         visited = set()
#         active = set()

#         self.isCycle = False

#         def dfs(vertex: int) -> None:
#             visited.add(vertex)
#             # active denotes the current vertex's recursion stack nodes
#             # it's used to find cycles in the graph
#             active.add(vertex)

#             for neighbor in graph[vertex]:
#                 if neighbor not in visited:
#                     dfs(neighbor)
#                 elif neighbor in active:
#                     self.isCycle = True
#                     break

#             sorted_order.append(vertex)
#             active.remove(vertex)
        
#         for course in range(numCourses):
#             if course not in visited:
#                 dfs(course)
        
#         # since we added the last course first due to recursion,
#         # we reverse the order before returning
#         return sorted_order[::-1] if not self.isCycle else []

'''
Topological Sort using Kahn's BFS algorithm

Track how many prerequisites each course still needs via in_degree. Seed a queue
with every course whose in_degree is zero, meaning it has no remaining prerequisites
and can be taken immediately. Each time a course is dequeued, decrement the
in_degree of all courses that depend on it. When a dependent's in_degree drops to
zero, it becomes available and is added to the queue. If a cycle exists, some nodes
will never reach in_degree zero and will be absent from sorted_order, which is
detected by checking the final list length against numCourses.

Time: O(V + E)
    Each node is enqueued and dequeued once; each edge is processed once when
    its source node is dequeued
Space: O(V + E)
    graph stores all E edges; in_degree and sources each hold at most V entries
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 0:
            return []

        # in_degree[i] = number of prerequisites course i still needs
        in_degree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        sorted_order = []

        # start with courses that have no prerequisites
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)

            for child in graph[vertex]:
                in_degree[child] -= 1

                # this child's last prerequisite was just completed; it is now available
                if in_degree[child] == 0:
                    sources.append(child)

        # nodes stuck in a cycle never reach in_degree 0 and are excluded from sorted_order
        if len(sorted_order) != numCourses:
            return []

        return sorted_order