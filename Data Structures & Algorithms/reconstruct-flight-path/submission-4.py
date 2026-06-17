'''
Create Adjacency list (from: [to_airport]), sorted in reverse by destination airport
Add JFK to stack and add its neighbors to stack from end .pop() (ascending)

Then add an airport to res only when no outgoing from it aka its the last airport
Do this for all airports when there is no outgoing. Then reverse and return res
Since we went from A to B and then added say B in res, next in stack would be
airport A.

The core insight: a node should be added to the itinerary only after ALL of
its outgoing edges are exhausted. This prevents getting stranded at a dead-end
before visiting the rest of the graph.

Sorting tickets in reverse and using pop() together enforce lexicographic order:
  graph["JFK"] = ["SFO", "ATL"]  (SFO inserted first, ATL inserted second)
  pop() returns "ATL" first, which is lexicographically smaller. Correct.

graph[airport] = list of destination airports, sorted so smallest is last (pop order)

Time: O(N log N)
    Sorting N tickets takes O(N log N); each ticket is pushed and popped exactly
    once from the stack, so the traversal is O(N)
Space: O(N)
    graph stores all N edges; stack also N
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph represented as a dictionary where each airport
        # is a key, and its destinations are values.
        graph = collections.defaultdict(list)

        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        # Initialize the stack with the starting airport "JFK" and
        # an empty itinerary
        stack = ["JFK"]
        new_itinerary = []

        while stack:
            curr = stack[-1]
            # If there are destinations from the current airport,
            # add the next destination to the stack
            if graph[curr]:
                stack.append(graph[curr].pop())
            else:
                # When there are no more destinations,
                # add the current airport to the new itinerary
                new_itinerary.append(stack.pop())

        # Reverse the new itinerary to get the correct order
        return new_itinerary[::-1]

'''
Time: O(E * V)
    For each edge we explore every vertex
    Worst case its completely connected
Space: O(E * V)
    Worst case stack goes to every vertex twice
'''
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:    
#         sort by source, dest so that when we add to adj list
#         the lexicographically smaller one is added to list first
#         tickets.sort()
#         adj = {src: [] for src, dest in tickets}
        
#         # populate adjcency list
#         for src, dest in tickets:
#             adj[src].append(dest)

#         def dfs(src):
#             # +1 coz tickets is src, dest so res will be + 1
#             if len(res) == len(tickets) + 1:
#                 return True
            
#             # i.e there is no outbound flight from src
#             # so this path is wrong, backtrack
#             if src not in adj:
#                 return False

#             # we are going to pop from actual adj list so make a copy
#             temp = list(adj[src])
#             # visit all dests from src and find valid path
#             for i, dest in enumerate(temp):
#                 # remove dest by idx marking it visited
#                 adj[src].pop(i)
#                 # add dest as next hop
#                 res.append(dest)

#                 # if we find a valid path from dest hop then return True
#                 if dfs(dest):
#                     return True
                
#                 # if no valid path, remove dest as hop and go to next dest of src
#                 adj[src].insert(i, dest)
#                 # since we are backtracking, remove dest from curr res
#                 res.pop()
            
#             # if we do not get a valid path after visiting all the possible dests from src, return False
#             return False
        
#         # Add JFK to res and start graph exploration
#         res = ["JFK"]
#         dfs("JFK")

#         return res