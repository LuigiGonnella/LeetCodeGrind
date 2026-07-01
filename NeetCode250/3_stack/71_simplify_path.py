
#!O(N) time and O(1) extra space
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""

        stack = []
        
        stack.append(path[0])
        i = 1
        glob_name = ""
        while i < len(path):
            char = path[i]
            if char != "." and char != "/":
                name = glob_name + char #inherit global_name, potentially filled of points

                while i < len(path) - 1 and path[i + 1] != "/": #if we have points next we have to add them to the name, we stop when we encount a slash
                    
                    name += path[i + 1]
                    i += 1
                
                stack.append(name)
                glob_name = "" #reset global_name

            elif char == "/" and stack and stack[-1] != "/":
                stack.append(char)
            elif char == ".":
                points = "."

                while i < len(path) - 1 and path[i + 1] == ".":
                    
                    points += path[i + 1]
                    i += 1
                
                if i < len(path) - 1 and path[i + 1] != "/": #if after points we have a letter --> treat like a name updating global_name
                    glob_name = points

                elif len(points) >= 3:
                    stack.append(points)
                elif len(points) == 2:
                    pops = 2
                    while len(stack) > 1 and pops:
                        stack.pop()
                        pops -= 1

                #skip if just one point
            
            i += 1
        
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        
        return "".join(stack)
                    

                

