class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #use bellman ford algorithm, here we use tempPrice array so that we don't update any postion with respect to a stop without consideration
        prices = [float("infinity")] * n
        prices[src] = 0
        for i in range(k+1):
            tempPrices = prices.copy() #copy this so that we can update this for this particular stop
            for s,d,p in flights:
                if prices[s] == float("infinity"):
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s]+p
            prices = tempPrices
        return -1 if prices[dst]==float("infinity") else prices[dst]
