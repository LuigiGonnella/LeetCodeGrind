int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {

    qsort(nums, numsSize, sizeof(int), cmp);

    int capacity = 16;
    int** res = malloc(capacity * sizeof(int*));
    *returnSize = 0;

    for (int i = 0; i < numsSize - 2; i++) {
        if (nums[i] > 0) break;

        // skip duplicate fixed element
        if (i > 0 && nums[i] == nums[i - 1])
            continue;

        int l = i + 1;
        int r = numsSize - 1;

        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];

            if (sum == 0) {

                if (*returnSize >= capacity) {
                    capacity *= 2;
                    res = realloc(res, capacity * sizeof(int*));
                }

                int* triplet = malloc(3 * sizeof(int));
                triplet[0] = nums[i];
                triplet[1] = nums[l];
                triplet[2] = nums[r];

                res[*returnSize] = triplet;
                (*returnSize)++;

                // skip duplicates for l and r
                while (l < r && nums[l] == nums[l + 1]) l++;
                while (l < r && nums[r] == nums[r - 1]) r--;

                l++;
                r--;

            } else if (sum < 0) {
                l++;
            } else {
                r--;
            }
        }
    }

    *returnColumnSizes = malloc(*returnSize * sizeof(int));
    for (int i = 0; i < *returnSize; i++)
        (*returnColumnSizes)[i] = 3;

    return res;
}

//we could also use HASH MAPS

// Intuition
// After sorting the array, we can fix two numbers and look for the third number that completes the triplet.
// To do this efficiently, we use a hash map that stores how many times each number appears.
// As we pick the first and second numbers, we temporarily reduce their counts in the map so we don't reuse them.
// Then we check whether the needed third value still exists in the map.
// Sorting also helps us skip duplicates easily so we only add unique triplets.

// Algorithm
// Sort the array to organize duplicates and allow easy skipping.
// Build a frequency map count for all numbers.
// Initialize an empty list res for storing valid triplets.
// Loop through each index i:
// Decrease the count of nums[i] (so it won't be reused).
// Skip duplicates of the first element.
// Loop through each index j > i:
// Decrease the count of nums[j].
// Skip duplicates of the second element.
// Compute the needed third value:
// target = -(nums[i] + nums[j])
// If target still has a positive count, add the triplet.
// After finishing all js, restore the counts for the second loop by adding back the decremented values.
// Return res containing all found triplets.

//HASH MAP SOLUTION//HASH MAP SOLUTION
#define MAX_SIZE ((int)1e5)

typedef struct Item {
    int value;
    int frequency;
    struct Item* next;
} Item;

Item* table[MAX_SIZE];

int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void initTable() {
    for (int i = 0; i< MAX_SIZE; i++) {
        table[i] = NULL;
    }
}

int hash(int value) {
    return ((value % MAX_SIZE) + MAX_SIZE) % MAX_SIZE;
}

void insert(int value) {
    int idx = hash(value);
    int found = 0;
    Item* curr = table[idx];

    while (curr != NULL) {

        if (curr -> value == value) {
            curr -> frequency ++;
            found = 1;
            break;
        }

        curr = curr -> next;
    }

    if (found == 0) {
        Item* element = malloc(sizeof(Item));
        element -> value = value;
        element -> frequency = 1;
        element -> next = table[idx];
        table[idx] = element;
    }
    
}

int decrement(int value) {
    int idx = hash(value);
    Item* curr = table[idx];

    while (curr != NULL) {

        if (curr -> value == value) {
            curr -> frequency --;
            return curr -> frequency;
        }

        curr = curr -> next;
    }

    return -2;


}

void freeTable() {
    for (int i = 0; i < MAX_SIZE; i++) {
        Item* curr = table[i];
        while (curr != NULL) {
            Item* temp = curr;
            curr = curr->next;
            free(temp);
        }
        table[i] = NULL;
    }
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    initTable();
    qsort(nums, numsSize, sizeof(int), cmp);
    int currSum;
    int capacity = 16;
    int** res = malloc(capacity * sizeof(int*));
    *returnSize = 0;

    for (int i = 0; i < numsSize; i++) {
        insert(nums[i]);
    }

    for (int i = 0; i < numsSize; i++) {
        int newFreq_i = decrement(nums[i]);
        if (i > 0 && nums[i] == nums[i-1]) {
            continue;
        }

        
        for (int j = i + 1; j < numsSize; j++) {
            int newFreq_j = decrement(nums[j]);
            if (j > i + 1 && nums[j] == nums[j-1]) {
                continue;
            }
            
            currSum = nums[i] + nums[j];
            int decr = decrement(-currSum);
            if (decr > -1) {
                int* triplet = malloc(3*sizeof(int));
                triplet[0] = nums[i];
                triplet[1] = nums[j];
                triplet[2] = -currSum;

                if ((*returnSize) >= capacity) {
                    capacity *=2;
                    res = realloc(res, capacity * sizeof(int*));
                }

                res[(*returnSize)++] = triplet;
                insert(-currSum);
            }
            else if (decr == -1) {
                insert(-currSum);
            }

            
        }
        for (int j = i + 1; j < numsSize; j++) {
            insert(nums[j]);
        }
    }

    *returnColumnSizes = malloc(*returnSize * sizeof(int));
    for (int i = 0; i < *returnSize; i++)
        (*returnColumnSizes)[i] = 3;

    freeTable();
    return res;
}