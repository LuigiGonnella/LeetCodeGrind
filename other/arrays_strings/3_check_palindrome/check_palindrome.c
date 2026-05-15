#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 9



int solve(char vec[N], int len) {
    int start = 0;
    int end = len-1;

    while(start<end) {
        if (vec[start++] != vec[end--]) return 0;
    }

    return 1;
}



void main(void) {
    char v1[N] = {'a', 'b', 'c', 'd', 'd', 'c', 'b', 'a', '\0'};

    printf("Is \"%s\" palindrome?\n", v1);

    if (solve(v1, strlen(v1))) {
        printf("True"); 
        return;
    } 
    
    printf("False");
    

    
}