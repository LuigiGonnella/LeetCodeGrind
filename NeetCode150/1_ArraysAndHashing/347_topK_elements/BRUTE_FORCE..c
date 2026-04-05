/**
 * Note: The returned array must be malloced, assume caller calls free().
 */


typedef struct Element {
    int val;
    int count;
    struct Element* next;

} Element;




void insert(int val, Element **head) {
    Element* curr = *head;
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
    el -> next = *head;
    *head = el;


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
    Element* head = NULL;
    int* sol = malloc(numsSize*sizeof(int)); //overdimension
    Element all[numsSize];
    for (int i = 0; i< numsSize; i++) {
        all[i].count = -1;
    }
    (*returnSize) = 0;


    for (int i = 0; i< numsSize; i++) {
        insert(nums[i], &head);
    }

    int j = 0;
    Element* curr = head;
    while(curr != NULL) {
        all[j++] = *curr;
        curr = curr -> next;
    }
    

    merge(all, numsSize);
    for (int i = 0; i< k; i++) {
        if (all[i].count != -1) {
            sol[(*returnSize)++] = all[i].val;
        }
    }

    sol = realloc(sol, (*returnSize)*sizeof(int));
    return sol;
}

//O(N^2) time
//O(N) space