class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 0:
            return sorted_order

        # Store the count of incoming prerequisites in a hashmap
        in_degree = {i: 0 for i in range(numCourses)}

        # i is the start of the edge and the array contains it's neighbors
        # aka end of the edge
        graph = {i: [] for i in range(numCourses)}

        # build the DAG
        for course, prereq in prerequisites:
            graph[prereq].append(course) # adding edge from prereq -> course
            in_degree[course] += 1 # since this course has one prereq

        '''
        Recursive DFS approach
        '''
        visited = set()
        active = set()

        sorted_order = []
        self.isCycle = False

        def dfs(vertex: int) -> None:
            visited.add(vertex)
            # active denotes the current vertex's recursion stack nodes
            # it's used to find cycles in the graph
            active.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in active:
                    self.isCycle = True
                    break

            sorted_order.append(vertex)
            active.remove(vertex)
        
        for course in range(numCourses):
            if course not in visited:
                dfs(course)
        
        # since we added the last course first due to recursion,
        # we reverse the order before returning
        return sorted_order[::-1] if not self.isCycle else []