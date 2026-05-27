

class ...:
    self.bl = -1
    self.res = []
    
    def check(sol, val):
        curr = float("-inf")
        for i, el in enumerate(sol):
            if el != 0:
                if val[i] > curr:
                    curr = val[i]
                else:
                    return False
        
        return True


    def disp_rip(pos, sol, val, n): 
        if pos >= n and check(sol, val):
            curr_val = []
            for i, el in enumerate(sol):
                if el != 0:
                    l += 1 
                    curr_val.append(val[i])
                
            
            if len(curr_val) > self.bl:
                self.bl = len(curr_val)
                self.res = curr_val

            return
                    
        sol[pos] = 0
        disp_rip(pos + 1, sol, val, n)
        sol[pos] = 1
        disp_rip(pos + 1, sol, val, n)


    
