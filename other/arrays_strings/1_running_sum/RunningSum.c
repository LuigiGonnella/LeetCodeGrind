#include <stdio.h>
#define N 10



int* solve(int* vec, int len) {

    for (int i = 1; i < len; i++) {
        vec[i] += vec[i-1];
    }

    return vec;
}



void main(void) {
    int v1[N] = {2, 1, 5, 6, 10, 12, 2, 1, 1, 2};

    printf("The running sum vector is\n");
    int* res = solve(v1, N);

    for (int i =0; i< N; i++) {
        printf("%d ", res[i]);
    }
    
}