from typing import List


class Solution:

    # BELLMAN FORD ALGORITHM
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices.copy()
            for edge in flights:
                if prices[edge[0]] == float('inf'):
                    continue
                temp_prices[edge[1]] = min(temp_prices[edge[1]], prices[edge[0]] + edge[2])
            prices = temp_prices.copy()
        return prices[dst] if prices[dst] != float('inf') else -1