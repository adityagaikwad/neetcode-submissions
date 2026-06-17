class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        DFS
        O(E + V) for time and space
        '''
        # in a fully connected tree, num vertices = num edges - 1
        # in a fully connected tree + 1 edge, num vertices = num edges
        numVertices = len(edges)
        # 1 indexed vertices
        adjencyList = [[] for _ in range(numVertices + 1)]
        visited = set()

        for u, v in edges:
            adjencyList[u].append(v)
            adjencyList[v].append(u)
        
        visited = set()
        cycle = set()
        cycleStart = -1

        # return if cycle is detected
        def dfs(node, parent):
            nonlocal cycleStart

            if node in visited:
                cycleStart = node
                return True

            visited.add(node)

            for neighbor in adjencyList[node]:
                # avoid fake cycle detection
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    
                    # during backtracking if we find cycleStart again,
                    # stop backtracking
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            
            return False
        
        # find all cycle nodes
        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        
        return []
                
        '''
        Union find. When we first do not do union, it means
        the parents are already the same. i.e its a cycle

        the first time add that edge, its a tree, second time we
        add it, its a cycle, return that edge (latest edge by default)

        O(E + V) for time and space
        '''
        # def find(node):
        #     # IMP
        #     curr = parent[node]
        #     # till we don't find the root of the component
        #     while curr != parent[curr]:
        #         # path compression to avoid recursive checks
        #         # in the future finds
        #         parent[curr] = parent[parent[curr]]
        #         curr = parent[curr]

        #     return curr
        
        # def union(n1, n2):
        #     parent1, parent2 = find(n1), find(n2)

        #     # if the parents are the same, no need to merge
        #     if parent1 == parent2:
        #         return False

        #     # merge n2 into n1
        #     if rank[parent1] > rank[parent2]:
        #         '''
        #         IMP: node2's parent's parent is now node1
        #         '''
        #         parent[parent2] = parent1
        #         # increase rank of parent1 by parent2 rank since we did union of two components
        #         rank[parent1] += rank[parent2]
        #     else:
        #         parent[parent1] = parent2
        #         rank[parent2] += rank[parent1]
            
        #     return True
        
        # # in a fully connected tree, num vertices = num edges - 1
        # # in a fully connected tree + 1 edge, num vertices = num edges
        # numVertices = len(edges)

        # # 1 indexed vertices
        # parent = [i for i in range(numVertices + 1)]
        # rank = [1 for _ in range(numVertices + 1)]

        # for n1, n2 in edges:
        #     if not union(n1, n2):
        #         return [n1, n2]
        
        # return []