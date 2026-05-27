#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


int find_max_el(int* vec, int l, int r) {
    int u, v;

    if (l == r) {
        return vec[l];
    }

    int m = (l + r) / 2;
    printf("GO TO LEFT (%d, %d) FROM :", l, m);
    for (int i = l; i < r; i++) {
        printf("%d ", vec[i]);
    }
    printf("\n");
    
    u = find_max_el(vec, l, m);
    printf(" -- > %d\n", u);

    printf("GO TO RIGHT (%d, %d) FROM :", m + 1, r);
    for (int i = l; i <= r; i++) {
        printf("%d ", vec[i]);
    }
    printf("\n");
    
    v = find_max_el(vec, m+1, r);
    printf(" -- > %d\n", v);

    if (u > v) {
        printf(" MAX: %d\n", u);
        return u;
    }
    else {
        printf(" MAX: %d\n", v);
        return v;
    
    }
    



}

int main() {
    int vec[10] = {4, 2, 6, 78, 1, 23, 5, 2, 9, 33};

    int max_el = find_max_el(vec, 0, 9);
    printf("The max number is %d", max_el);

    return 0;
}

