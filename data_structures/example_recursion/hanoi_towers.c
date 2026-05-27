#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


void hanoi_towers(int n, int src, int dst) {
    int aux = 3 - (src + dst);
    if (n == 1) {
        printf("src: %d -> dst: %d\n", src, dst);
        return;
    }

    hanoi_towers(n-1, src, aux); // n-1 da src a aux
    printf("src: %d -> dst: %d\n", src, dst); //1 da src a dst
    hanoi_towers(n-1, aux, dst); // n-1 da aux a dst
}

int main() {
    hanoi_towers(3, 0, 2);
}

