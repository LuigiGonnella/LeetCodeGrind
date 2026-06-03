

#BRUTE FORCE
#!O(R * S) --> for each request find lowest server and update server

#!O(R * logS) --> same but with binary search starting as right = r (request)
class Solution:
    def findRequestTarget(num_servers: int, requests: List[int]) -> List[int]:

        alloc_state = [0] * num_servers #tracks number of requests handling by each server --> always deascending monotonic

        res = []

        for r in requests:
            server_idx = r
            min_alloc = alloc_state[r]
            left, right = 0, r #inclusive

            while left <= right:

                mid = left + (right - left) // 2

                if alloc_state[mid] <= min_alloc:
                    server_idx = mid

                    #go left to find the leftmost one
                    right = mid - 1
                else: #go right to find the minimum one
                    left = mid + 1
            

            alloc_state[server_idx] += 1
            res.append(server_idx)


        return res

#!O(R * logS) --> same but with MIN SEGMENT TREE

#!O(R + S) time (we intialize alloc_state having length S) and O(max(R, S)) space
class Solution:
    def findRequestTarget(num_servers: int, requests: List[int]) -> List[int]:

        alloc_state = [0] * num_servers #tracks number of requests handling by each server --> always deascending monotonic
        next_server = [0] * (len(requests) + 1) #tracks next server to assign to each request

        res = []

        for r in requests:
            #the minimum allocations available are in alloc_state[r] since the lowest <= r is always at last index r
            min_alloc = alloc_state[r]

            #for the tiebreaker we need to find the lowest index, this is tracked by next_server
            idx = next_server[min_alloc]

            alloc_state[idx] += 1 #increment load of the chosen server
            next_server[min_alloc] += 1 #increment solution idx server for the old allocation since the current server has more load, so the correct server for the previous load is the next server
            #this is possible because the correct server is always the first of the server having the same load and for sure ther will be NO server in next position having a lower load (monotonic decreasing)

            res.append(idx)
        
        return res



