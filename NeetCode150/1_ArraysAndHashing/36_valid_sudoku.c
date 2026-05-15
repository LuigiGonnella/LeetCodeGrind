#define DIM 9
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool checkRow(char** board, int row, int col, int occurs[]) {
    if (col >= DIM) {
        return true;
    }

    if (board[row][col] != '.' && (board[row][col] < '1'  || board[row][col] > '9')) {
        printf("problem with %c --> out of range\n", board[row][col]);
        return false;
    }

    if (board[row][col] == '.') {
        return checkRow(board, row, col+1, occurs);    
    }

    if (occurs[(board[row][col]) - '0' -1] == 0) {
        printf("problem with %c --> too many repetitions\n", board[row][col]);
        return false;
    }



    occurs[(board[row][col]) - '0' -1]  -= 1;
    return checkRow(board, row, col+1, occurs);    
}

bool checkCol(char** board, int row, int col, int occurs[]) {
    if (row >= DIM) {
        return true;
    }

    if (board[row][col] != '.' && (board[row][col] < '1'  || board[row][col] > '9')) {
        return false;
    }

    if (board[row][col] == '.') {
        return checkCol(board, row+1, col, occurs);    
    }

    if (occurs[(board[row][col]) - '0' -1] == 0) {
        return false;
    }



    occurs[(board[row][col]) - '0' -1] -= 1;
    return checkCol(board, row+1, col, occurs);    
}

bool checkSquare(char** board, int row, int col, int occurs[], int i, int j) {
    if (i >= 3) {
        return true;
    }

    if (j >= 3) {
        j=0;
        return checkSquare(board, row, col, occurs, i+1, j);
    }

    if (board[row+i][col+j] != '.' && (board[row+i][col+j] < '1'  || board[row+i][col+j] > '9')) {
        return false;
    }

    if (board[row+i][col+j] == '.') {
        return checkSquare(board, row, col, occurs, i, j+1);    
    }

    if (occurs[(board[row+i][col+j]) - '0' -1] == 0) {
        return false;
    }

    occurs[(board[row+i][col+j]) - '0' -1]  -= 1;
    return checkSquare(board, row, col, occurs, i, j+1);  

}


bool isValidSudoku(char** board, int boardSize, int* boardColSize) {

    for (int i =0; i<boardSize; i++) {
        int digits[9] = {1, 1, 1, 1, 1, 1, 1, 1, 1};
        if (!checkRow(board, i, 0, digits)) {
            printf("Error in row %d\n", i);
            return false;
        }
    }

    for (int j =0; j<boardColSize[0]; j++) {
        int digits[9] = {1, 1, 1, 1, 1, 1, 1, 1, 1};
        if (!checkCol(board, 0, j, digits)) {
            printf("Error in col %d\n", j);
            return false;
        }
    }

    for (int i=0; i<boardSize; i++) {
        for (int j =0; j<boardColSize[i]; j++) {
            if (i%3 == 0 && j%3 == 0 ) {
                int digits[9] = {1, 1, 1, 1, 1, 1, 1, 1, 1};
                if (!checkSquare(board, i, j, digits, 0, 0)) {
                    printf("Error in square (%d, %d)\n", i, j);
                    return false;
                }
            }
        }
    }

    return true;
    
}

//THIS IS O(3*N^2) = three passes reading all cells (still O(N^2) in big o notation)

//SOLUTION WITH ONLY 1 PASS --> "pure" O(N^2)

typedef struct Element {
    int val;
    struct Element* next;
} Element;

Element* rows[DIM];
Element* cols[DIM];
Element* squares[DIM];

int hashSquare(int r, int c) {
    return (r/3)*3 + c/3; //with only r/3 + c/3 i obtain coordinates but (0,1) would be identical to (1,0), so i need to "flatten" with (Y*width) + X formula
}

void initHashTables() {
    for (int i=0;i<DIM;i++) {
        rows[i] = cols[i] = squares[i] = NULL;
    }
}

bool inserInHashSet(Element** head, int val) {
    Element* curr = *head;

    while(curr != NULL) {
        if (curr -> val == val) {
            printf("found duplicate --> %d\n", val);
            return false;
        }
        printf("found --> %d\n", curr -> val);


        curr = curr->next;
    }

    Element* el = malloc(sizeof(Element));
    el -> val = val;
    el -> next = *head;
    *head = el;
    printf("insert %d in head\n", val);
    return true;
}   

bool insert(int val, int rowIdx, int colIdx) {
    int squareIdx = hashSquare(rowIdx, colIdx);

    printf("Inserting %d at row index %d, column index %d and square index %d...\n\n", val, rowIdx, colIdx, squareIdx);
    if (!inserInHashSet(&rows[rowIdx], val)) {
        printf("problem in row %d\n", rowIdx);
        return false;
    }
    if (!inserInHashSet(&cols[colIdx], val)) {
        printf("problem in col %d\n", colIdx);
        return false;
    }

    return inserInHashSet(&squares[squareIdx], val);
}

bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    initHashTables();

    for (int i=0;i<boardSize;i++) {
        for(int j=0;j<boardColSize[i];j++) {
            if (board[i][j] == '.') {
                continue;
            }

            if (board[i][j] < '1' ||  board[i][j] > '9') {
                return false;
            }

            if (!insert(board[i][j]-'0', i, j)) {
                return false;
            }
        }
    }

    return true;


    
}