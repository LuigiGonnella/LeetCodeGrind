#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct Element {
    char name;
    int size; // weight
    int val;  // value
} Element;



void solveR(Element* items, int* sol, int n, int* best_items, int* best_val, int curr_cap, int max_cap, int curr_val, int pos) {

    if (pos >= n) {
        if (curr_val > *best_val) { //no need to check **size** correctness... already guaranteed by pruning condition during recursion
            *best_val = curr_val;
            for (int i = 0; i< n; i++) {
                best_items[i] = sol[i];
            }
        }
        return;
    }

    if (curr_cap + items[pos].size <= max_cap) {
        sol[pos] = 1;
        curr_cap += items[pos].size;
        curr_val += items[pos].val;

        solveR(items, sol, n, best_items, best_val, curr_cap, max_cap, curr_val, pos+1);

        sol[pos] = 0;
        curr_cap -= items[pos].size;
        curr_val -= items[pos].val;
        solveR(items, sol, n, best_items, best_val, curr_cap, max_cap, curr_val, pos+1);
    }
    else {
        sol[pos] = 0;
        solveR(items, sol, n, best_items, best_val, curr_cap, max_cap, curr_val, pos+1);
    }

}


int main() {
    int n = 4;
    Element* items = malloc(n * sizeof(Element));
    int* sol = malloc(n * sizeof(int));
    int* best_items = malloc(n * sizeof(int));
    int best_val = INT_MIN;


     // Initialize items according to the provided table:
    // Name:  A   B   C   D
    // Value: 10  6   8   9
    // Weight:8   4   2   3
    items[0].name = 'A'; items[0].val = 10; items[0].size = 8;
    items[1].name = 'B'; items[1].val = 6;  items[1].size = 4;
    items[2].name = 'C'; items[2].val = 8;  items[2].size = 2;
    items[3].name = 'D'; items[3].val = 9;  items[3].size = 3;

   solveR(items, sol, n, best_items, &best_val, 0, 10, 0, 0);

   printf("Maximum value = %d\n", best_val);
   printf("Best items: ");
   for (int i =0; i<n; i++) {
    printf("%d ", best_items[i]);
   }





    free(items);



    return 0;
}