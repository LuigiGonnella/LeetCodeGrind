#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 32

typedef struct binary {
    int* bit;
    int len;
} binary;

binary* solve(int number) {
    int i, bit[N];
    i = 0;

    do {
        bit[i] = number % 2; //Least significant bit, we need to print in reverse later
        number /= 2;

        i++;

    } while (number > 0); // if number == 0 --> bits = [0]
    
    i --;

    int* sol = malloc(N * sizeof(int));
    int j = 0;
    while (i>=0) {
        sol[j++] = bit[i--];
    }   

    binary* final = malloc(sizeof(binary));

    final ->bit = sol;
    final -> len = j;

    return final;
}



void main(void) {
    int number = 12;

    printf("The binary encoding of %d is:\n", number);

    binary* res;
    res = solve(number);

    for (int i = 0; i< res -> len; i++) {
        printf("%d ", res -> bit[i]);
    }

    free(res);
}