#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    (*returnSize) = 2;
    int* sol = malloc((*returnSize)*sizeof(int));
    
    int i = 0;
    int j = numbersSize - 1;

    while (i < j) {
        int result = numbers[i] + numbers[j];  
        if (result == target) {
            sol[0] = i + 1;
            sol[1] = j + 1;
            return sol;
        }

        if (result > target) {
            j--;
            continue;
        }
        else {
            i++;
        }
    }
    
    return NULL;
    
    
}