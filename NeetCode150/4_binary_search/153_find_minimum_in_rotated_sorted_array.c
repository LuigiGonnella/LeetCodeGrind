// Time Complexity: O(log n) because it halves the search space every iteration.
// Space Complexity: O(1) because it only uses a few integer variables.

int findRotations(int* nums, int l, int r) {
    int firstNum = nums[0];
    int m;
    int index_found = 0;

    while (l <= r) {
        m = l + (r-l) /2; //!AVOIDS overflow if l and r are massive numbers
        if (nums[m] > firstNum) {
            //go right
            if (m > index_found) {
                index_found = m;
            }
            l = m + 1;
        }
        else { 
            // go left
            r = m - 1;
        }
    }

    return index_found + 1;

}


int findMin(int* nums, int numsSize) {
    if (numsSize == 0) {
        return -1;
    }

    int n_rotations = findRotations(nums, 1, numsSize-1) % numsSize;
    return nums[n_rotations];
    
}