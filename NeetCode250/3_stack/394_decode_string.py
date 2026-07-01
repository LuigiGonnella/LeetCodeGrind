
#!O(n + N) time and O(1) extra space
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:

            if char != "]":
                stack.append(char)
            
            else:
                

                # el = ""
                # while stack and stack[-1] != "[":
                #     el = stack.pop() + el --> !this would cause N^2 instead of N

                tmp = []
                while stack and stack[-1] != "[":
                    tmp.append(stack.pop())
                    
                tmp.reverse()
                el = "".join(tmp)
                stack.pop() #pop [
                
                k = 0
                mul = 1
                while stack and len(stack[-1]) == 1 and 0 <= (ord(stack[-1]) - ord("0")) <= 9:
                    k += int(stack.pop()) * mul #pop k
                    mul *= 10

                el *= k
                stack.append(el)
        
        return "".join(stack)



        