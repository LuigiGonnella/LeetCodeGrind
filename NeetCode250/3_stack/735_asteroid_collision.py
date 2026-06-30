
#!O(N)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for ast in asteroids:
            
            if ast < 0: #if negative, can collide with left positive asteroids
                exploded = False
                while stack and stack[-1] > 0 and abs(ast) >= abs(stack[-1]): #while top stack is positive and my negative asteroid has bigger abs --> my asteroid survives
                    top = stack.pop() #explode positive asteroid
                    if abs(ast) == abs(top): #if they are equal, explode also my asteroid
                        exploded = True
                        break
                
                if exploded: #if exploded, go next
                    continue

                if not stack or (stack and stack[-1] < 0): #if my asteroid survived through all positives (all stack or until first negative)
                    stack.append(ast) #add to stack
            
            else: #if positive asteroid, it will never collide (goes on the right, with no negatives ahead)
                stack.append(ast)
            
    
        
        return stack
        