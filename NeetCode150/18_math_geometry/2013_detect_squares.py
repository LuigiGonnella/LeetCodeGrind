
#!O(N) count (keys iteration and O(1) add) time and O(N) space (hash map)
class CountSquares:

    def __init__(self):
        self.squares = {} #x : MAP of y: #elements with coordinates (x,y)


    def add(self, point: List[int]) -> None:
        
        x = point[0]
        y = point[1]

        if x not in self.squares:
            self.squares[x] = defaultdict(int)
        
        self.squares[x][y] += 1

        

    def count(self, point: List[int]) -> int:

        x = point[0]
        y = point[1]

        if x not in self.squares:
            return 0 
        
        tot = 0
        
        for yN in self.squares[x].keys():
            if yN != y:
                side = yN - y
                #check upper left and upper right (side > 0) or bottom left and bottom right (side < 0)
                c1 = self.squares[x][yN] if x in self.squares else 0
                c2 = self.squares[x - side][yN] if x - side in self.squares else 0
                c3 = self.squares[x - side][y] if x - side in self.squares else 0
               

                tot += c1 * c2 * c3

                
                c1 = self.squares[x][yN] if x in self.squares else 0
                c2 = self.squares[x + side][yN] if x + side in self.squares else 0
                c3 = self.squares[x + side][y] if x + side in self.squares else 0
                

                tot += c1 * c2 * c3

        return tot
            



        
