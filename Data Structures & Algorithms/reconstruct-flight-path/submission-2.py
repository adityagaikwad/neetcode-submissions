class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        Time complexity: O(N log N)
            Let N be the number of tickets. Sorting the tickets in reverse order takes O(N log N) time.
            Processing each ticket using the stack takes O(N) time.
            Space complexity: O(N)
        Space: O(N)
            For graph and stack
        '''
        # Create a graph represented as a dictionary where each airport is a key, and its destinations are values.
        graph = collections.defaultdict(list)

        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        # Initialize the stack with the starting airport "JFK" and an empty itinerary.
        stack = ["JFK"]
        new_itinerary = []

        while stack:
            curr = stack[-1]
            # If there are destinations from the current airport, add the next destination to the stack.
            if graph[curr]:
                stack.append(graph[curr].pop())
            else:
                # When there are no more destinations, add the current airport to the new itinerary.
                new_itinerary.append(stack.pop())

        # Reverse the new itinerary to get the correct order.
        return new_itinerary[::-1]

        '''
        Time: O(E * V)
            For each edge we explore every vertex
            Worst case its completely connected
        Space: O(E * V)
            Worst case stack goes to every vertex twice
        '''
        
        # sort by source, dest so that when we add to adj list
        # the lexicographically smaller one is added to list first
        # tickets.sort()
        # adj = {src: [] for src, dest in tickets}
        
        # # populate adjcency list
        # for src, dest in tickets:
        #     adj[src].append(dest)

        # def dfs(src):
        #     # +1 coz tickets is src, dest so res will be + 1
        #     if len(res) == len(tickets) + 1:
        #         return True
            
        #     # i.e there is no outbound flight from src
        #     # so this path is wrong, backtrack
        #     if src not in adj:
        #         return False

        #     # we are going to pop from actual adj list so make a copy
        #     temp = list(adj[src])
        #     # visit all dests from src and find valid path
        #     for i, dest in enumerate(temp):
        #         # remove dest by idx marking it visited
        #         adj[src].pop(i)
        #         # add dest as next hop
        #         res.append(dest)

        #         # if we find a valid path from dest hop then return True
        #         if dfs(dest):
        #             return True
                
        #         # if no valid path, remove dest as hop and go to next dest of src
        #         adj[src].insert(i, dest)
        #         # since we are backtracking, remove dest from curr res
        #         res.pop()
            
        #     # if we do not get a valid path after visiting all the possible dests from src, return False
        #     return False
        
        # # Add JFK to res and start graph exploration
        # res = ["JFK"]
        # dfs("JFK")

        # return res