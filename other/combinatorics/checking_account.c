#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


void check(int *sol, int*min, int* best, int n) {
    int curr_max;
    int curr_min;
    int curr_diff;
    int curr_sum = 0;

    for (int i =0; i<n; i++) {
        curr_sum += sol[i];
        if (i==0) {
            curr_max = sol[i];
            curr_min = sol[i];
        }
        else {
            if (curr_sum < curr_min) curr_min = curr_sum;
            if (curr_sum > curr_max) curr_max = curr_sum;
        }

    }
    curr_diff = curr_max - curr_min;
    if (curr_diff < *min) {
        *min = curr_diff;
        for (int i=0; i< n; i++) {
            best[i] = sol[i];
        }
    } 


}


void solveR(int* val, int* sol, int n, int*min, int*mark, int* best, int pos) {

    if (pos >= n) {
        check(sol, min, best, n);
        return;
    }


    for (int i = 0; i< n; i++) {

        if (mark[i]==0) {
            mark[i] = 1;
            sol[pos] = val[i];
            solveR(val, sol, n, min, mark, best, pos+1);
            mark[i] = 0;
        }

        
    }

}


int main() {
    int n = 10;
    int ref[10] = {-1, -6, 3, 14, -5, 16, 7, 8, -9, 120};
    int* val = malloc(n * sizeof(int));
    int* sol = malloc(n * sizeof(int));
    int* best = malloc(n * sizeof(int));
    int* mark = calloc(n, sizeof(int));
    int min = INT_MAX;

    for (int i=0; i< n; i++) {
        val[i] = ref[i];
    }

    solveR(val, sol, n, &min, mark, best, 0);
    printf("Minimum difference: %d\n", min);
    printf("Best order:  [");
    for (int i = 0; i < n; i ++) {
        printf("%d", best[i]);
        if (i != n - 1) {
            printf(" ");
        }
    }
    printf("]");


    return 0;
}