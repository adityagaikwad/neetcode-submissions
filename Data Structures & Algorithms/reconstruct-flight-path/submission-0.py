class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        Time: O(E * V)
            For each edge we explore every vertex
            Worst case its completely connected
        Space: O(E * V)
            Worst case stack goes to every vertex twice
        '''
        
        # sort by source, dest so that when we add to adj list
        # the lexicographically smaller one is added to list first
        tickets.sort()
        adj = {src: [] for src, dest in tickets}
        
        # populate adjcency list
        for src, dest in tickets:
            adj[src].append(dest)

        def dfs(src):
            # +1 coz tickets is src, dest so res will be + 1
            if len(res) == len(tickets) + 1:
                return True
            
            # i.e there is no outbound flight from src
            # so this path is wrong, backtrack
            if src not in adj:
                return False

            # we are going to pop from actual adj list so make a copy
            temp = list(adj[src])
            # visit all dests from src and find valid path
            for i, dest in enumerate(temp):
                # remove dest by idx marking it visited
                adj[src].pop(i)
                # add dest as next hop
                res.append(dest)

                # if we find a valid path from dest hop then return True
                if dfs(dest):
                    return True
                
                # if no valid path, remove dest as hop and go to next dest of src
                adj[src].insert(i, dest)
                # since we are backtracking, remove dest from curr res
                res.pop()
            
            # if we do not get a valid path after visiting all the possible dests from src, return False
            return False
        
        # Add JFK to res and start graph exploration
        res = ["JFK"]
        dfs("JFK")

        return res