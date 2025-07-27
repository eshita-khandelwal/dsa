class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build a graph (adjacency list) where each airport maps to a min-heap (priority queue)
        graph = defaultdict(list)

        for src, dest in tickets:
            heapq.heappush(graph[src], dest)  # Use heap to always get the lexicographically smallest destination

        itinerary = []  # This will hold our final result in reverse order

        def dfs(airport):
            # Visit all destinations from current airport using DFS
            while graph[airport]:
                # Always take the smallest lexical airport from the heap
                next_dest = heapq.heappop(graph[airport])
                dfs(next_dest)

            # Add airport to itinerary after visiting all its neighbors (post-order)
            itinerary.append(airport)

        # Start DFS from JFK
        dfs("JFK")

        # Since we added airports post-order, we need to reverse the list at the end
        return itinerary[::-1]