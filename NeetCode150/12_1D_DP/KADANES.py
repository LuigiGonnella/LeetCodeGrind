
#!MAX SUM
def kadane(arr):
    # Se l'array è vuoto, la somma massima è 0
    if not arr:
        return 0
        
    # Inizializziamo entrambe le variabili con il primo elemento
    max_sum = arr[0]
    current_sum = arr[0]
    
    # Iteriamo dal secondo elemento in poi
    for num in arr[1:]:
        # Decidiamo se estendere la sotto-sequenza o ricominciare
        current_sum = max(num, current_sum + num)
        # Aggiorniamo il massimo globale se abbiamo trovato di meglio
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# Test
array_esempio = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"La somma massima è: {kadane(array_esempio)}")  # Output: 6



#!MAX PRODUCT
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp_max = num * curMax
            tmp_min = num * curMin

            curMax = max(tmp_max, tmp_min, num)
            curMin = min(tmp_max, tmp_min, num)

            res = max(res, curMax)
        
        return res