typedef struct Item {
    int val;
    int streak;
    struct Item* next;
} Item;

int hash(int val, int dim) {
    return ((val % dim) + dim) % dim;
}

int getStreak(Item** table, int val, int dim) {
    int idx = hash(val, dim);
    Item* curr = table[idx];

    while (curr != NULL) { 
        if (curr -> val == val) {
            return curr -> streak;
        }
        curr = curr -> next;
    }

    return 0;
}

void insertStreak(Item** table, int val, int streak, int dim) {
    int idx = hash(val, dim);

    Item* curr = table[idx];

    while (curr != NULL) { 
        if (curr -> val == val) {
            curr -> streak = streak;
            return;
        }
        curr = curr -> next;
    }
}

int insert(Item** table, int val, int dim) {
    int idx = hash(val, dim);

    Item* curr = table[idx];

    while (curr != NULL) { 
        if (curr -> val == val) { //already present
            return 0;
        }
        curr = curr -> next;
    }

    //not present
    Item* el = malloc(sizeof(Item));
    el -> val = val;
    int leftStreak = getStreak(table, val-1, dim);
    int rightStreak = getStreak(table, val+1, dim);
    int currStreak = leftStreak + rightStreak + 1;
    el -> streak = currStreak;
    el -> next = table[idx];
    table[idx] = el;

    //update boundaries
    int leftBoundary = val - leftStreak;
    int rightBoundary = val + rightStreak;
    insertStreak(table, leftBoundary, currStreak, dim);
    insertStreak(table, rightBoundary, currStreak, dim);

    return currStreak;

}

int longestConsecutive(int* nums, int numsSize) {
    Item** table = calloc(numsSize, sizeof(Item*));


    int maxStreak = 0;
    int currStreak;
    for(int i =0; i<numsSize;i++) {
        currStreak = insert(table, nums[i], numsSize);
        if (currStreak > maxStreak) {
            maxStreak = currStreak;
        }
    }

    free(table);

    return maxStreak;

}