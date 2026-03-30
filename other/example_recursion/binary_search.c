#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


int bin_search(int* vec, int l, int r, int k) {

    if (l > r) {
        return -1; //not present
    }

    int m = (l + r) / 2;

    if (vec[m] == k) {
        return m;
    }

    if (vec[m] > k) {
        return bin_search(vec, l, m, k); 
        
    }

    return bin_search(vec, m+1, r, k);

    
}

int main() {
    int vec[10] = {1, 3, 4, 6, 10, 23, 25, 26, 90, 330};

    int idx = bin_search(vec, 0, 9, 25); //6
    printf("The index of %d is %d", 25, idx);

    return 0;
}

