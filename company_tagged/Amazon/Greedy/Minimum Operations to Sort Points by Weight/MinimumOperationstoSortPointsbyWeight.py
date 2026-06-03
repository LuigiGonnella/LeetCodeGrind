

class Solution:
    def solve(weight, dist) -> int:

        if not weight:
            return 0

        #sort by weight maintaining original idx tracked
        points = sorted((el, idx) for idx, el in enumerate(weight))
        

        tot_steps = 0
        prev_pos = points[0][1]
        #the lowest weight never moves

        for _, idx in points[1:]: #for every other weight, in order (ascending)
            if idx <= prev_pos: #if it is before the previous, we need to move it
                step = dist[idx] #get the step
                target = prev_pos + 1 #the target is to overlap the previous
                distance = (target - idx) #we have to cover this distance

                #the steps we have to add are the ceil of distance / step (upper bound)
                steps = distance // step 
                steps += 1 if distance % step != 0 else 0
                #ceil(distance / step)
            
                tot_steps += steps #add to sol
                prev_pos = idx + (step * steps) #final id is previous id + the total distance covered
            
            else: #otherwise it stays where it is
                prev_pos = idx
            
        
        return tot_steps
    
    ####
    #weight = [2, 3, 5, 6]
    #start from idx = 0, w = 3
    #final_idx = 0
    #original_idx = 0
    #prev_el = 2 with id = 3
    #while --> final_idx = 0 + 4 = 4 > 3 --> stop
    # curr_steps = 1 --> tot_steps = 1
    #update idx of [3] with 4

