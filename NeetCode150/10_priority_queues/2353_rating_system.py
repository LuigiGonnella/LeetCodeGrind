
#!O(logN) per change, while with linear search would have been O(N)
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.FoodToCus = {}
        self.CusToRat = defaultdict(list)
        self.FoodToRat = {} #for lazy update

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.FoodToCus[food] = cuisine
            self.FoodToRat[food] = rating
            heapq.heappush(self.CusToRat[cuisine], (-rating, food))



    def changeRating(self, food: str, newRating: int) -> None:
        # for i, (_, foodKey) in enumerate(self.CusToRat[self.FoodToCus[food]]):
        #     if foodKey == food:
        #         self.CusToRat[self.FoodToCus[food]][-1],  self.CusToRat[self.FoodToCus[food]][i] = self.CusToRat[self.FoodToCus[food]][i],  self.CusToRat[self.FoodToCus[food]][-1]
        #         self.CusToRat[self.FoodToCus[food]].pop()
        #         self.CusToRat[self.FoodToCus[food]].append((-newRating, food))
        #         heapq.heapify(self.CusToRat[self.FoodToCus[food]])
        #         return

        self.FoodToRat[food] = newRating
        heapq.heappush(self.CusToRat[self.FoodToCus[food]], (-newRating, food))

        
        

    def highestRated(self, cuisine: str) -> str:
        heap = self.CusToRat[cuisine]

        while heap:
            rat, food = heap[0]
            if - rat == self.FoodToRat[food]:
                return food
            
            heapq.heappop(heap) #lazy delete
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)