
#!O(orders * logN)
class Solution:
    def solve(supplierStock, orders):
        max_heap = [-stock for stock in supplierStock]
        heapq.heapify(max_heap)

        tot_revenue = 0
        while orders and max_heap:
            revenue = - heapq.heappop(max_heap)
            orders -= 1

            tot_revenue += revenue
            if revenue > 1:
                revenue -= 1
                heapq.heappush(max_heap, - revenue)
        
        return tot_revenue
