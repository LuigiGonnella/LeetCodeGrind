#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool searchR(int** matrix, int l, int r, int rows, int cols, int target) {
    int m, i, j;
    if (l > r) {
        return false;
    }

    m = (l + r) / 2;
    i = m/cols;
    j = m%cols;

    if (matrix[i][j] == target) {
        return true;
    }
    else if (target < matrix[i][j]) {
        return searchR(matrix, l, m-1, rows, cols, target);
    }

    return searchR(matrix, m+1, r, rows, cols, target);
}


bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int n_elements = matrixSize * matrixColSize[0];
    int l = 0, r = n_elements - 1;

    return searchR(matrix, l, r, matrixSize, matrixColSize[0], target);
    
}
