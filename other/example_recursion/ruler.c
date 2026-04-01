#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//given 'n' i have to print 2^n ticks where the middle tick ha heigth n, the middle in the 2 half has height n-1, .... 


void mark(int m, int h) {
    printf("%d \t", m);
    for (int i = 0; i<h; i++) {
        printf("*");
    }
    printf("\n");
}


void ruler(int l, int r, int h) { 
    int m = (l + r) / 2;

    if (h > 0) {
        ruler(l, m, h-1);
        mark(m, h);
        ruler(m, r, h -1);
    }

}

int main() {

    ruler(0, 8, 4);
    return 0;
}