/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#define MAX_SIZE ((int)1e5)

typedef struct Element {
    int val;
    int count;
    struct Element* next;

} Element;

Element* table[MAX_SIZE];

int hash(int key, int dim) {
    return ((key % dim) + dim) % dim;
}

void initTable() {
    for (int i =0; i< MAX_SIZE; i++) {
        table[i] = NULL;
    }
}

void freeTable() {
    for (int i = 0; i < MAX_SIZE; i++) {
        Element* curr = table[i];
        
        while (curr != NULL) {
            Element* temp = curr;  // 1. Save the current node
            curr = curr->next;     // 2. Move the pointer forward safely
            free(temp);            // 3. Destroy the saved node
        }
        
        table[i] = NULL; // clean up the dangling pointer
    }
}

void insert(int val) {
    int idx = hash(val, MAX_SIZE);

    Element* curr = table[idx];
    while(curr != NULL) {
        if (curr -> val == val) {
            curr -> count +=1;
            return;
        }
        curr = curr -> next;
    }
    Element* el = malloc(sizeof(Element));
    el -> val = val;
    el -> count = 1;
    //insert in head
    el -> next = table[idx];
    table[idx] = el;


}


typedef struct Item {
    int val;
    struct Item* next;
} Item;

int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    initTable();
    int* sol = malloc(numsSize*sizeof(int)); //overdimension
    Item* lists[numsSize];
    for (int i = 0; i< numsSize; i++) {
        lists[i] = NULL;
    }
    (*returnSize) = 0;


    for (int i = 0; i< numsSize; i++) {
        insert(nums[i]);
    }

    for (int i = 0; i< MAX_SIZE; i++) {
        Element* curr = table[i];
        while(curr != NULL) {
            Item* el = malloc(sizeof(Item));
            el -> val = curr -> val;
            el -> next = lists[(curr -> count) - 1];
            lists[(curr -> count) - 1] = el;
            curr = curr -> next;
        }
    }

    for (int i = numsSize-1; i>= 0 && (*returnSize) < k; i--) {
        Item* curr = lists[i];
        while (curr != NULL) {
            sol[(*returnSize)++] = curr -> val;
            if ((*returnSize) == k) break;
            curr = curr -> next;
        }
    }

    sol = realloc(sol, (*returnSize)*sizeof(int));
    freeTable();
    //free lists
    for (int i = 0; i<numsSize; i++) {
        Item* curr = lists[i];

        while (curr != NULL) {
            Item* tmp = curr;
            curr = curr -> next;
            free(tmp);

        }
    }
    return sol;
}

//this was O(N) 