/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int prefix_sums[numsSize];
    int suffix_sums[numsSize];
    int j;
    int* answer = malloc(numsSize * sizeof(int));
    (*returnSize) = 0;

    prefix_sums[0] = 1;
    suffix_sums[numsSize-1] = 1;
    

    for (int i=1; i<numsSize; i++) {
        prefix_sums[i] = prefix_sums[i-1] * nums[i-1];

        j=numsSize - i -1;
        suffix_sums[j] = suffix_sums[j+1] * nums[j+1];
    }

    for (int i=0; i<numsSize; i++) {
        answer[i] = prefix_sums[i] * suffix_sums[i];
        (*returnSize)++;
    }    

    return answer;
}