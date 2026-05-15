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
    if (key < 0) key = -key;

    return key % dim;
}

void initTable() {
    for (int i =0; i< MAX_SIZE; i++) {
        Element* el = malloc(sizeof(Element));
        if (el == NULL) {
            printf("Error in allocating table");
            return;
        } 
        el -> count = 0;
        el -> val = i;
        el -> next = NULL;
        table[i] = el;
    }
}

void freeTable() {
    for (int i =0; i< MAX_SIZE; i++) {
        free(table[i]);
    }
}

void insert(int val) {
    int idx = hash(val, MAX_SIZE);
    printf("INDEX: %d\n", idx);

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

void two_way_merge(Element A[], Element *B, int l, int r, int q) {
    int i = l;
    int j = q + 1;

    for (int k = l; k <= r; k ++) {
        if (i > q) {
            B[k] = A[j++];
        }
        else if (j > r) {
            B[k] = A[i++];
        }
        else if (A[i].count >= A[j].count) { //stability
            B[k] = A[i++];
        }
        else {
            B[k] = A[j++];
        }
    }

    for (int k = l; k <= r; k ++) {
        A[k] = B [k];
    }

}

void mergeR(Element A[], Element *B, int l, int r) {

    if (l >= r) {
        return; //not present
    }

    int q = (l + r) / 2;

    mergeR(A, B, l, q); 
    mergeR(A, B, q+1, r);
    two_way_merge(A, B, l, r, q);
}


void merge(Element A[], int size) {
    Element *B = malloc(size * sizeof(Element));
    int l = 0;
    int r = size - 1; 

    mergeR(A, B, l, r);
}

int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    initTable();
    int* sol = calloc(MAX_SIZE, sizeof(int)); //overdimension
    Element all[numsSize];
    for (int i = 0; i< numsSize; i++) {
        all[i].count = -1;
    }
    (*returnSize) = 0;


    for (int i = 0; i< numsSize; i++) {
        insert(nums[i]);
    }

    int j = 0;
    for (int i = 0; i< MAX_SIZE; i++) {
        Element* curr = table[i];
        while(curr != NULL && curr -> count != 0) {
            all[j++] = *curr;
            curr = curr -> next;
        }
    }

    merge(all, numsSize);
    for (int i = 0; i< k; i++) {
        if (all[i].count != -1) {
            sol[(*returnSize)++] = all[i].val;
        }
    }

    sol = realloc(sol, (*returnSize)*sizeof(int));
    freeTable();
    return sol;
}

//this was O(NlogN) 


//EXPLORE OTHER SOLUTION (better complexity)

